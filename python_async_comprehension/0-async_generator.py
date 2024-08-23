#!/usr/bin/env python3
"""
This module contains the coroutine async_generator
"""
import asyncio
import random


async def async_generator():
    """Coroutine which will loop 10 times.

    Asynchronously wait 1 second and yield a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
