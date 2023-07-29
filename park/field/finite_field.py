from __future__ import annotations


class FieldValue:
    def __init__(self, value: int | FieldValue):
        self.__value = value

    def __add__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value + other.__value)
        return FieldValue(self.__value + other)

    def __sub__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value - other.__value)
        return FieldValue(self.__value - other)

    def __mul__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value * other.__value)
        return FieldValue(self.__value * other)

    def __truediv__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value // other.__value)
        return FieldValue(self.__value // other)

    def __mod__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value % other.__value)
        return FieldValue(self.__value % other)

    def __pow__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return FieldValue(self.__value**other.__value)
        return FieldValue(self.__value**other)

    def __eq__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value == other.__value

        return self.__value == other

    def __ne__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value != other.__value

        return self.__value != other

    def __lt__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value < other.__value

        return self.__value < other

    def __le__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value <= other.__value

        return self.__value <= other

    def __gt__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value > other.__value

        return self.__value > other

    def __ge__(self, other: int | FieldValue):
        if isinstance(other, FieldValue):
            return self.__value >= other.__value

        return self.__value >= other

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return f"FieldValue({self.__value})"


class FiniteField:
    pass
