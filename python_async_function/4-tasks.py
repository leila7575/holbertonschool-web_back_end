#!/usr/bin/env python3
"""
This module contains the asynchronous routine wait_n     
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns task_wait_random n times with max_delay
    Returns the list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
