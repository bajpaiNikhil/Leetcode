


class Stupid(object):
    def getcount(self,s):

        count=[0 for i in range(27)]
        for i in s:
            count[ord(i)-ord("A")+1]+=1
        return self.dfs(count)
    def dfs(self,count):
        sum=0
        for i in range(1,27):
            if count[i]==0:
                continue
            count[i]-=1
            sum+=1
            sum+=self.dfs(count)
            count[i]+=1
        return sum

choti=Stupid()
print(choti.getcount("AAABBC"))
