import math
n = 60
lengthA = (1 - 0.402) * math.cos(math.radians(n)) - 0.402 + 1.012
print(lengthA)
lengthB = -2 * math.sin(math.radians(n))
print(lengthB)
lengthC = 0.402 - (1 + 0.402) * math.cos(math.radians(n)) + 1.012
print(lengthC)
value_teta4positive = 2 * math.degrees(
    math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))

print(value_teta4positive)


lengthA = (1 - 0.402) * math.cos(math.radians(60)) - 0.402 + 1.012


lengthB = -2 * math.sin(math.radians(60))

lengthC = 0.402 - (1 + 0.402) * math.cos(math.radians(n)) + 1.012

value_teta4positive = 2 * math.degrees(math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
print(value_teta4positive)