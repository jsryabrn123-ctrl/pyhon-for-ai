# Python for AI

Small Python examples for working with data and plotting.

## Requirements

- Python 3.10 or newer
- Packages listed in `requirements.txt`

Install the dependencies in a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Examples

Run these commands from the repository root:

```powershell
python hello.py
python interactive_demo.py
```

`hello.py` prints the current working directory. `interactive_demo.py` plots
sample Paris temperature data, saves `weather_chart.png`, and displays the
chart.

The `sales-analysis` example reads its sample sales data and generates JSON,
Excel, and CSV results in `sales-analysis/output`:

```powershell
Set-Location .\sales-analysis
python analyzer.py
```

The `.venv` and any other local virtual environments are intentionally excluded
from Git; install dependencies from `requirements.txt` instead.
