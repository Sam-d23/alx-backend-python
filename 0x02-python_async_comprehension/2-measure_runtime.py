#!/usr/bin/env python3

import asyncio
import time
from importlib import import_module as using



async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel
    using asyncio.gather and returns total runtime.
    """
    start_time = time.perf_ounter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.perf_counter() - start_time
    return total_runtime

