#!/usr/bin/env python3
"""
This module contains the coroutine async_comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects and returns 10 random numbers."""
    return [i async for i in async_generator()]
