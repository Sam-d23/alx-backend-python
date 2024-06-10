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
    delay = await asyncio.gather(
            *tuple(map(lamda _: wait_random(max_delay), range(n))))
    return sorted(delay)
