x,y,z=map(int,input().split())
totalmin=z*1440
totaltime=x*y
if totalmin<totaltime:
    print("NO")
else:
    print("YES")
