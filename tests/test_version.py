"""Basic test to verify package import and version."""

import pytest

from databricks_dataeng import __version__


def test_version_is_string():
    assert isinstance(__version__, str)
    assert len(__version__) > 0
