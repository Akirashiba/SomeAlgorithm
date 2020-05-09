class LongestSubString:

    @staticmethod
    def longest_without_repeating_character(test_str: str) -> int:
        # Target: 获取最长不相同字符子串长度
        # 空间复杂度O(n) 时间复杂度O(n)
        # 算法思想: 游标一直往后推 记录当前从start开始所有字符的下标
        # 当遇到重复的字符 start = 重复字符下标 + 1
        start, maxLength = 0, 0
        usedChar = {}
        for index, char in enumerate(test_str):
            if char in usedChar and start <= usedChar[char]:
                # 出现重复字符时 start 变成重复字符的 index + 1
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index-start+1)
            usedChar[char] = index
        return maxLength

    @staticmethod
    def longest_palindrome(test_str: str) -> str:
        # Target: 获取最长回文子串
        # 时间复杂度O(n) 空间复杂度O(n)
        # 算法思想: 先从小回文串来找 大回文串必定包含小回文串
        # 游标一直往后推 遇到小回文串就把 max_len 放大再查找看能不能命中大回文串
        if len(test_str) < 2 or test_str == test_str[::-1]:
            return test_str
        str_len = len(test_str)
        start, max_len = 0, 1
        for cur in range(str_len):
            odd = test_str[cur-max_len-1:cur+1]
            even = test_str[cur-max_len:cur+1]
            if cur-max_len-1 >= 0 and odd == odd[::-1]:
                start = cur-max_len-1
                max_len += 2
                continue
            if cur-max_len >= 0 and even == even[::-1]:
                start = cur-max_len
                max_len += 1
        return test_str[start:start+max_len]


if __name__ == "__main__":
    test_str = "abcsadagegbthbvoxcadesadxczr"
    print(LongestSubString.longest_without_repeating_character(test_str))
    test_str = "sdlasnflsafasldjadahuewr"
    print(LongestSubString.longest_palindrome(test_str))
