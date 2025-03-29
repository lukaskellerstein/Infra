import logging
import traceback
from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
from fastapi.responses import JSONResponse
import uvicorn

# Initialize FastAPI
app = FastAPI()

# === Logging Configuration ===
log_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(log_formatter)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# === Model for POST payload ===
class EchoPayload(BaseModel):
    message: str


# === Middleware to log requests ===
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    start_time = datetime.utcnow()

    try:
        response = await call_next(request)
    except Exception as e:
        logger.exception("Unhandled exception occurred during request handling.")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error"}
        )

    duration = (datetime.utcnow() - start_time).total_seconds()
    logger.info(f"Completed in {duration:.4f}s - Status: {response.status_code}")

    return response


# === Endpoints ===
@app.get("/")
def read_root():
    try:
        logger.info("GET / called")
        return {"message": "Welcome to the FastAPI example!"}
    except Exception:
        logger.exception("Error in GET /")
        return JSONResponse(status_code=500, content={"error": "Something went wrong"})


@app.get("/status")
def get_status():
    try:
        logger.info("GET /status called")
        return {"status": "ok", "version": "1.0.0"}
    except Exception:
        logger.exception("Error in GET /status")
        return JSONResponse(status_code=500, content={"error": "Something went wrong"})


@app.post("/echo")
def echo_message(payload: EchoPayload):
    try:
        logger.info(f"POST /echo called with payload: {payload.dict()}")
        return {"you_sent": payload.message}
    except Exception:
        logger.exception("Error in POST /echo")
        return JSONResponse(status_code=500, content={"error": "Something went wrong"})


# === Run with uvicorn if run directly ===
if __name__ == "__main__":
    try:
        logger.info("Starting server with uvicorn...")
        uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        logger.error("Failed to start server.")
        logger.error(traceback.format_exc())
