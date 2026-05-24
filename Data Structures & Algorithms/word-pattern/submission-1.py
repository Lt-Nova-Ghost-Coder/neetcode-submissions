class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        self.pattern = pattern
        self.s = s
        array = self.s.split()
        if len(self.pattern) != len(array):
            return False
        
        Map = {}
        reverseMap = {}

        for i in range(len(array)):
            ch = self.pattern[i]
            word = array[i]

            if ch not in Map:
                Map[ch] = word
            elif Map[ch] != word:
                return False
            

            if word not in reverseMap:
                reverseMap[word] = ch
            elif reverseMap[word] != ch:
                return False
        return True
        