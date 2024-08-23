#!/usr/bin/env python3
"""
This module contains the coroutine async_generator.
"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Coroutine which will loop 10 times.

    Asynchronously wait 1 second and yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
