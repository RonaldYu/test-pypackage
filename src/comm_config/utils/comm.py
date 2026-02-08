from ..models.comm import Comm
from datetime import datetime

def comm_config(
    comm_id: str,
    comm_name: str,
    comm_type: str,
    comm_status: str,
    comm_created_at: datetime,
    comm_updated_at: datetime,
) -> Comm:
    try:
        if comm_id is None or comm_name is None or comm_type is None or comm_status is None or comm_created_at is None or comm_updated_at is None:
            raise ValueError("All fields are required")
        else:
            #x
            return Comm(
                comm_id=comm_id,
                comm_name=comm_name,
                comm_type=comm_type,
                comm_status=comm_status,
                comm_created_at=comm_created_at,
                comm_updated_at=comm_updated_at,
            )

    except Exception as e:
        raise
