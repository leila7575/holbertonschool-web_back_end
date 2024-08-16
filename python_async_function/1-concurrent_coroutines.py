#!/usr/bin/env python3
"""
This module contains the asynchronous routine wait_n     
"""
import asyncio
from wait_random import wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with max_delay
    Returns the list of delays in ascending order
    """
    coroutine_list = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutine_list)
    return sorted(delays)
