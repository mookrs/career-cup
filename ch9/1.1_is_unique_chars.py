"""确定一个字符串的所有字符是否全都不同，假定字符集为 ASCII。"""


def is_unique_chars(s):
    if len(s) > 256:
        return False

    char_set = [False] * 256
    for char in s:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


def is_unique_chars2(s):
    """假定字符串只含有小写字母 a 到 z"""
    if len(s) > 256:
        return False

    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)

    return True


print(is_unique_chars('abcdefag'))
print(is_unique_chars('abcdefg'))
print(is_unique_chars2('abcdefag'))
print(is_unique_chars2('abcdefg'))
