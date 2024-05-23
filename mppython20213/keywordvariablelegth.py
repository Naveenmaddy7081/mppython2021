def person(name,*data):
    print(name)
    print(data)

person('ashwani',9956477677,'gkp',36,373000,'Male')

def person1(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person1(name='ashwani',age=66,gender='Male',contact='9956477677')
