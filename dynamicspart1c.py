import math
import dynamics
a = dynamics.a
valK = dynamics.freudestein()
valA=valK.fred()[0]
valB = valK.fred()[1]
valC = valK.fred()[2]
print('steve',valC,valB)
n = a - 5
while n < 165:
    n = n + 5
    lengthA = (1-valB)* math.cos(math.radians(n)) - valA +valC
    lengthB = -2 *  math.sin(math.radians(n))
    lengthC = valA - (1+valB)* math.cos(math.radians(n)) + valC
    generated = 65 + 0.43 * n
    value_teta4positive = 2 * math.degrees(math.atan((-lengthB+math.sqrt(lengthB**2-4*lengthA*lengthC))/(2*lengthA)))
    print('required',generated)
    print('generated',value_teta4positive)
    error = value_teta4positive - generated
    print('error',error)



