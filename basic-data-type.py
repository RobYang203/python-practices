bool_a = True
bool_b = False
bool_c = None

print("----- print Boolean -----")
print("a = ", bool_a, type(bool_a))
print("Not a = ", not bool_a)
print(bool_b, type(bool_a))
print(bool_c, type(bool_a))

int_a = 1
int_b = -1
int_add = int_a + int_b

print("----- print Integer -----")
print(int_a, type(int_a))
print(int_b, type(int_b))
print("a + b = ", int_add, type(int_add))

float_a = 1.1
float_b = -1.1
float_add = float_a + float_b

print("----- print Float -----")
print(float_a, type(float_a))
print(float_a, type(float_a))
print(float_b, type(float_b))
print("a + b = ", float_add, type(float_add))

str_a = "hello"
str_b = "world"
str_c = " "
str_add = str_a + str_c + str_b

print("----- print String -----")
print(str_a, type(str_a), len(str_a))
print(str_b, type(str_b), len(str_b))
print('count l in a = ' , str_a.count("l"))
print("upper a = " , str_a.upper())
print("capitalize a = " , str_a.capitalize())
print("a + c + b = ", str_add, type(str_add), len(str_add))

str_number = '1234'
convert_int_a = int(str_number)
covert_float_b = float(str_number)
convert_str_c =  str(float_a)

print("----- print Convert type -----")
print(convert_int_a, type(convert_int_a))
print(covert_float_b, type(covert_float_b))
print(convert_str_c, type(convert_str_c))

print("----- print Multiple type to same variable -----")
multi_a = 1
print(multi_a , type(multi_a))

multi_a = 1.1
print(multi_a , type(multi_a))

multi_a = 'hello'
print(multi_a , type(multi_a))