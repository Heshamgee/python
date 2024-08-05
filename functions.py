#function as a tutorial 
"""function is a block of code that can use it when we call"""

#my code is a function calculats the number of hours in the day with variables days and printing message
def hours_on_days(no_of_days, message):
    if no_of_days > 0 :
         calculation = no_of_days * 24 
         print(f"The number of hours on {no_of_days} days is = {calculation}")
         print(message)
           
    else: 
        return "u intered a negative value "
# Taking user input
user_input=int(input("inter the number of days ")) 

# Calling the function  
hours_on_days(user_input, "thanks for using our function")

def validate_and_execute():
    #using a function and his prameter as input in one line
if user_input.isdigit() :
    
    #casting = is convert one data type  to other data type variable  
    user_input_number =int(user_input)

    calculated_value =days_to_units(user_input_number)
    print(calculated_value)
else :
    print("your input is not a number ,dont ruin my program")