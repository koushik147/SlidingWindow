class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p)>len(s): # length of p is greater then length of s
            return [] # return the empty array
        result = [] # create the resultant empty array
        pcount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0} # create the pcount dictionary with 0
        ssCount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0} # create the sscount dictionary with 0
        for ch in p: # creating the frequency hashmap
            if ch in pcount:
                pcount[ch]+=1 # increment the ch value by 1
            else:
                pcount[ch]=1 # setting the ch value by 1
    
        start =0

        #constructing the window
        for end in range(len(p)): # run until the s[end] value in pcount then increment end value by 1
            if s[end] in pcount:
                ssCount[s[end]]+=1
        if pcount==ssCount: # if pcount is equal to sscount the append the start value to result
            result.append(start)


        #sliding/moving the window
        for end in range(len(p),len(s)): #incoming element at end then increase the count at ssCount
            if s[end] in pcount:
                ssCount[s[end]]+=1

            if s[start] in ssCount: #outgoing element at start then decrease the count at ssCount
                ssCount[s[start]]-=1
            start+=1

            if pcount==ssCount: # if pcount is equal to sscount the append the start value to result
                result.append(start)


        return result # returning the resultant array
