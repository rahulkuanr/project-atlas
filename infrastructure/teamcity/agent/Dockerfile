FROM jetbrains/teamcity-agent

USER root

ARG NODE_VERSION=24.20.0
ARG UV_VERSION=0.11.31
ARG TARGETARCH

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates xz-utils \
    && rm -rf /var/lib/apt/lists/*

RUN case "${TARGETARCH}" in \
      arm64) NODE_ARCH="arm64" ;; \
      amd64) NODE_ARCH="x64" ;; \
      *) echo "Unsupported architecture: ${TARGETARCH}" && exit 1 ;; \
    esac \
    && curl -fsSL "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.xz" \
       -o /tmp/node.tar.xz \
    && mkdir -p /usr/local/lib/nodejs \
    && tar -xJf /tmp/node.tar.xz -C /usr/local/lib/nodejs \
    && ln -s "/usr/local/lib/nodejs/node-v${NODE_VERSION}-linux-${NODE_ARCH}/bin/node" /usr/local/bin/node \
    && ln -s "/usr/local/lib/nodejs/node-v${NODE_VERSION}-linux-${NODE_ARCH}/bin/npm" /usr/local/bin/npm \
    && ln -s "/usr/local/lib/nodejs/node-v${NODE_VERSION}-linux-${NODE_ARCH}/bin/npx" /usr/local/bin/npx \
    && rm /tmp/node.tar.xz

RUN curl -LsSf https://astral.sh/uv/${UV_VERSION}/install.sh \
    | env UV_UNMANAGED_INSTALL=/usr/local/bin UV_NO_MODIFY_PATH=1 sh
    
USER buildagent

RUN uv python install 3.13
