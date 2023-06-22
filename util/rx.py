from typing import TypeVar


T = TypeVar('T')


def log(observable: T):
    print(observable)
    return observable
