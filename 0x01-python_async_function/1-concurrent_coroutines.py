#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax.py').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random
    n times and returns the delay of each spawn
    in ascending order.
    """
    return sorted(await asyncio.gather(*(wait_random(max_delay) for _ in range(n))))
