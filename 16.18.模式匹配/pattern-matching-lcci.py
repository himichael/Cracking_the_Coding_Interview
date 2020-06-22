from collections import Counter
class Solution:
    def check(self,pattern, value ,lenP):
        """
        :param pattern , value: Be same as patternMatching()
        :param lenP: lenP={'a':la ,'b':lb}
        :return: bool
        """
        strD={}
        strS=set()
        si=0
        for ch in pattern:
            _str=value[si:si+lenP[ch]]
            if ch not in strD:
                if _str not in strS: # 但需注意"a"和"b"不能同时表示相同的字符串
                    strD[ch]=_str
                    strS.add(_str)
                else: return False
            elif _str!=strD[ch]:
                return False
            si += lenP[ch]
        return True

    def patternMatching(self, pattern, value):
        if ""==pattern: return ""==value    # ①
        Cab=Counter(pattern)    #计数pattern中每个元素的出现次数
        na,nb = Cab['a'],Cab['b']   #求得na,nb
        if 0==na:   # 由①: na和nb 不可能同时为0.
            if 0==len(value)%nb:
                return self.check(pattern,value,{'b':len(value)//nb,})
        elif 0==nb: #零值特别处理
            if 0==len(value)%na:
                return self.check(pattern,value,{'a':len(value)//na,})
        else:
            for la in range(len(value)+1):
                sb = len(value)-na*la # sb= nb*lb
                if sb <0:return False
                if sb%nb ==0:
                    lb=sb//nb
                    if self.check(pattern,value,{'a':la,'b':lb}):
                        return True #有解
        return False