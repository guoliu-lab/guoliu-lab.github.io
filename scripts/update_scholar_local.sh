#!/bin/zsh
# Daily Google Scholar stats refresh, run by launchd
# (~/Library/LaunchAgents/com.wel.scholar-update.plist).
set -e
cd "${0:A:h}/.."

echo "[$(date '+%Y-%m-%d %H:%M:%S')] fetching scholar stats"
/usr/bin/python3 scripts/fetch_scholar.py

if git diff --quiet data/scholar.json; then
  echo "no change"
  exit 0
fi

git add data/scholar.json
git commit -m "Update Google Scholar stats"
git push
echo "pushed updated stats"
