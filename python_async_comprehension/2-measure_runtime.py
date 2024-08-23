#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel
    and measures total runtime."""
    start = time.perf_counter()
    coroutines: List[asyncio.Task] = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
