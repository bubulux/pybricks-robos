# .devcontainer/Dockerfile
FROM python:3.12-bookworm

# Bluetooth + DBus + USB tools
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    bluez bluetooth dbus usbutils && \
    rm -rf /var/lib/apt/lists/*

# Pybricks toolchain
RUN pip install --no-cache-dir pybricksdev pybricks-stubs
