"""Tests for the databricks_dataeng package."""

import pytest
from datetime import datetime

from databricks_dataeng.models.basic import Basic
from databricks_dataeng.utils.basic import basic_config


def test_basic_model():
    """Basic model accepts valid fields."""
    now = datetime.now()
    b = Basic(
        id="id1",
        name="Alice",
        age=30,
        email="a@example.com",
        created_at=now,
        updated_at=now,
    )
    assert b.id == "id1"
    assert b.name == "Alice"
    assert b.age == 30


def test_basic_config_returns_basic():
    """basic_config() returns a Basic instance."""
    now = datetime.now()
    b = basic_config(
        basic_id="id1",
        basic_name="Bob",
        basic_age=25,
        basic_email="b@example.com",
        basic_created_at=now,
        basic_updated_at=now,
    )
    assert isinstance(b, Basic)
    assert b.name == "Bob"
    assert b.age == 25
