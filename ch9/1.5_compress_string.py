"""利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。如果压缩后的字符串没有变短，则返回原先的字符串。"""


def compress(s):
    size = count_compression(s)
    if size >= len(s):
        return s

    str_list = []
    last = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            str_list.append(last)
            str_list.append(str(count))
            last = s[i]
            count = 1

    str_list.append(last)
    str_list.append(str(count))
    return ''.join(str_list)


def count_compression(s):
    if not s:
        return 0
    last = s[0]
    size = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] == last:
            count += 1
        else:
            last = s[i]
            size = size + 1 + len(str(count))
            count = 1

    size = size + 1 + len(str(count))
    return size


print(compress('aabcccccaaa'))
print(compress('aabcaa'))
