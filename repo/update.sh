#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

echo "============================================="
echo "   Hellokhe iOS 7.x Repository Builder       "
echo "============================================="
python3 scan.py

echo ""
echo "--- Hosted iOS 7 Packages ---"
grep "^Package:" Packages | sed 's/Package: / - /'

echo ""
echo "Repository updated successfully!"
echo "To publish your updates to GitHub Pages:"
echo "  git add ."
echo "  git commit -m 'Update iOS 7 packages'"
echo "  git push origin main"
