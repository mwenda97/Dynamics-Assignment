import math
import numpy as np


k1A = ((math.cos(math.radians(73.03)))**2 +(math.cos(math.radians(84.75)))**2 +(math.cos(math.radians(103.7)))**2
       +(math.cos(math.radians(122.65)))**2+(math.cos(math.radians(134.37)))**2)
k1B = (math.cos(math.radians(18.67))*math.cos(math.radians(73.03))+math.cos(math.radians(45.92))*math.cos(math.radians(84.75))
       +math.cos(math.radians(90))*math.cos(math.radians(103.7))+math.cos(math.radians(134.08))
       *math.cos(math.radians(122.65))+math.cos(math.radians(161.33))*math.cos(math.radians(134.37)))
k1C = (math.cos(math.radians(73.03))+math.cos(math.radians(84.75))+math.cos(math.radians(103.7))+math.cos(math.radians(122.65))
       +math.cos(math.radians(134.37)))
k1D = (math.cos(math.radians(73.03))*math.cos(math.radians(18.67-73.03))+math.cos(math.radians(84.75))
       *math.cos(math.radians(45.92-84.75))+math.cos(math.radians(103.7))*math.cos(math.radians(90-103.7))
       +math.cos(math.radians(122.65))*math.cos(math.radians(134.08-122.65))+math.cos(math.radians(134.37))
       *math.cos(math.radians(161.33-134.37)))

k2A = (math.cos(math.radians(18.67))*math.cos(math.radians(73.03))+math.cos(math.radians(45.92))*math.cos(math.radians(84.75))
       +math.cos(math.radians(90))*math.cos(math.radians(103.7))+math.cos(math.radians(134.08))
       *math.cos(math.radians(122.65))+math.cos(math.radians(161.33))*math.cos(math.radians(134.37)))
k2B = ((math.cos(math.radians(18.67)))**2 +(math.cos(math.radians(45.92)))**2 +(math.cos(math.radians(90)))**2 +
       (math.cos(math.radians(134.08)))**2+(math.cos(math.radians(161.33)))**2)
k2C = ((math.cos(math.radians(18.67))) +(math.cos(math.radians(45.92))) +(math.cos(math.radians(90)))
       +(math.cos(math.radians(134.08)))+(math.cos(math.radians(161.33))))
k2D = (math.cos(math.radians(18.67))*math.cos(math.radians(18.67-73.03))+math.cos(math.radians(45.92))
       *math.cos(math.radians(45.92-84.75))+math.cos(math.radians(90))*math.cos(math.radians(90-103.7))
       +math.cos(math.radians(134.08))*math.cos(math.radians(134.08-122.65))+math.cos(math.radians(161.33))
       *math.cos(math.radians(161.33-134.37)))


k3A = (math.cos(math.radians(73.03))+math.cos(math.radians(84.75))+math.cos(math.radians(103.7))+math.cos(math.radians(122.65))
       +math.cos(math.radians(134.37)))
k3B = ((math.cos(math.radians(18.67))) +(math.cos(math.radians(45.92))) +(math.cos(math.radians(90)))
       +(math.cos(math.radians(134.08)))+(math.cos(math.radians(161.33))))
k3C = 1
k3D = ((math.cos(math.radians(18.67-73.03))) +(math.cos(math.radians(45.92-84.75))) +(math.cos(math.radians(90-103.7)))
       +(math.cos(math.radians(134.08-122.65)))+(math.cos(math.radians(161.33-1234.37))))


cram1 = np.array([(k1A,-k1B,k1C),( k2A  , -k2B,k2C),(k3A,-k3B,k3C)])
cram = np.array([k1D,k2D,k3D])
sol = np.linalg.solve(cram1, cram)
print(sol)
print('K1',sol[0],'K2',sol[1],'K3',sol[2])
lenghtA = 410/ sol[0]
print('lenthA==',lenghtA)
lenghtC = 410/sol[1]
print('lenthC==',lenghtC)
b = math.sqrt(-lenghtA**2+-lenghtC**2+410**2 -2*-lenghtA*-lenghtC*sol[2])
print('lengthB==',b)
n = 15 - 5
valA = sol[0]
valB = sol[1]
valC = sol[2]
while n < 165:
    n = n + 5
    lengthA = (1-valB)* math.cos(math.radians(n)) - valA +valC
    #print('st A',lenghtA)
    lengthB = -2 *  math.sin(math.radians(n))
    #print('stB',lengthB)
    lengthC = valA - (1+valB)* math.cos(math.radians(n)) + valC
    #print('stC',lenghtC)
    value_teta4positive = 2 * math.degrees(math.atan((-lengthB+math.sqrt(lengthB**2-4*lengthA*lengthC))/(2*lengthA)))
    generated = 65 + 0.43 * n
    print(generated)
    error = generated - value_teta4positive
    print('least str',value_teta4positive)
    print('the erroris ==',error)




