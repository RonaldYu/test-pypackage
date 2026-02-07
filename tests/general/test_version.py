"""Project-level test: package is installable and has a version."""

import pytest
from importlib.metadata import PackageNotFoundError, version


def test_package_version():
    """When installed (e.g. pip install -e .), package has a non-empty version."""
    try:
        v = version("databricks-engtoolkits")
    except PackageNotFoundError:
        pytest.skip("Package not installed (run: pip install -e .)")
    assert isinstance(v, str)
    assert len(v) > 0
