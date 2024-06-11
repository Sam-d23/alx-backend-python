#!/usr/bin/env python3

import asyncio
from importlib import import_module as using


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from the
    imported file, and returns them.
    """
    return [num async for num in async_generator()]
