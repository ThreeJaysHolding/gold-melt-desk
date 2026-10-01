#!/usr/bin/env python3
"""Gold melt desk calculator. Deterministic. No model in the formula."""
from dataclasses import dataclass

TROY_G = 31.1034768
KARAT = {"10K": 10/24, "14K": 14/24, "18K": 18/24, "22K": 22/24, "24K": 1.0, "999": 0.999, "900": 0.900}

@dataclass
class Quote:
    gross_g: float
    karat: str
    spot_oz: float
    dead_frac: float = 0.0
    c: float = 0.97
    premium: float = 0.25
    ship_in: float = 25.0
    ship_out: float = 25.0
    refiner_acct: float = 0.95
    buffer: float = 25.0
    hammer: float = 0.0

    def fine_g(self) -> float:
        return self.gross_g * KARAT[self.karat] * (1 - self.dead_frac) * self.c

    def spot_g(self) -> float:
        return self.spot_oz / TROY_G

    def gross_melt(self) -> float:
        return self.fine_g() * self.spot_g()

    def net_payout(self) -> float:
        return self.gross_melt() * self.refiner_acct - self.ship_out

    def landed(self) -> float:
        return self.hammer * (1 + self.premium) + self.ship_in

    def max_hammer(self) -> float:
        return max(0.0, (self.net_payout() - self.ship_in - self.buffer) / (1 + self.premium))

    def edge(self) -> float:
        return self.net_payout() - self.landed()

    def report(self) -> str:
        lines = [
            f"gross_g={self.gross_g}  karat={self.karat}  c={self.c}  dead={self.dead_frac}",
            f"fine_g={self.fine_g():.3f}  spot_g=${self.spot_g():.2f}  gross_melt=${self.gross_melt():.2f}",
            f"net_payout=${self.net_payout():.2f}  max_hammer=${self.max_hammer():.2f}",
        ]
        if self.hammer:
            e = self.edge()
            pct = e / self.landed() if self.landed() else 0
            lines.append(f"hammer=${self.hammer:.2f}  landed=${self.landed():.2f}  edge=${e:.2f} ({pct:.1%})")
        return "\n".join(lines)

if __name__ == "__main__":
    q = Quote(gross_g=20, karat="14K", spot_oz=4280.69, hammer=800)
    print(q.report())
