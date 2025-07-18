def main():
#collecting information from user
    weight=float(input("What's your weight (strictly in kg)? "))
    height=float(input("What's your height (strictly in meters)? "))
    result=bmi(weight, height)
    print(f'Your BMI is: {result} \nYour BMI category is: {bmi_category(result)}')
#calculating bmi
def bmi(weight, height):
    return (round(weight/pow(height, 2), 2))
#defining bmi category
def bmi_category(bmi_value):
    if bmi_value<18.5:
        return 'Underweight'
    elif bmi_value>18.5:
        return 'Good'
    elif bmi_value>25:
        return 'Overweight'
    else:
        return 'Danger zone'
main()