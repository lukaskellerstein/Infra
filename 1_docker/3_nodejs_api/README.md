# Run

```bash
npm start
```

or

```bash
node index.js
```

# Docker

Build

```bash
docker build -t my_nodejs_api_1 .
```

Run

```bash
docker run --name my-nodejs-api-1 -p 8000:8000 my_nodejs_api_1
```

# Test

via curl

```bash
curl http://localhost:8000/
```

```bash
curl http://localhost:8000/status
```

```bash
curl -X POST http://localhost:8000/echo -H "Content-Type: application/json" -d '{"message":"Hello from curl!"}'
```
