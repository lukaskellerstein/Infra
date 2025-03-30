FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy proto files and compile them
COPY product.proto .
COPY order.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. product.proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. order.proto
# Copy the rest of the application code
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
