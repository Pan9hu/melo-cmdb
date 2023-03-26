#!/usr/bin/env zsh

# shellcheck disable=SC2034
GO_FLAGS="-tags=libipmctl,netgo,libpfm"
make clean
make build