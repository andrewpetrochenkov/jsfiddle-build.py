#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- "${BASH_SOURCE[0]%/*}"/jsfiddle1 # "${BASH_SOURCE[0]%/*}"/jsfiddle2
( set -x; python -m jsfiddle_build "$@" )
