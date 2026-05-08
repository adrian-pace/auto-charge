FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

# Create a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app

# Enable bytecode compilation for slightly faster startup
ENV UV_COMPILE_BYTECODE=1

# Copy from your project to the container
# Copy pyproject.toml and uv.lock first to cache the dependencies layer
COPY pyproject.toml uv.lock* ./
COPY main.py easee_api.py config.py ./

# Give ownership of the copied files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Install the project and its dependencies using uv
# This automatically creates a .venv inside the container
RUN uv sync --no-dev --no-cache

# Ensure the installed binaries are on the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run FastAPI in production mode
# Binds to 0.0.0.0 so the reverse proxy can route traffic to it
CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
