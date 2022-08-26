from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_items(

) -> Any:
    """
    Retrieve items.
    """
    items = {1: 'item-1', 2: 'item-2'}
    return items
