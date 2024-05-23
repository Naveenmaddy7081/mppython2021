s='welcome in Python in'
print(len(s))
print(s)
print(s[0:])
print(s[0::2])
print(s.title())
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.count('in'))
name='Ram'
print(name.isalpha())
str="Ram123st"
print(str.isalnum())
mobile='9956477677'
print(mobile.isdigit())
test='Her name is Tammana and Tammana is good girl'
print(test.replace('Tammana','Sonia'))
a='!!!!!!!!! Welcome to India                 '
print(a,end="")
print('Hello')
print(a.strip('!'))
print(a.rstrip( ))
print(a.lstrip( ))

text="hello, how, r, you"
print(text.split(','))

print(text.find('hjfgf'))

str2='Welcome'
print(str2.endswith('e'))
print(str2.startswith('W'))
if str2[0]=='w':
    print('Item found')
else:
    print('item not found')



