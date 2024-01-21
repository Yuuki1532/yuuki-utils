import sys, asyncio, time
import functools

async def async_wrapper(func, *args, **kwargs):
    """
    Wrapper to generate async coroutine for sequential functions.
    This runs `func` in another thread/process from the current event loop.
    `func`: sequential callable which is NOT be defined as async function
    """
    func = functools.partial(func, *args, **kwargs)
    return await asyncio.get_event_loop().run_in_executor(None, func)

