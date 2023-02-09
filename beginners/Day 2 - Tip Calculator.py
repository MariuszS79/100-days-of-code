print ("Welcome to the tip calculator")
total = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give?: "))
people = int(input("How many people to split the bill?: "))

tip_result = (total/100) * tip
tip_result = round((tip_result/people), 2)
total_result = round((total/people),2)

print("Bill per person is ",total_result, "$")
print("Tip per person is ",tip_result, "$")
print ("Total per person is ",(total_result+tip_result), "$")
