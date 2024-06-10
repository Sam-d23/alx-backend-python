#!/usr/bin/env python3
"""AsyncIO
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous co-routine that takes in an argument,
    that waits for a randomn delay and returns it.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
