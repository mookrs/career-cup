"""给定两个字符串，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。"""


def permutation(s, t):
    if len(s) != len(t):
        return False

    letters = [0] * 256

    for char in s:
        letters[ord(char)] += 1

    for char in t:
        if letters[ord(char)] == 0:
            return False
        letters[ord(char)] -= 1

    return True


print(permutation('god', 'dog'))
print(permutation('goods', 'doogt'))
