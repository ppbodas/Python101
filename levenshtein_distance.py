def l_distance(s1, s2):
    dp = [len(s2)*[-1] for i in range(len(s1))]   # Creates m rows n columns
    out = l_distance_recur(s1, s2, len(s1)-1, len(s2)-1, dp)
    print(f"distance is {out}")
    return out


def l_distance_recur(s1, s2, i, j, dp):
    if i < 0: return j + 1
    if j < 0: return i + 1

    if dp[i][j] != -1: return dp[i][j]

    out = -1

    if s1[i] == s2[j] :
        out = l_distance_recur(s1, s2, i-1, j-1, dp)
    else:
        out = 1 + min(l_distance_recur(s1, s2, i-1, j, dp), l_distance_recur(s1, s2, i, j-1, dp),  l_distance_recur(s1, s2, i-1, j-1, dp))

    dp[i][j] = out
    return out






if __name__ == "__main__":
    assert l_distance("kitten", "sitting") == 3
    assert l_distance("sunday", "saturday") == 3
    assert l_distance("", "abc") == 3
    assert l_distance("abc", "abc") == 0
    assert l_distance("abc", "") == 3
    print("All tests passed")
