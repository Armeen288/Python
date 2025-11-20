import math
angledeg= float(input('Enter angle in degrees: '))
anglerad= math.radians(angledeg)
sin = math.sin(anglerad)
cos = math.cos(anglerad)
tan = math.tan(anglerad)
print("Sin(", angledeg, ")=", sin)
print("Cos(", angledeg, ")=", cos)  
print("Tan(", angledeg, ")=", tan)