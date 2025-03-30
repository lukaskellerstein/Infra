FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Compile the proto file (generates product_pb2.py and product_pb2_grpc.py)
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. product.proto
EXPOSE 50051
CMD ["python", "server.py"]
