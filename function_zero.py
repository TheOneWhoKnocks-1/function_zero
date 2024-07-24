from types import GeneratorType


class ListTools:

    @staticmethod
    def check_none(value):
        if value is None:
            raise ValueError("Cannot run the code with no arguments!"
                             " or mayhaps an argument is missing")
        return

    @staticmethod
    def fix_type(value):

        if isinstance(value, list):
            return value

        if isinstance(value, GeneratorType):
            return list(value)

        if isinstance(value, int or float):
            value = str(value)
            return [int(i) for i in value]

        if len(value) < 100:
            if isinstance(value, str):
                return [i for i in value]
            elif isinstance(value, dict):
                return [i for i in value.keys()]
        raise ValueError(f"Could not turn the {value} to a list"
                         f"Please insert iterable objects")

    @staticmethod
    def list_rotator(value=None, num=1):
        ListTools.check_none(value)
        try:
            return value[-num:] + value[:-num]
        except Exception:
            value = ListTools.fix_type(value)
            return value[-num:] + value[:-num]

    @staticmethod
    def least_and_most_repeated(value=None):
        ListTools.check_none(value)
        value = ListTools.fix_type(value)
        least, most = 1, 1
        o1, o2 = "", ""

        for i in value:
            if value.count(i) > most:
                most = value.count(i)
                o1 = i
            if value.count(i) <= least:
                least = value.count(i)
                o2 = i
        return {o1:most, o2:least}

    @staticmethod
    def reversed_value(value=None):
        ListTools.check_none(value)
        value = ListTools.fix_type(value)
        return list(reversed(value))

    @staticmethod
    def binary_search(value=None, obj=None, real_count=False):
        ListTools.check_none(value)
        ListTools.check_none(obj)
        value = ListTools.fix_type(value)
        lo, hi = 0, len(value) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            val = value[mid]

            if val == obj:
                if real_count:
                    return mid + 1
                return mid
            elif val < obj:
                lo = mid + 1
            else:
                hi = mid - 1

        return "not found"

    @staticmethod
    def linear_search(value=None, obj=None, real_count=False):
        ListTools.check_none(value)
        ListTools.check_none(obj)
        value = ListTools.fix_type(value)
        for i in value:
            if i == obj:
                if real_count:
                    return value.index(i) + 1
                return value.index(i)
        return "not found"

    @staticmethod
    def bubble_sort(value=None):
        ListTools.check_none(value)
        if isinstance(value, list or int):
            raise ValueError(f"Bubble sorting is not possible on {value}")
        ListTools.check_none(value)
        value = ListTools.fix_type(value)
        try:
            length = len(value)
            for i in range(length):
                for j in range(0, length - i - 1):
                    if value[j+1] < value[j]:
                        value[j],value[j+1] = value[j+1],value[j]
            return value
        except TypeError:
            raise TypeError("Bubble sort is not possible for multiple kinds of data!")

