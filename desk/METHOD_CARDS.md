# METHOD CARDS — Champion v1 (frozen until beaten)

Status: CHAMPION
Frozen: 2026-09-24
Promotion rule: a challenger must beat this card on median % error AND worst-tail error across closed melts, with n >= 10 in-class.

## Card C1 — Melt from listing (primary)

Allowed: listed gross weight, listed karat, visible stamps only to confirm or downgrade, named coin catalog spec, house wording, spot.

Forbidden: inferring grams from pixels, raising grams above the listing, forum gram claims, treating the estimate as value.

```
fine_g     = gross_g * (karat / 24) * (1 - dead_frac) * c
spot_g     = spot_oz / 31.1034768
gross_melt = fine_g * spot_g
net_payout = gross_melt * refiner_acct - ship_out
landed     = hammer * (1 + premium) + ship_in
edge       = net_payout - landed
max_hammer = (net_payout - ship_in - buffer) / (1 + premium)
```

Defaults: premium 0.25, ship_in 25, ship_out 25, refiner_acct 0.95, buffer 25.
Construction c: solid 0.97, mixed scrap 0.88, hollow 0.75, clasp-only stamp 0.80, filled/plated 0.00.
BUY if edge/landed >= 0.12. WATCH 0.05 to 0.12. Else SKIP.

Kill: gold-filled, no weight, mixed karat with no split, stamp vs test off by more than one karat.

## Card C2 — Photo audit

Photos may confirm, cut c, raise dead weight, or kill. They never write a new gram number.

## Card C3 — Houses

Tier A: Heritage; LiveAuctioneers houses with a metal-fineness warranty.
Tier B: named estate houses with listed tested weight and stamp photos.
Tier C: daily liquidation rope-chain sellers; Invaluable-only houses.

## Card C4 — Learning

After n >= 5 settled lots in a class, move c by 0.02. No silent rewrite. Nothing has been updated. No settled lots exist.

## Card C5 — Small lots

Same dollars tied up. Small lots work only if batched, weight is listed, piece is plain, and edge after premium is still at least 12%.
