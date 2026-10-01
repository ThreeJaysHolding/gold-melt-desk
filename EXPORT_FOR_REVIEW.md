# GOLD MELT DESK — EXPORT FOR EXTERNAL REVIEW

Date: 2026-09-30. Public repo: https://github.com/ThreeJaysHolding/gold-melt-desk

Instruction to reviewing AIs: do not assume a computer-vision weight-from-photos product exists. It does not.

## One sentence

A human-in-the-loop bid desk. It reads auction listings that already print weight and karat, computes a max hammer, and the human bids and ships to a refiner. It does not look at a photo and know the grams.

## How money would be made

1. Find a lot with printed grams and a single karat, or a named coin with catalog weight.
2. Compute expected refiner payout, not the auction estimate.
3. Bid only if landed cost (hammer + buyer premium + inbound ship) is under payout minus a buffer, with at least 12% net edge.
4. Win, receive in Woodland Hills, weigh, batch, insured ship to a mail-in refiner.
5. Profit = payout minus landed minus outbound ship minus tax.

No LiveAuctioneers account, no refiner contract, no scale confirmed, zero lots purchased, zero assays. Any dollar figure is a model.

## Formulas

```
fine_g     = gross_g * (karat / 24) * (1 - dead_frac) * c
spot_g     = spot_oz / 31.1034768
gross_melt = fine_g * spot_g
net_payout = gross_melt * 0.95 - 25
landed     = hammer * (1 + premium) + 25
max_hammer = (net_payout - 25 - 25) / (1 + premium)
```

Spot used on 2026-09-24: $4,280.69/oz. Worked example: 20 g plain 14K, c 0.97, hammer $800, premium 25% → fine 11.32 g, max hammer about $1,124, edge about 42% if the listing weight is true.

## 2026-09-24 scan (not purchased)

- Golden Sun 14K Byzantine 13 g at $275: max hammer $535 if treated as hollow.
- John Moran 14K figaro 46.3 g at $1,800: max hammer $2,538 at 32% premium if solid, about $1,930 if hollow.
- Mixed-karat, gold-filled, and no-weight bags: skipped.

## How much the operator is poised to make

$0 until a lot is won and settled.

| Case | Requirement | Annual net, model only |
|---|---|---|
| Current | No accounts | $0 |
| Sparse | 2 wins/month, $200 net | about $5k |
| Working desk | 8 wins/month, $300 net, batched | about $29k |
| $100k/year | about $8.3k net/month | Not shown by one scan. Needs capital and a repeat supply of mispriced weighed lots. |

## The app

See desk/desk.html and desk/melt.py. The HTML page takes grams, karat, construction factor, dead fraction, premium, and current hammer. It prints fine grams, melt, net, max hammer, and BUY/WATCH/SKIP. It does not scrape auctions or bid.
