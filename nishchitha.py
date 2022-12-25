class data:
    sumofpapers=[]
    l=[]
    def _init_(self):
        TOI=[3,3,3,3,3,5,6]
        Hindu=[2.5,2.5,2.5,2.5,2.5,4,4]
        ET=[4,4,4,4,4,4,10]
        BM=[1.5,1.5,1.5,1.5,1.5,1.5,1.5]
        HT=[2,2,2,2,2,4,4]
        self.l=['TOI','Hindu','ET','BM','HT']
        self.sumofpapers=[sum(TOI),sum(Hindu),sum(ET),sum(BM),sum(HT)]
        #print(sumofpapers)
s=data()
sl=s.sumofpapers
n=int(input())
res=[]
for i in range(len(sl)):
    for j in range(i+1,len(sl)):
        if((sl[i]+sl[j])<n):
           res.append("{"+str(s.l[i])+","+str(s.l[j])+"}")
for i in res:
    print(i)