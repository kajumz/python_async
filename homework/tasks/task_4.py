async def task_1(i: int, res):
    res.append(1)
    if i == 0:
        return
    if i > 5:
        await task_2(i // 2, res)
    else:
        await task_2(i - 1, res)


async def task_2(i: int, res):
    res.append(2)
    if i == 0:
        return
    if i % 2 == 0:
        await task_1(i // 2, res)
    else:
        await task_2(i - 1, res)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    res = []
    await task_1(i, res)
    return int("".join(map(str, res)))
