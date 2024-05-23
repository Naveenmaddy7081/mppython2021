'''
9 is prime or not
9%2==0
9%3==0  ----

29
29%2,3,4,.....28

'''

n=5
i=2
while i<=n-1:    # 2,3,4
    if n%i==0:
        print("Not prime")
        break
    i = i + 1

else:  # loop else will be executed when loop  runs properly
    print("Prime no")

