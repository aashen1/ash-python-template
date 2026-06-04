# ── Stage 1: Build wheel ──────────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY src/ src/

RUN pip install --no-cache-dir build && \
    python -m build

# ── Stage 2: Runtime ─────────────────────────────────────────────────
FROM python:3.12-slim AS runner

WORKDIR /app

COPY --from=builder /app/dist/*.whl /tmp/

RUN pip install --no-cache-dir /tmp/*.whl && \
    rm -rf /tmp/*.whl

CMD ["python", "-m", "change_to_your_name"]
