# ── Stage 1: Build ──────────────────────────────────────────────────
FROM ghcr.io/prefix-dev/pixi:0.70.1 AS build

WORKDIR /app

# Copy pixi config first for Docker layer caching
COPY pixi.toml pixi.lock ./

# Copy project files needed for build
COPY pyproject.toml README.md LICENSE ./
COPY src/ src/

# Install production environment (--locked ensures lockfile consistency)
RUN pixi install --locked -e prod

# Generate shell-hook script to activate the environment
RUN pixi shell-hook -e prod -s bash > /shell-hook
RUN echo "#!/bin/bash" > /app/entrypoint.sh
RUN cat /shell-hook >> /app/entrypoint.sh
RUN echo 'exec "$@"' >> /app/entrypoint.sh

# ── Stage 2: Production ─────────────────────────────────────────────
FROM ubuntu:24.04 AS production

# Install runtime system libraries (SSL, compression, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates libexpat1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Only copy the production environment (path must match build stage)
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build --chmod=0755 /app/entrypoint.sh /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD [ "python", "-m", "change_to_your_name" ]
