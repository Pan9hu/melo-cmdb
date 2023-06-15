#!/usr/bin/env sh

echo "Building gMetrics."
cd mmetrics/
make build

echo "Building mCore."
cd ../mcore
go build .

echo "Copy binary to target dir."

echo "Install gmetrics."
echo "Install mcore."
