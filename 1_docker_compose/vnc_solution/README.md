# Build ALL

Build

```bash
docker compose build --no-cache
```

Run

```bash
docker compose up
```

# Build Proxy (Websocker <> TCP)

Websockify repo: https://github.com/novnc/websockify

**Build**

Build a docker container `./docker/build.sh`. I changed the build script to:

```
#!/usr/bin/env sh
set -e -x
cd "$(dirname "$0")"
(cd .. && python3 setup.py sdist --dist-dir docker/)
docker build -t websockify:0.0.1 .
```

**Tag**

```bash
docker tag websockify:0.0.1 lukaskellerstein/websockify:0.0.1
```

Push

```bash
docker push lukaskellerstein/websockify:0.0.1
```

# Build UI

**Build**

```bash
docker build -t vnc-react-ui:0.0.1 .
```

**Run**

```bash
docker run --name vnc-react-ui -e MY_BASE_URL=/ui -p 3100:80 vnc-react-ui:0.0.1
```

if I will not set the MY_BASE_URL envVar, the default (`/ui`) will be used. The default one is defined in entrypoint.sh

```
BASE_URL="${MY_BASE_URL:-/ui}"
```

**Tag**

```bash
docker tag vnc-react-ui:0.0.1 lukaskellerstein/vnc-react-ui:0.0.1
```

**Push**

```bash
docker push lukaskellerstein/vnc-react-ui:0.0.1
```

# Open

Open UI

http://localhost:3100/ui

Add VMs in the UI

localhost:7100
localhost:7101
