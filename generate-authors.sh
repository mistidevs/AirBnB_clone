#!/usr/bin/env bash

set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set -x

# see also ".mailmap" for how email addresses and names are deduplicated
cat > "AUTHORS" <<- EOF
	# File @generated by generate-authors.sh. DO NOT EDIT.
	# This file lists all contributors to the repository.
	# See generate-authors.sh to make modifications.

	$(git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
