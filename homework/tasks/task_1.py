from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        # YOUR CODE GOES HERE
        res = await f()
        return res
    elif isinstance(f, Task):
        res = await f
        return res
        # YOUR CODE GOES HERE
    elif isinstance(f, Coroutine):
        res = await f
        return res
        # YOUR CODE GOES HERE
    else:
        raise ValueError('invalid argument')
