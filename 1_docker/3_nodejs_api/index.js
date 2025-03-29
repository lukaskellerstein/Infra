import express from "express";
import morgan from "morgan";
import { z } from "zod";
import logger from "./logger.js";

const app = express();
const port = 8000;

// Middleware for JSON parsing
app.use(express.json());

// Middleware for logging HTTP requests
app.use(
  morgan("combined", {
    stream: {
      write: (message) => logger.info(message.trim()),
    },
  })
);

// Timing middleware
app.use(async (req, res, next) => {
  const start = Date.now();
  res.on("finish", () => {
    const duration = ((Date.now() - start) / 1000).toFixed(4);
    logger.info(`Completed in ${duration}s - Status: ${res.statusCode}`);
  });

  logger.info(`Incoming request: ${req.method} ${req.originalUrl}`);
  next();
});

// Routes
app.get("/", (req, res) => {
  logger.info("GET / called");
  res.json({ message: "Welcome to the Express example!" });
});

app.get("/status", (req, res) => {
  logger.info("GET /status called");
  res.json({ status: "ok", version: "1.0.0" });
});

const echoSchema = z.object({
  message: z.string(),
});

app.post("/echo", (req, res) => {
  try {
    const parsed = echoSchema.parse(req.body);
    logger.info(`POST /echo called with payload: ${JSON.stringify(parsed)}`);
    res.json({ you_sent: parsed.message });
  } catch (err) {
    logger.error(`Validation error in POST /echo: ${err}`);
    res.status(400).json({ error: "Invalid request payload" });
  }
});

// Error handler
app.use((err, req, res, next) => {
  logger.error(`Unhandled exception: ${err.stack}`);
  res.status(500).json({ error: "Internal server error" });
});

// Start server
app.listen(port, () => {
  logger.info(`Server listening on http://0.0.0.0:${port}`);
});
