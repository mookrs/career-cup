"""将字符串中的空格全部替换为 `%20`。"""


def replace_spaces(s):
    space_count = 0
    for char in s:
        if char == ' ':
            space_count += 1

    new_len = len(s) + space_count * 2
    new_s = [None] * new_len
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            new_s[new_len - 1] = '0'
            new_s[new_len - 2] = '2'
            new_s[new_len - 3] = '%'
            new_len -= 3
        else:
            new_s[new_len - 1] = s[i]
            new_len -= 1

    return ''.join(new_s)


s = 'I feel good'
print(replace_spaces(s))
