"""Tests for the comm_config package."""

import pytest
from datetime import datetime

from comm_config import Comm, comm_config


def test_comm_model():
    """Comm model accepts valid fields."""
    now = datetime.now()
    c = Comm(
        comm_id="id1",
        comm_name="name1",
        comm_type="type1",
        comm_status="active",
        comm_created_at=now,
        comm_updated_at=now,
    )
    assert c.comm_id == "id1"
    assert c.comm_name == "name1"
    assert c.comm_status == "active"


def test_comm_config_returns_comm():
    """comm_config() returns a Comm instance."""
    now = datetime.now()
    c = comm_config(
        comm_id="id1",
        comm_name="name1",
        comm_type="type1",
        comm_status="active",
        comm_created_at=now,
        comm_updated_at=now,
    )
    assert isinstance(c, Comm)
    assert c.comm_id == "id1"
