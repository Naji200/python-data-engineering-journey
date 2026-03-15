a = 25 
b= '25'
print(type(a))
print(type(b))
parse_a = str(a)
print(type(parse_a))
parse_b = int(b)
print(type(parse_b))
# print(parse_a + parse_b)


print("enter ur age")
age = input()
if age >= 18:
    print("you are an adult")
else:    print("you are a minor")