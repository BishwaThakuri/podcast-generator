#!/bin/bash
set -e

echo "=============="

# Configure git
git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL:-${GITHUB_ACTOR}@users.noreply.github.com}"
git config --global --add safe.directory /github/workspace

# Run feed generator
python /usr/bin/feed.py

# Commit only if changes exist
git add podcast.xml
if git diff --cached --quiet; then
    echo "No changes in podcast.xml, skipping commit."
else
    git commit -m "Update podcast.xml"
    git push
fi

echo "=============="
