#############################################################
#function 
#Define reusable code blocks:

def greet(name):
    return f"hello,{name}!"

#call it
print(greet("hesham"))
print(greet("ali"))

#function with default parameters 

def power(base,exponent=2):
    return base ** exponent

print(power(5)) #25

print(power(5,1)) # 5

#multiple return values 
def calculate(a,b):
    return a + b , a - b , a * b 

print(f"sum_result , diff_result , prod_result = {calculate(10,5)}")

#####################################################
