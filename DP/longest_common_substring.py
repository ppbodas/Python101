def longest_common_substring(s1, s2):
    dp = [len(s2)*[-1] for _ in range(len(s1))]
    out = 0
    max_str = ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            current = longest_common_substring_recur(s1, s2, i, j, dp)
            if current > out:
                out = current
                max_str = s1[i-out + 1: i + 1]

    #print(max_str)
    return out

def longest_common_substring_recur(s1, s2, i, j, dp):
    if i < 0: return 0
    if j < 0: return 0

    if dp[i][j] != -1: return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 1 + longest_common_substring_recur(s1, s2, i - 1, j - 1, dp)
    else:
        dp[i][j] =  0

    return dp[i][j]


def longest_common_subsequence(s1, s2):
    dp = [len(s2) * [-1] for _ in range(len(s1))]

    out =  longest_common_subsequence_recur(s1, s2, len(s1) - 1, len(s2) - 1, dp)
    print (dp)
    return out


def longest_common_subsequence_recur(s1, s2, i, j,dp):
    if i < 0: return 0
    if j < 0: return 0

    if s1[i] == s2[j]:
        dp[i][j] =  1 + longest_common_subsequence_recur(s1, s2, i - 1, j - 1, dp)
    else:
        dp[i][j] = max(longest_common_subsequence_recur(s1, s2, i, j - 1, dp),
                        longest_common_subsequence_recur(s1, s2, i - 1, j, dp))

    return dp[i][j]


if __name__ == "__main__":
    # substring tests (contiguous)
    assert longest_common_substring("abcdef", "zcdemf") == 3   # "cde"
    assert longest_common_substring("abcd", "abcd") == 4       # "abcd"
    assert longest_common_substring("abc", "xyz") == 0         # no match
    assert longest_common_substring("", "abc") == 0            # empty input
    assert longest_common_substring("abc", "") == 0            # empty input
    assert longest_common_substring("abcdef", "cdef") == 4     # "cdef"
    print("All substring tests passed")

    # subsequence tests (non-contiguous)
    assert longest_common_subsequence("abcdef", "ace") == 3    # "ace"
    assert longest_common_subsequence("abcd", "abcd") == 4     # "abcd"
    assert longest_common_subsequence("abc", "xyz") == 0       # no match
    assert longest_common_subsequence("", "abc") == 0          # empty input
    assert longest_common_subsequence("abc", "") == 0          # empty input
    assert longest_common_subsequence("abcde", "ace") == 3     # "ace"
    print("All subsequence tests passed")
