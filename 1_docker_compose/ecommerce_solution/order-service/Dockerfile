FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Compile the proto file (generates order_pb2.py and order_pb2_grpc.py)
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order.proto
EXPOSE 50052
CMD ["python", "server.py"]
