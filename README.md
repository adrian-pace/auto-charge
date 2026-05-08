# ⚡ Auto Charge

A lightweight, programmatic FastAPI interface to control your Easee EV charger. Built for automation, this service acts as a bridge to the official Easee Developer API, allowing you to easily trigger charging sessions via simple internal HTTP requests.

---

## 🚀 Quickstart

### Option A: Run with Docker (Production Ready)
1. **Configure Secrets**: Ensure your server's secret directory is set up with your Easee credentials at `../secrets/auto-charge.env`:
   ```env
   EASEE_EMAIL=your_email@example.com
   EASEE_PASSWORD=your_secure_password
   EASEE_CHARGER_ID=your_charger_id
   ```
2. **Start the Service**:
   ```bash
   docker compose up -d
   ```
   *Note: The container runs securely behind the `caddy_net` internal network without exposing ports to the host.*

### Option B: Local Development
1. **Clone & Configure**:
   ```bash
   git clone <your-repository-url>
   cd auto-charge
   echo -e "EASEE_EMAIL=your_email\nEASEE_PASSWORD=your_pass\nEASEE_CHARGER_ID=your_charger_id" > .env
   ```
2. **Run the Server**:
   Using `uv` (a fast Python package manager):
   ```bash
   uv run fastapi dev
   ```
3. **Verify the API login script**:
   ```bash
   uv run test_login.py
   ```

---

## 📡 API Endpoints

Once running locally (`http://localhost:8000`), the following simple endpoints are exposed:

- **Start Charging**: `GET /start-charge/`
- **Stop Charging**: `GET /stop-charge/`

Each endpoint automatically handles authentication, fetches a fresh token, and sends the corresponding command to your specific Easee charger ID.

*Interactive Documentation (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)*

---

## 🏗️ Architecture

- **`main.py`**: FastAPI routing and web server configuration.
- **`easee_api.py`**: Core asynchronous SDK to communicate with the Easee Developer API.
- **`config.py`**: Strongly typed environment variable validation using `pydantic-settings`.
- **`Dockerfile`**: A highly-optimized, multi-arch compatible container using the official Astral `uv` slim image, configured to run as a secure non-root `appuser`.

## 📦 Building the Docker Image

To build the image manually for both AMD64 and ARM64 architectures (including SLSA provenance and SBOMs):

```bash
# 1. Create a buildx builder instance (one-time setup)
docker buildx create --use --name production-builder

# 2. Build and push to Docker Hub
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --provenance=true \
  --sbom=true \
  --push \
  -t <your-dockerhub-username>/auto-charge:latest \
  .
```
