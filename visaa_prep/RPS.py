v,c=map(str,input().split())
if (v=='R' and c=='S') or (v=='S' and c=='P') or (v=='P' and c=='R'):
    print("Vignesh")
elif v==c:
    print("NULL")
else:
    print("Charan")
