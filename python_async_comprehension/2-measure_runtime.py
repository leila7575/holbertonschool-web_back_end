#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Executes async_comprehension four times in parallel
    and measures total runtime."""
    start = time.perf_counter()
    coroutines = [async_comprehension(i) for i in range(4)]
    results = await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
