# BMI Calculator

# Other Information
width = 75

# Heading
print("*" * width)
print((" BMI CALCULATOR ").center(width, "~"))
print("*" * width)

# Inputs
w = float(input("Enter your weight (in KG)\t\t\t\t\t: "))
height = float(input("Enter your height (in inches/cm/metre)\t\t\t\t: "))
hu = input("Enter the Unit in which the height is entered (inches/cm/metre) : ")

# Height Conversion
if hu == "inches" or hu == "in":  # Inch to metre
    height = height / 39.3701
elif hu == "cm" or hu == "centimetre":  # Cm to metre
    height = height / 100

# BMI Calculation
hs = pow(height, 2)
BMI = w / hs  # BMI calculation

# Output
print("*" * 30)
print("Your BMI is", round(BMI, 1))

# BMI Conditioning
if BMI < 18.5:
    print("You are Underweight.")
if BMI >= 18.5 and BMI <= 24.9:
    print("You lie in Normal BMI range.")
if BMI >= 25 and BMI <= 29.9:
    print("You are Overweight.")
if BMI > 30:
    print("You are Obese.")

# Weight recommendations
if BMI > 24.9:
    pw = 24.9 * hs
    print("To lie under the normal criteria, your preferred weight should be", round(pw, 0), "KG")
    print("You are overweight by", round(w - pw, 1), "KG")

if BMI < 18.5:
    pw = 18.6 * hs
    print("To lie under the normal criteria, your preferred weight should be", round(pw, 0), "KG")
    print("You are underweight by", abs(round(w - pw, 1)), "KG")
