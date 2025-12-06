#!/bin/bash

case "$1" in
	r)
		shift
		python3 magma_viz/cli/main.py "$@"
		;;
	t)
		shift
		pytest "$@"
		;;
	*)
		shift
		echo "invalid option: $@"
esac
