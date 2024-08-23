#!/usr/bin/env python3
"""
This module contains the coroutine async_generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine which will loop 10 times.

    Asynchronously wait 1 second and yield a random number between 0 and 10.
    """
    async def number() -> float:
        """Returns radom number between 0 and 10."""
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    for _ in range(10):
        yield await number()
