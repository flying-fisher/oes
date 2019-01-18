'''Python exercise1: Substring with Concatenation of All Words (from leetcode.com)
Problem description:

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words==[]:
            return []
        lenstr=len(s)
        lenword=len(words[0])
        lensubstr=len(words)*lenword
        times={}
        for word in words:
            if word in times:
                times[word]+=1
            else:
                times[word]=1
        ans=[]
        for i in range(min(lenword,lenstr-lensubstr+1)):
            self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
        return ans
    def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)