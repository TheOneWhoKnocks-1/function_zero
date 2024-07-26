from types import GeneratorType
from string import ascii_letters
from re import match

class ChangeType:

    @staticmethod
    def turn_to_string(value):

        if isinstance(value, str):
            return value

        if isinstance(value, list):
            return "".join(value)

        if isinstance(value, int or float):
            return str(value)

        if isinstance(value, dict):
            lili = []
            for i, j in value.items():
                x = f"{i} = {j} "
                lili.append(x)
            return "".join(lili)

        if isinstance(value, GeneratorType):
            x = list(value)
            return "".join(map(str,x))

        raise ValueError(f"{value} cannot be converted to string.")

    @staticmethod
    def turn_to_list(value):

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
    def turn_to_int(value):

        try:
            if isinstance(value, str):

                return int(value)

            if isinstance(value, list):
                x = "".join((map(str, value)))
                return int(x)

            if isinstance(value, GeneratorType):
                y = list(value)
                x = "".join((map(str, y)))
                return int(x)

        except Exception:
            raise ValueError(f"{value} cannot turn it's type to int!")

        raise ValueError(f"{value} cannot turn it's type to int!!")

class ListTools:
    """
    Notes: this class has functions that take a list object, if the object is not a list , it
    will change it's type to a list and run the chosen codes. Be aware that not all of the objects
    can change their type to a list! Therefore, every function SHOULD have at least one value given.
    """
    @staticmethod
    def check_none(value):
        if value is None:
            raise ValueError("Cannot run the code with no arguments!"
                             " or mayhaps an argument is missing")
        return

    @staticmethod
    def list_rotator(value=None, num=1):
        ListTools.check_none(value)
        try:
            return value[-num:] + value[:-num]
        except Exception:
            value = ChangeType.turn_to_list(value)
            return value[-num:] + value[:-num]

    @staticmethod
    def least_and_most_repeated(value=None):
        ListTools.check_none(value)
        value = ChangeType.turn_to_list(value)
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
        value = ChangeType.turn_to_list(value)
        return list(reversed(value))

    @staticmethod
    def binary_search(value=None, obj=None, real_count=False):
        ListTools.check_none(value)
        ListTools.check_none(obj)
        value = ChangeType.turn_to_list(value)
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
        value = ChangeType.turn_to_list(value)
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
        value = ChangeType.turn_to_list(value)
        try:
            length = len(value)
            for i in range(length):
                for j in range(0, length - i - 1):
                    if value[j+1] < value[j]:
                        value[j],value[j+1] = value[j+1],value[j]
            return value
        except TypeError:
            raise TypeError("Bubble sort is not possible for multiple kinds of data!")

class CustomCypher:

    @staticmethod
    def CeaserCypher(string=None, key=1, mode="e"):
        ListTools.check_none(string)
        string = ChangeType.turn_to_string(string)
        alpha = ascii_letters

        if mode.lower() == 'e':
            def encrypt(result="", key=key):
                for ch in string:
                    if ch not in alpha:
                        result += ch
                    else:
                        new_key = (alpha.index(ch) + key) % len(alpha)
                        result += alpha[new_key]
                return result
            return encrypt()
        else:
            key2 = key * -1
            return CustomCypher.CeaserCypher(string, key2)

    @staticmethod
    def CC_brute_force(string=None):
        ListTools.check_none(string)
        result = []
        new_word = ""

        if isinstance(string, str) and len(string) < 100:
            for i in range(len(ascii_letters)):
                for j in string:
                    new_word += CustomCypher.CeaserCypher(j, i)

                result.append(new_word)
                new_word = ""

        else:
            raise TypeError("The input was either not string or too long.")
        return result

class RegEx:

    @staticmethod
    def is_email(st):
        ListTools.check_none(st)
        rules = r'^\w+@[a-zA-Z]+\.[a-zA-Z]{3}$'
        st = ChangeType.turn_to_string(st)
        if match(rules, st):
            return True
        return False

    @staticmethod
    def is_phonenum(st):
        ListTools.check_none(st)
        st = ChangeType.turn_to_string(st)
        rules = r"^09[0-9]{9}$"
        if match(rules, st):
            return True
        return False

















