import grpc
from concurrent import futures
import time
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

import product_pb2
import product_pb2_grpc

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["ecommerce"]
products_collection = db["products"]

class ProductServiceServicer(product_pb2_grpc.ProductServiceServicer):
    def CreateProduct(self, request, context):
        product = {
            "name": request.name,
            "price": request.price
        }
        result = products_collection.insert_one(product)
        return product_pb2.CreateProductResponse(id=str(result.inserted_id))

    def GetProduct(self, request, context):
        product = products_collection.find_one({"_id": ObjectId(request.id)})
        if product:
            return product_pb2.GetProductResponse(
                id=str(product["_id"]),
                name=product["name"],
                price=product["price"]
            )
        else:
            context.set_details("Product not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return product_pb2.GetProductResponse()

    def ListProducts(self, request, context):
        products = []
        for prod in products_collection.find():
            products.append(product_pb2.GetProductResponse(
                id=str(prod["_id"]),
                name=prod["name"],
                price=prod["price"]
            ))
        return product_pb2.ListProductsResponse(products=products)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Product Service started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
