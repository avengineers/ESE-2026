FROM mcr.microsoft.com/devcontainers/javascript-node:5-24-bookworm

# Corporate CA (proxy). initializeCommand in devcontainer.json copies the host
# certificates into certs/ before the build.
COPY certs/ /usr/local/share/ca-certificates/
RUN update-ca-certificates

# uv runs the Python scripts in scripts/ (make_qr.py, make_docx.py).
COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /uvx /usr/local/bin/

ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_DIR=/etc/ssl/certs
ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV PIP_CERT=/etc/ssl/certs/ca-certificates.crt
