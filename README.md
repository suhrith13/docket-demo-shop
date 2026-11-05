# docket-demo-shop

The project itself: [suhrith13/Docket](https://github.com/suhrith13/Docket).


A tiny Python project used to demo **Docket**, a courtroom-style code review in a Switch room.

> **The bugs in this repo are planted on purpose.** `main` is clean and its tests pass.
> The two PR branches each contain deliberate defects so the demo is reproducible:
>
> | Branch | What it adds | Planted defects |
> | --- | --- | --- |
> | `pr-1-order-history` | `order_history()` and `apply_loyalty_discount()` | Pagination skips the first page; loyalty discount has no cap and can go negative |
> | `pr-2-order-search` | `search_orders()` | Repeats PR 1's pagination mistake, so the prosecutor can cite the earlier ruling |

## Run the tests

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Use it for the demo

1. Push this repo to GitHub with all three branches: `git push -u origin --all`
2. Open PR 1: `pr-1-order-history` into `main`.
3. Start a case in the `docket-court` room by tagging `@docket-prosecutor` with the PR number.
4. After the judge rules on PR 1, open PR 2: `pr-2-order-search` into `main`.
