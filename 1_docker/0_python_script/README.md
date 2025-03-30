# Build

```bash
docker build -t my_python_script:0.0.1 .
```

# Run

```bash
docker run --name my-python-script my_python_script:0.0.1
```

# Push

Tag

```bash
docker tag my_python_script:0.0.1 lukaskellerstein/my_python_script:0.0.1
```

Push

```bash
docker push lukaskellerstein/my_python_script:0.0.1
```
