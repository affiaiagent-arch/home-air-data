"""Annual running cost for a dehumidifier, from published inputs only.

The only published annual-hours figure is 1,095 h/year (US DOE dehumidifier
test procedure, 10 CFR 430 Appendix X1, dehumidification mode). Power draw and
price per kWh are yours to supply — there are no defaults, because a default
would be a guess.

    python dehumidifier_running_cost.py --watts 300 --price 0.17
    -> 55.85 USD/year    (300 W x 1095 h / 1000 x 0.17 $/kWh)

MIT License.
"""
import argparse


def annual_cost(watts: float, hours_per_year: float, price_per_kwh: float) -> float:
    """kWh = watts / 1000 * hours; cost = kWh * price."""
    return watts / 1000.0 * hours_per_year * price_per_kwh


def main() -> None:
    p = argparse.ArgumentParser(description="Annual dehumidifier running cost")
    p.add_argument("--watts", type=float, required=True, help="rated power draw in watts")
    p.add_argument("--hours", type=float, default=1095.0,
                   help="annual hours (default 1095 = US DOE dehumidification mode)")
    p.add_argument("--price", type=float, required=True, help="electricity price, USD per kWh")
    a = p.parse_args()
    print(f"{annual_cost(a.watts, a.hours, a.price):.2f} USD/year")


if __name__ == "__main__":
    main()
