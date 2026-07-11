class Solution:

    def encode(self, strs: List[str]) -> str:
        result=[]
        for w in strs:
            result.append(str(len(w)) + "#" + w)
        return "".join(result)
    def decode(self, s: str) -> List[str]:
        i=0
        decoded=[]
        while i<len(s):
            j=s.find("#",i)
            length=int(s[i:j])
            start=j+1
            end=start+length
            word=s[start:end]
            decoded.append(word)
            i=end
        return decoded
