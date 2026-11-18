def make_validator(min_value):
    def validator(number):
        return number >= min_value
    return validator

check_18 = make_validator(18)
check_100 = make_validator(100)

print(check_18(20))   
print(check_18(10))   

print(check_100(120)) 
print(check_100(50))  