import sys


class Jar:
    def __init__(self, capacity=12, size=0):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
            if isinstance(size, int) and 0 <= size <= capacity:
                self._size = size
        else:
            raise ValueError("Pease enter an integer!")


    def __str__(self) -> str:
        if self.size == 0:
            return f"No cookies in the jar!"
        return "🍪" * self.size


    def deposit(self, n):
        if n.isdigit():
            n = int(n)
            if (self.size + n) > self.capacity:
                raise ValueError("Entered amount exceeds jar capacity!")
            else:
                self._size += n
        else:
            raise ValueError("Please enter an integer!")


    def withdraw(self, n):
        if n.isdigit():
            n = int(n)
            if n > self._size:
                raise ValueError("Insufficient cookies in jar!")
            else:
                self._size -= n
        else:
            raise ValueError("Please enter an integer!")


    @property
    def capacity(self) -> int:
        return self._capacity


    @property
    def size(self) -> int:
        return self._size
