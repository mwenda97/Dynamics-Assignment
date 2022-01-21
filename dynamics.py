import math
import numpy as np
import matplotlib.pyplot as plt
class chevy():
    def cheb1(self):
        c = (b - a) / 2
        d = (2 * 1 - 1) / (2 * 3)
        z = math.degrees(math.pi)
        x = (a + b) / 2 - c * math.cos(math.radians(z * d))
        print('value for teta 2 first spacing==',x)
        return x

    def cheb2(self):
        c = (b - a) / 2
        d = (2 * 2 - 1) / (2 * 3)
        z = math.degrees(math.pi)
        x = (a + b) / 2 - c * math.cos(math.radians(z * d))
        print('value for teta 2 second spacing==', x)
        return x

    def cheb3(self):
        c = (b - a) / 2
        d = (2 * 3 - 1) / (2 * 3)
        z = math.degrees(math.pi)
        x = (a + b) / 2 - c * math.cos(math.radians(z * d))
        print('value for teta 2 third spacing==', x)
        return x
class angles():
    def angle(self):
        e = 65 + 0.43 * q
        f = 65 + 0.43 * w
        g = 65 + 0.43 * r
        return [e, f, g]

class freudestein():
    def fred(self):
        k1a = math.cos(math.radians(q1))
        k2a = (math.cos(math.radians(q)))
        ka = q-q1
        k3a = (math.cos(math.radians(ka)))
        k1b = (math.cos(math.radians(q2)))
        k2b = (math.cos(math.radians(w)))
        kb = w-q2
        k3b = (math.cos(math.radians(kb)))
        k1c = (math.cos(math.radians(q3)))
        k2c = (math.cos(math.radians(r)))
        kc = r-q3
        k3c = (math.cos(math.radians(kc)))
        frd1 = np.array([(k1a, -k2a, 1), (k1b, -k2b, 1), (k1c, -k2c, 1)])
        frd2 = np.array([k3a, k3b, k3c])
        cramer = np.linalg.solve(frd1, frd2)
        return cramer
class length():
    def lent(self):
        leng = fixed
        length1 = leng/fredi.fred()[0]
        length2 = leng/fredi.fred()[1]
        le = length1**2 + length2**2 + leng**2 -2 *length1 * length2 * fredi.fred()[2]
        length3 = math.sqrt(le)
        return [length1,length2,length3]
class transmission():
    def trans(self):
        tra = -length.lent()[0]
        trb = length.lent()[2]
        trc = -length.lent()[1]
        trd = fixed
        n = a-5
        while n<165:
            n = n+5
            trans = (trb ** 2 + trc ** 2 - tra ** 2 - trd ** 2 + 2 * tra * trd * math.cos(math.radians(n)))/(2*trb*trc)
            transangle = math.degrees(math.acos(trans))
            print('transmission angle',n,transangle)



a = int(input('enter the value for teta 0=='))
b = int(input('enter the value for teta f=='))
fixed = int(input('enter the length of the fixed link=='))
chevy = chevy()
q = chevy.cheb1()
w = chevy.cheb2()
r = chevy.cheb3()
ang = angles()
aw = ang.angle()
q1 = ang.angle()[0]
q2 = ang.angle()[1]
q3 = ang.angle()[2]
print('all anges for teta 4>>',aw)
print('first spacing teta 4>>',q1)
print('second spacing teta 4>>',q2)
print('third spacing teta 4>>',q3)
fredi = freudestein()
print('value of k1==',fredi.fred()[0])
print('value of k2==',fredi.fred()[1])
print('value of k3==',fredi.fred()[2])
length = length()
print('lenth of link a is==',length.lent()[0])
print('lenth of link c is==',length.lent()[1])
print('lenth of link b is==',length.lent()[2])
transmission = transmission()
trt = transmission.trans()



