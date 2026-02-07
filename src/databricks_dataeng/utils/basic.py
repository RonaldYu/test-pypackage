from datetime import datetime

from ..models.basic import Basic


def basic_config(
    basic_id: str,
    basic_name: str,
    basic_age: int,
    basic_email: str,
    basic_created_at: datetime,
    basic_updated_at: datetime,
) -> Basic:

    return Basic(
        id=basic_id,
        name=basic_name,
        age=basic_age,
        email=basic_email,
        created_at=basic_created_at,
        updated_at=basic_updated_at,
    )


