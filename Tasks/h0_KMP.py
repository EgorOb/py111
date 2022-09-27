from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    print(prefix_str)
    v = [0] * len(prefix_str)
    for i in range(1, len(prefix_str)):
        k = v[i - 1]
        while k > 0 and prefix_str[k] != prefix_str[i]:
            k = v[k - 1]
        if prefix_str[k] == prefix_str[i]:
            k = k + 1
        v[i] = k
    return v


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    answer = []
    pref = _prefix_fun(substr + '#' + inp_string)
    l_input = len(inp_string)
    l_sub = len(substr)
    for i in range(l_input):
        if pref[l_sub + i + 1] == l_sub:
            answer.append(i + 1 - l_sub)
    print(inp_string, substr, pref)

    if answer:
        return answer[0]
    return None

# def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
#     """
#     Implementation of Knuth-Morrison-Pratt algorithm
#
#     :param inp_string: String where substr is to be found (haystack)
#     :param substr: substr to be found in inp_string (needle)
#     :return: index where first occurrence of substr in inp_string started or None if not found
#     """
#
#     index = None
#     f = _prefix_fun(substr)
#     k = 0
#     for i in range(len(inp_string)):
#         while k > 0 and substr[k] != inp_string[i]:
#             k = f[k - 1]
#         if substr[k] == inp_string[i]:
#             k = k + 1
#         if k == len(substr):
#             index = i - len(substr) + 1
#             break
#
#     print(inp_string, substr, _prefix_fun)
#     return index


if __name__ == "__main__":
    # print(_prefix_fun("abcdabcabcdabcdab"))
    print(kmp_algo(inp_string='abcabcdabcdabdcdab', substr='abcdabd'))
