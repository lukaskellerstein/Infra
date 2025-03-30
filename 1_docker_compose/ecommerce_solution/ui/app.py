from flask import Flask, render_template, request, redirect, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import grpc
import os

# Import the generated code for product and order services
import product_pb2
import product_pb2_grpc
import order_pb2
import order_pb2_grpc

URL_ROOT_PATH = os.environ.get("URL_ROOT_PATH", "/")
PORT = int(os.environ.get("PORT", 5000))
PRODUCT_SERVICE_URL = os.environ.get("PRODUCT_SERVICE_URL", "product-service:50051")
ORDER_SERVICE_URL = os.environ.get("ORDER_SERVICE_URL", "order-service:50052")

app = Flask(__name__)

def get_product_stub():
    # Connect to the product service by its docker service name
    channel = grpc.insecure_channel(PRODUCT_SERVICE_URL)
    stub = product_pb2_grpc.ProductServiceStub(channel)
    return stub

def get_order_stub():
    # Connect to the order service by its docker service name
    channel = grpc.insecure_channel(ORDER_SERVICE_URL)
    stub = order_pb2_grpc.OrderServiceStub(channel)
    return stub

@app.route('/')
def index():
    stub = get_product_stub()
    response = stub.ListProducts(product_pb2.ListProductsRequest())
    products = response.products
    return render_template('index.html', products=products)

@app.route('/create', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price = float(request.form.get('price'))
    stub = get_product_stub()
    stub.CreateProduct(product_pb2.CreateProductRequest(name=name, price=price))
    return redirect(url_for('index'))

# New endpoints for order usage

@app.route('/orders')
def list_orders():
    # Fetch orders from order service
    order_stub = get_order_stub()
    orders_response = order_stub.ListOrders(order_pb2.ListOrdersRequest())
    orders = orders_response.orders
    # Also fetch products to show product names in orders
    product_stub = get_product_stub()
    products_response = product_stub.ListProducts(product_pb2.ListProductsRequest())
    # Build a dictionary mapping product ID to product name
    products = {p.id: p.name for p in products_response.products}
    return render_template('orders.html', orders=orders, products=products)

@app.route('/orders/create', methods=['POST'])
def create_order():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity'))
    order_stub = get_order_stub()
    order_stub.CreateOrder(order_pb2.CreateOrderRequest(product_id=product_id, quantity=quantity))
    return redirect(url_for('list_orders'))

if __name__ == '__main__':
    app.config['APPLICATION_ROOT'] = URL_ROOT_PATH

    # Mount the Flask app under the desired prefix using DispatcherMiddleware
    application = DispatcherMiddleware(Flask('dummy_app'), {
        URL_ROOT_PATH: app
    })

    run_simple('0.0.0.0', PORT, application, use_reloader=False, use_debugger=False)
