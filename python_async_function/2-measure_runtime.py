#!/usr/bin/env python3
"""
This module contains the function measure_time            
"""
import asyncio
import time
from 1-concurrent_coroutines import wait_n    


def measure_time(n: int, max_delay: int) -> float:        
    """
    Measures the total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
