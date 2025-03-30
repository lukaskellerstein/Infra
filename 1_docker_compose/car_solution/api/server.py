from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId
import uvicorn
import traceback
import os

PORT = int(os.environ.get("PORT", 8000))
DB_URL = os.environ.get("DB_URL", "db") 
DB_PORT = int(os.environ.get("DB_PORT", 27017)) 


app = FastAPI()
client = MongoClient(f"mongodb://{DB_URL}:{DB_PORT}/")
db = client["car_db"]
cars_collection = db["cars"]

class Car(BaseModel):
    make: str
    model: str
    year: int

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/cars")
def create_car(car: Car):
    car_dict = car.dict()
    result = cars_collection.insert_one(car_dict)
    created_car = cars_collection.find_one({"_id": result.inserted_id})
    created_car["id"] = str(created_car.pop("_id"))
    return created_car

@app.get("/cars")
def get_all_cars():
    cars = []
    for car in cars_collection.find():
        car["id"] = str(car.pop("_id"))
        cars.append(car)
    return cars

@app.get("/cars/{car_id}")
def get_car(car_id: str):
    car = cars_collection.find_one({"_id": ObjectId(car_id)})
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    car["id"] = str(car.pop("_id"))
    return car

@app.put("/cars/{car_id}")
def update_car(car_id: str, car: Car):
    result = cars_collection.update_one({"_id": ObjectId(car_id)}, {"$set": car.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"status": "updated"}

@app.delete("/cars/{car_id}")
def delete_car(car_id: str):
    result = cars_collection.delete_one({"_id": ObjectId(car_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"status": "deleted"}

# === Run with uvicorn if run directly ===
if __name__ == "__main__":
    try:
        print("Starting server with uvicorn...")
        uvicorn.run("server:app", host="0.0.0.0", port=PORT, reload=True)
    except Exception as e:
        print("Failed to start server.")
        print(traceback.format_exc())