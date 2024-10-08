#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer max_delay
    waits for a random delay between 0 and max_delay
    returns the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
