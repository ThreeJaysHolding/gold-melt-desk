# What was created — description, then the actual files

Date: 2026-09-30
Branch: main
This file is the honest split. Other AIs should read this before critiquing.

## Description of what was created

A human-in-the-loop gold-scrap bid desk, not a vision app.

- Frozen method (champion v1): only use listed grams and karat. Photos may cut or kill a lot. Photos may not invent grams.
- Melt formulas in a spreadsheet (gold_desk.xlsx on the operator's Google Drive) and in desk/melt.py and desk/desk.html.
- Lot book, kill flags, house tiers (LiveAuctioneers + Heritage), physical loop (receive in Woodland Hills, weigh, ship to a mail-in refiner).
- One public scan on 2026-09-24. Most scrap lots had no usable weight and were skipped. Two lots with printed grams were scored as conditional buys. None were purchased.
- A Friday 9:00am PT scan automation was scheduled in the operator's Grok account. That automation is not in this repo.
- Operator still must open LiveAuctioneers, a refiner account, and click bids. That has not been done.

## What was asked that was not created

- An app that estimates actual gold grams from auction photos.
- Training and retesting on past auction datasets with known post-smelt weights. Those labels do not exist in public data, and none were collected.
- A self-modifying brain that rewrites its own method. Method changes are written down as challengers. Nothing has been promoted.
- A living. Zero lots bought. Zero assays. Poised profit is $0 until a lot is won and settled.
- $100,000 a year at 10 hours a week. That was a target. It is not a result.

## What you will find in this repo

| Path | What it actually is |
|---|---|
| WHAT_YOU_ASKED.md | Operator's words, quoted |
| WHAT_WAS_CREATED.md | This file |
| EXPORT_FOR_REVIEW.md | Full review packet: business, formulas, money bands, embedded calculator |
| desk/START_HERE.md | Operating definition |
| desk/METHOD_CARDS.md | Champion rules |
| desk/desk.html | Phone calculator. Hardcoded spot from 2026-09-24. Does not scrape or bid. |
| desk/melt.py | Same math in Python |
| desk/scan_watchlist.md | 2026-09-24 scan |

The spreadsheet with live Excel formulas is on the operator's Google Drive, not in this repo (binary). The formulas are copied in EXPORT_FOR_REVIEW.md.
