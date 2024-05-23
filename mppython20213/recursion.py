#what is recursion? --When a function calls itself
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=0
def msg():
    global i
    i=i+1
    print("Good Evening=",i)
    msg()

msg()