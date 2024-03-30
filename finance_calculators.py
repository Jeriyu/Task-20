import math

# define the variable user_input
user_input = ""

# Display menu giving the user the options to choose - investment or bond

menu_text = """investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
   
Enter either 'investment' or 'bond' from the menu above to proceed:
            """

# take the user input and store as a variable, convert to lower case if not entered this way

user_input = input(menu_text).lower()



#  if the user selects investment, ask the user to input
#  - the amount of money they are depositing
#  - the interest rate as a percentage
#  - the number of years they plan on investing

# define the variables
deposit =  0.0
interest_rate = 0.0
years = 0.0
interest = ""
total = 0.0
r = 0.0

# ask again if the user does not enter investment or bond
while user_input != "investment" and user_input != "bond":    
        user_input = input(menu_text).lower()

# if investment is entered ask for more inputs
if user_input == "investment":
    deposit = float(input("Please enter the amount of money you are depositing: "))
    interest_rate = float(input("Please enter the interest rate as a percentage: "))
    r = float(interest_rate)/100
    years = float(input("Please enter the number of years you want to invest for: "))
    interest = input("Please enter the interest type you would like - compound / simple: ").lower()       

    #ask again if user does not choose either simple or compound
    while interest != "simple" and interest != "compound":
             interest = input("Please enter the interest type you would like - compound / simple: ").lower()
    
    # if simple interest
    if interest == "simple":
        total = deposit * (1 + r*years)
        round_total = round(total,2)
        print(f"The total amount after {years} years if you deposit £{deposit} and the interest rate is {interest_rate}%: {round_total}")       
   
    # if compound interest
    else:
        total = deposit * math.pow((1 + r),years)
        round_total = round(total,2)
        print(f"The total amount after {years} years if you deposit £{deposit} and the interest rate is {interest_rate}%: £{round_total}")
        
# if bond is entered ask for more inputs 
else:
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate(%): "))
    i = (interest_rate*0.01)/12
    months = float(input("Please enter the number of months to repay the bond: "))
    repayment = (i * house_value)/(1-(1 + i)**(-months))
    round_repayment = round(repayment,2)
    print(f"The monthly repayments will be £{round_repayment}.")
  