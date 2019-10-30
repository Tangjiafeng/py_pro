# 目标字符串中匹配模式串的位置
# https://leetcode-cn.com/problems/implement-strstr/solution/python3-sundayjie-fa-9996-by-tes/
class Sunday:
    def strStr(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1,-1,-1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack) : return -1
        if needle == "" : return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx+len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx+len(needle)]

            # 判断是否匹配
            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]


        return -1 if idx+len(needle) >= len(haystack) else idx

if __name__ == '__main__':
    sunday = Sunday()
    print(sunday.strStr("hello", "ll"))