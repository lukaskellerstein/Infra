Build

```bash
docker build -t nginx2 .
```

Run

```bash
docker run --name nginx2-container -e MY_BASE_URL=/aaa -p 9002:80 nginx2
```

if I will not set the MY_BASE_URL envVar, the default (`/ui`) will be used. The default one is defined in entrypoint.sh

```
BASE_URL="${MY_BASE_URL:-/ui}"
```
