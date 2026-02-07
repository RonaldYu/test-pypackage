"""Pytest configuration: ensure report output directories exist."""

import os


def pytest_configure(config):
    """Create testing_reports/testing and testing_reports/coverage if missing."""
    # Project root = parent of tests/
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
