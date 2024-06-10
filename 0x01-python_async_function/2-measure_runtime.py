#!/usr/bin/env python3

import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time and
    returns the average.
    """
    start_time = time()
    await wait_n(n, max_delay)
    end_time = time()
    total_time = end_time - start_time
    return total_time/n
