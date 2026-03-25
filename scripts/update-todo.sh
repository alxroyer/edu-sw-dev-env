#!/usr/bin/env bash

SCRIPTS_DIR="$(dirname "${BASH_SOURCE}")"
REPO_DIR="${SCRIPTS_DIR}/.."

pushd "${REPO_DIR}" > /dev/null
    head -n $(grep -n "# TODOs" TODO.md | tail -n 1 | sed -e "s/:.*//") TODO.md > TODO.md.tmp
    echo "" >> TODO.md.tmp
    grep -Irn TODO *.md | grep -v "^TODO\.md:" | sed -e "s/^\(.*\)$/- \1/" >> TODO.md.tmp
    mv TODO.md.tmp TODO.md
popd > /dev/null
