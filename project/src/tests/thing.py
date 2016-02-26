def weight(val):
    def decorator(func):
        func.__weight__ = val
        return func
    return decorator


@weight(3)
def test1():
    return 1

print test1()
print test1.__weight__
