# databricks-dataeng

Databricks data engineering Python package.

## Installation

From source (development):

```bash
pip install -e ".[dev]"
```

Build a wheel:

```bash
pip install build
python -m build
```

Wheels and source distribution will be in `dist/`.

## Running tests

Install dev dependencies (if not already):

```bash
pip install -e ".[dev]"
```

Run all tests:

```bash
pytest
```

Or run with a path:

```bash
pytest tests/ -v
```

Reports are written to:

- **JUnit XML** and **pytest HTML**: `testing_reports/results/` (`report.xml`, `report.html`)
- **Coverage** (HTML + XML): `testing_reports/coverage/` (`index.html`, `coverage.xml`)

## Development

- Source code: `src/comm_config/`, `src/databricks_dataeng/`
- Tests: `tests/`


## Install package
- pip install dist/databricks_engtoolkits-{version}-py3-none-any.whl
- pip install dist/databricks-engtoolkits-{version}.tar.gz