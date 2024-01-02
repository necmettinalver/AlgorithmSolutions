class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        g_ptr = 0
        s_ptr = 0

        while g_ptr < len(g) and s_ptr < len(s):
            if s[s_ptr] >= g[g_ptr]:
                child += 1
                g_ptr += 1
            s_ptr += 1

        return child

#If you feed the little child and aim to feed more children       
"""
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        if sum(g) < sum(s): #self.sumx(g) < self.sumx(s):
            return len(g)
        else:
            child = 0
            cookie_size = 0

            for cookie in s[0:]:
                cookie_size += cookie
                smallest = g[0]
                if(cookie_size >= smallest):
                    child += 1
                    g.pop(0)
                    cookie_size-= smallest

            return child
"""
