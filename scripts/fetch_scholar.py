#!/usr/bin/env python3
"""Fetch Google Scholar stats and write data/scholar.json.

Run by .github/workflows/update-scholar.yml on a daily schedule.
Fails loudly (non-zero exit) so the workflow skips the commit and the
site keeps serving the previous numbers.
"""
import json
import sys
from datetime import date, timezone
from pathlib import Path

from scholarly import scholarly

SCHOLAR_ID = "RxDTLEYAAAAJ"
OUT = Path(__file__).resolve().parent.parent / "data" / "scholar.json"


def main() -> None:
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

    citations = author.get("citedby")
    hindex = author.get("hindex")
    publications = len(author.get("publications", []))
    if not citations or not hindex or not publications:
        sys.exit("scholar returned incomplete data; keeping previous JSON")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "citations": citations,
                "hindex": hindex,
                "i10index": author.get("i10index"),
                "publications": publications,
                "updated": date.today().isoformat(),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT}: {citations} citations, h-index {hindex}, {publications} publications")


if __name__ == "__main__":
    main()
