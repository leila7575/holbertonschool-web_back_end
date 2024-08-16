#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random
"""
import asyncio
import random


async def wait_random(max_delay = 10):
    """asynchronous coroutine that takes in an integer argument max_delay
    waits for a random delay between 0 and max_delay
    returns the delay 
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
