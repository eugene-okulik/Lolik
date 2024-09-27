# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция


def repeat_me(func):
    def wrapper(*args, count):
        for _ in range(count):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=5)

# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет обработать
# такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)
#
#
# example('print me')
