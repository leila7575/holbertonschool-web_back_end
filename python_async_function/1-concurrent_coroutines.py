#!/usr/bin/env python3
"""
This module contains the asynchronous routine wait_n
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with max_delay
    Returns the list of delays in ascending order
    """
    coroutine_list = [wait_random(max_delay) for i in range(n)]
    completed_delays = [await o for o in asyncio.as_completed(coroutine_list)]
    return completed_delays
