import grpc
from concurrent import futures
import time
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

import order_pb2
import order_pb2_grpc

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["ecommerce"]
orders_collection = db["orders"]

class OrderServiceServicer(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        order = {
            "product_id": request.product_id,
            "quantity": request.quantity
        }
        result = orders_collection.insert_one(order)
        return order_pb2.CreateOrderResponse(id=str(result.inserted_id))

    def GetOrder(self, request, context):
        order = orders_collection.find_one({"_id": ObjectId(request.id)})
        if order:
            return order_pb2.GetOrderResponse(
                id=str(order["_id"]),
                product_id=order["product_id"],
                quantity=order["quantity"]
            )
        else:
            context.set_details("Order not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return order_pb2.GetOrderResponse()

    def ListOrders(self, request, context):
        orders = []
        for order in orders_collection.find():
            orders.append(order_pb2.GetOrderResponse(
                id=str(order["_id"]),
                product_id=order["product_id"],
                quantity=order["quantity"]
            ))
        return order_pb2.ListOrdersResponse(orders=orders)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Order Service started on port 50052")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
