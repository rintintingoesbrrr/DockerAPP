# Flask API with CI/CD pipeline using Github Actions
## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns list of available endpoints |
| `/hello` | Returns greeting message |
| `/health` | Returns application health status |

## Running Locally

### Option 1: Direct execution

Install dependencies and run with Gunicorn:

```bash
pip install flask gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 server:app
```

### Option 2: Docker

Build and run the container:

```bash
docker build -t flask-app .
docker run -p 8000:8000 flask-app
```

The service will be available at `http://localhost:8000`.

## Running Tests

Install test dependencies and run pytest:

```bash
pip install flask pytest
pytest -v
```

## CI/CD Workflow

The GitHub Actions pipeline (`.github/workflows/main.yml`) runs automatically on pushes and pull requests to `main` or `master` branches.

### Pipeline Stages

1. **Test**: Sets up Python 3.10, installs dependencies, and runs pytest.
2. **Build and Push**: On successful tests, builds the Docker image and pushes it to GitHub Container Registry at `ghcr.io/<username>/<repository>`.

Pull requests only run tests. Merges to main/master trigger the full build and push.

## Deploying on Minikube

Start Minikube and apply the deployment:

```bash
minikube start
minikube kubectl -- apply -f deployment.yaml
```

Access the service:

```bash
minikube service psl
```

Verify deployment status:

```bash
minikube kubectl -- get pods
minikube kubectl -- get services
```