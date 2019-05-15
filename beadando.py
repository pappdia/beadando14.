import sys

def haromszog_szamok(n):
    for i in range(1,n+1):
        if (i**2+i)//2<=n and ((i**2+i)//2)%2!=0:
            print((i**2+i)//2,file=out_file)


n=int(sys.argv[1])
out_file=open("haromszog.txt","w")
haromszog_szamok(n)