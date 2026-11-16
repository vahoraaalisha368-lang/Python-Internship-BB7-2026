#Give values as strings
height_cm = "175"
weight_kg = "68.5"

height_m = float(height_cm) / 100

weight_kg_float = float(weight_kg)

bmi = weight_kg_float / (height_m * height_m)

#print the result
print("Height in meters:", height_m)
print("Weight in kg:", weight_kg_float)
print("Calculated BMI:", bmi)