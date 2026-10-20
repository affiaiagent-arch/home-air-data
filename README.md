# Home Air Data

A small, source-linked dataset for home air treatment — dehumidifiers, humidifiers and air purifiers.

Every value here is copied from a published document (US DOE test procedure, the ENERGY STAR sizing table, or manufacturer support/manual guidance), and the source is named in the data itself. Nothing is estimated. Where a document does not publish a number, the dataset does not contain one.

Maintained by [Goods Review Lab](https://goodsreviewlab.com), an independent research site that reads what owners report and compares it with what the manufacturer publishes.

## Files

| File | What it is |
|---|---|
| `dehumidifier_capacity.csv` | The published sizing cells: pints of water per day by dampness band, at the rating condition (65 °F, 60% RH). |
| `temperature_window.csv` | The operating window a portable dehumidifier is sold for, and the temperature its capacity label is measured at. |
| `air_purifier_filter_hours.csv` | One 2,000-hour filter counter, converted to calendar days at four duty cycles. |
| `dehumidifier_running_cost.py` | Annual running cost from power draw, annual hours and a price per kWh. No defaults — you supply the inputs. |

## Sources

- **US DOE dehumidifier test procedure**, 10 CFR 430 Appendix X1 — rating ambient 65 °F dry-bulb / 60% RH; annual dehumidification hours 1,095.
- **ENERGY STAR dehumidifier sizing table** — pints per day by floor area and dampness.
- **Published manufacturer support and manual guidance** — operating window 41–96 °F; best performance above 65 °F; 2,000-hour filter counters.

## A note on what is *not* here

No document we read publishes an output-loss curve per degree below 65 °F. That number is therefore absent, not zero. If you need it, the honest answer is "not published".

## License

Data: CC0 1.0 (public domain). Code: MIT. Use it, cite it, no permission needed.
