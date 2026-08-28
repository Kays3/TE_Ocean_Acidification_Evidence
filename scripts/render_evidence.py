#!/usr/bin/env python3
"""Render the tab separated evidence register as a GitHub friendly table."""

from pathlib import Path
import csv


ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "evidence" / "claims.tsv"
target = ROOT / "evidence" / "index.md"

with source.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle, delimiter="\t"))

columns = ["id", "topic", "claim", "evidence", "status", "caveat"]
lines = [
    "# Evidence register",
    "",
    "This page is generated from [`claims.tsv`](claims.tsv). Each row separates the claim from the evidence and its limits.",
    "",
    "| ID | Topic | Claim | Evidence | Status | Caveat |",
    "| --- | --- | --- | --- | --- | --- |",
]
for row in rows:
    lines.append("| " + " | ".join(row[column].replace("|", "\\|") for column in columns) + " |")

target.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {target.relative_to(ROOT)} from {source.relative_to(ROOT)}")
