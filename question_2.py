import numpy as np
import math
import matplotlib.pyplot as plt
class least():
    def les(self):
        k1A = ((math.cos(math.radians(70))) ** 2 + (math.cos(math.radians(76))) ** 2 + (
            math.cos(math.radians(83))) ** 2
               + (math.cos(math.radians(91))) ** 2 + (math.cos(math.radians(100))))
        k1B = (math.cos(math.radians(40)) * math.cos(math.radians(70)) + math.cos(math.radians(45)) * math.cos(
            math.radians(76))
               + math.cos(math.radians(50)) * math.cos(math.radians(83)) + math.cos(math.radians(55))
               * math.cos(math.radians(91)) + math.cos(math.radians(60)) * math.cos(
                    math.radians(100)))
        k1C = (math.cos(math.radians(70)) + math.cos(math.radians(76)) + math.cos(math.radians(83)) + math.cos(
            math.radians(91))
               + math.cos(math.radians(100)))
        k1D = (math.cos(math.radians(70)) * math.cos(math.radians(40 - 70)) + math.cos(math.radians(76))
               * math.cos(math.radians(45 - 76)) + math.cos(math.radians(83)) * math.cos(math.radians(50 - 83))
               + math.cos(math.radians(91)) * math.cos(math.radians(55 - 91)) + math.cos(math.radians(100))
               * math.cos(math.radians(60 - 100)))
        k2A = (math.cos(math.radians(40)) * math.cos(math.radians(70)) + math.cos(math.radians(45)) * math.cos(
            math.radians(76))
               + math.cos(math.radians(50)) * math.cos(math.radians(83)) + math.cos(math.radians(55))
               * math.cos(math.radians(91)) + math.cos(math.radians(60)) * math.cos(
                    math.radians(100)))
        k2B = ((math.cos(math.radians(40))) ** 2 + (math.cos(math.radians(45))) ** 2 + (
            math.cos(math.radians(50))) ** 2 +
               (math.cos(math.radians(55))) ** 2 + (math.cos(math.radians(60))) ** 2)
        k2C = ((math.cos(math.radians(40))) + (math.cos(math.radians(45))) + (math.cos(math.radians(50)))
               + (math.cos(math.radians(55))) + (math.cos(math.radians(60))))
        k2D = (math.cos(math.radians(40)) * math.cos(math.radians(40 - 70)) + math.cos(math.radians(45))
               * math.cos(math.radians(45 - 76)) + math.cos(math.radians(50)) * math.cos(math.radians(50 - 83))
               + math.cos(math.radians(55)) * math.cos(math.radians(55 - 91)) + math.cos(
                    math.radians(60)) * math.cos(math.radians(60 - 100)))
        k3A = (math.cos(math.radians(70)) + math.cos(math.radians(76)) + math.cos(math.radians(83)) + math.cos(
            math.radians(91))
               + math.cos(math.radians(100)))
        k3B = ((math.cos(math.radians(40))) + (math.cos(math.radians(45))) + (math.cos(math.radians(50)))
               + (math.cos(math.radians(55))) + (math.cos(math.radians(60))))
        k3C = 1
        k3D = ((math.cos(math.radians(40 - 70))) + (math.cos(math.radians(45 - 76))) + (
            math.cos(math.radians(50 - 83)))
               + (math.cos(math.radians(55 - 91))) + (math.cos(math.radians(60 - 100))))
        cramerA = np.array([(k1A,-k1B,k1C),(k2A,-k2B,k2C),(k3A,-k3B,k3C)])
        cramerB = np.array([k1D,k2D,k3D])
        solution = np.linalg.solve(cramerA,cramerB)
        print('K1==',solution[0],'K2==',solution[1],'K3==',solution[2])
        lenthA = 180/solution[0]
        print('lenght of linkA==',lenthA)
        lenthC = 180/solution[1]
        print('lenth of linkC ==',lenthC)
        lenthB = math.sqrt(lenthA**2+lenthC**2+180**2-2*lenthA*lenthC*solution[2])
        print('lenth of linkB ==',lenthB)
        n = 39
        while n < 60:
            n = n + 1
            trans = (lenthB ** 2 + -lenthC ** 2 - lenthA ** 2 - 180 ** 2 + 2 * lenthA * 180 * math.cos(math.radians(n)))\
                    / (2 * lenthB * -lenthC)
            transangle = math.degrees(math.acos(trans))
            print('transmission angle', n, transangle)

        lengthA = (1 - solution[1]) * math.cos(math.radians(40)) - solution[0] + solution[2]
        print('structural lenghtA==',lenthA)
        lengthB = -2 * math.sin(math.radians(40))
        print('structural lenthB==',lenthB)
        lengthC = solution[0] - (1 + solution[1]) * math.cos(math.radians(40)) + solution[2]
        print('structural lenghtC==',lenthC)

        n = 40
        m =70
        lengthA = (1 - solution[1]) * math.cos(math.radians(n)) - solution[0] + solution[2]
        print('st A',lengthA)
        lengthB = -2 * math.sin(math.radians(n))
        print('stB',lengthB)
        lengthC = solution[0] - (1 + solution[2]) * math.cos(math.radians(n)) + solution[2]
        print('stC',lengthC)
        value_teta4positive = 2 * math.degrees(math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
        value_teta4positive = value_teta4positive/2
        generated = m
        print(generated)
        error = generated - value_teta4positive
        print('least str', value_teta4positive)
        print('the errors 40 ==', error)
        #################################################################################################################
        n = 45
        m = 76
        lengthA = (1 - solution[1]) * math.cos(math.radians(n)) - solution[0] + solution[2]
        print('st A', lengthA)
        lengthB = -2 * math.sin(math.radians(n))
        print('stB', lengthB)
        lengthC = solution[0] - (1 + solution[2]) * math.cos(math.radians(n)) + solution[2]
        print('stC', lengthC)
        value_teta4positive = 2 * math.degrees(
            math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
        value_teta4positive = value_teta4positive / 2
        generated = m
        print(generated)
        error = generated - value_teta4positive
        print('least str', value_teta4positive)
        print('the errors 45 ==', error)
        ################################################################################################################
        n = 50
        m = 83
        lengthA = (1 - solution[1]) * math.cos(math.radians(n)) - solution[0] + solution[2]
        print('st A', lengthA)
        lengthB = -2 * math.sin(math.radians(n))
        print('stB', lengthB)
        lengthC = solution[0] - (1 + solution[2]) * math.cos(math.radians(n)) + solution[2]
        print('stC', lengthC)
        value_teta4positive = 2 * math.degrees(
            math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
        value_teta4positive = value_teta4positive / 2
        generated = m
        print(generated)
        error = generated - value_teta4positive
        print('least str', value_teta4positive)
        print('the errors 50 ==', error)
        ################################################################################################################
        n = 55
        m = 91
        lengthA = (1 - solution[1]) * math.cos(math.radians(n)) - solution[0] + solution[2]
        print('st A', lengthA)
        lengthB = -2 * math.sin(math.radians(n))
        print('stB', lengthB)
        lengthC = solution[0] - (1 + solution[2]) * math.cos(math.radians(n)) + solution[2]
        print('stC', lengthC)
        value_teta4positive = 2 * math.degrees(
            math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
        value_teta4positive = value_teta4positive / 2
        generated = m
        print(generated)
        error = generated - value_teta4positive
        print('least str', value_teta4positive)
        print('the errors 55 ==', error)
        ################################################################################################################
        n = 60
        m = 100
        lengthA = (1 - solution[1]) * math.cos(math.radians(n)) - solution[0] + solution[2]
        print('st A', lengthA)
        lengthB = -2 * math.sin(math.radians(n))
        print('stB', lengthB)
        lengthC = solution[0] - (1 + solution[2]) * math.cos(math.radians(n)) + solution[2]
        print('stC', lengthC)
        value_teta4positive = 2 * math.degrees(
            math.atan((-lengthB + math.sqrt(lengthB ** 2 - 4 * lengthA * lengthC)) / (2 * lengthA)))
        value_teta4positive = value_teta4positive / 2
        generated = m
        print(generated)
        error = generated - value_teta4positive
        print('least str', value_teta4positive)
        print('the errors 100 ==', error)


least().les()

