#!/usr/bin/env sh

echo "Building gMetrics."
cd gmetrics/
make build

echo "Building mCore."
cd ../mcore
go build .

echo "Copy binaray to target dir."

echo "Install gmetrics."
echo "Install mcore."
