# extends mathematical functions
import math

# console will print the following sentence below 
# the new "\n" line character will create a new line
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")

# the following sentences will be printed below and the tab "\t" character will make space between the sentences
print("investment \t\t\t - to calculate the amount of the interest you'll earn on interest")
print("bond \t\t\t\t - to calculate the amount you'll have to pay on a home loan")


# created a variable called "your_calculator" that requests an input of either (investment) or (bond) and converted input to all capital letters 
your_calculator = input("Enter the 'investment' or 'bond': ").upper()

# if variable (your_calculator) is equal to "Investment" in uppercase letters
if your_calculator == "Investment".upper():
 
 your_p = float(input("Enter deposit amount: "))
# output will be displayed
 print(your_p)

# created a variable called your_r and assigned it to a float requesting the user to enter interest rate 
 your_r = float(input("Enter interest rate number (%) percentage sign not included: "))

# output will be displayed
 print(your_r) 

# created a variable called your_t and assigned it to a float requesting the user to enter number of years 
 your_t = float(input("Enter  number of years you plan on investing for: "))
# output will be diplayed
 print(your_t)


# created a variable called (your_interest) and assigned it user input of either uppercase "SIMPLE" or uppercase "COMPOUND" 
 your_interest = input(" Choose either 'simple' or 'compound' interest :").upper()


# if user input is equal to (SIMPLE)
# created a variable total_simple and the following will be executed (your_p * (1+((your_r)/100) * your_t)),converted total using the float function
 if your_interest == "simple".upper():
     total_simple =  float(your_p * (1 + (your_r/ 100) * your_t))

# display total_simple(output)
     print(round(total_simple, 2))

# else if variable your_interest is equal to (COMPOUND) it will execute the following (your_p * math.pow((1+your_r/100), your_t)),converted total using the float function
 elif your_interest == "compound".upper():
     total_compound = float(your_p * math.pow((1+(your_r / 100)),your_t))

# display (total_compound) output
     print(round(total_compound, 2))

# set a default to "not a choice given", if the user does not pick "COMPOUND" or "SIMPLE", it will display default message
 else: 
      print("Did not enter compound or simple")
# else if the user chose uppercase("BOND") 
elif your_calculator ==  "bond".upper():
# created a variable called i and assigned it to a float requesting the user to enter interest rate 
  i = float(input("Enter interest rate for bond: ")) / 100
  print(i)

# created a variable called p and assigned it to a float requesting the user to enter interest rate   
  p = float(input("Enter the present value amount: "))
  print(p)

# created a variable called n and assigned it to a float requesting the user to enter interest rate   
  n = float(input("Enter number of months: "))
  print(n)

# it will execute the following (((i/12)*p) / (1 - (1+(i/12)) ** (-n))),converted total using the float function  
  total_bond = float(((i/12)*p)/(1 - (1+(i/12)) ** (-n)))

# it will display the rounded by two decimal place values 
  print(round(total_bond, 2))

# set our default to the sentence below, it will display the sentence 
else: 
 print("Did not choose 'investment' or 'bond'")


