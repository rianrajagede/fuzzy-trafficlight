import numpy as np
import matplotlib.pyplot as plt

class ThreeNormal(object):
    def __init__(self, domain, A, B, C, title, label_A, label_B, label_C):
        self.A = A
        self.B = B
        self.C = C
        self.title = title
        self.label_A = label_A
        self.label_B = label_B
        self.label_C = label_C
        self.domain = np.arange(domain+1)

        self.btm = np.zeros(len(self.domain))
        self.mid = np.zeros(len(self.domain))
        self.top = np.zeros(len(self.domain))

        for i in self.domain:
            if i<=A:
                self.btm[i] = 1
                self.mid[i] = 0
                self.top[i] = 0
            elif i<=B:
                self.btm[i] = (B-i)/((B-A)*1.0)
                self.mid[i] = (i-A)/((B-A)*1.0)
                self.top[i] = 0
            elif i<=C:
                self.btm[i] = 0
                self.mid[i] = (C-i)/((C-B)*1.0)
                self.top[i] = (i-B)/((C-B)*1.0)
            else:
                self.btm[i] = 0
                self.mid[i] = 0
                self.top[i] = 1

    def draw(self, btm, top):
        plt.title(self.title)
        plt.gca().set_ylim([0,1])
        plt.gca().set_xlim([btm,top])
        plt.plot(self.domain,self.btm,'r',label=self.label_A)
        plt.plot(self.domain,self.mid,'g',label=self.label_B)
        plt.plot(self.domain,self.top,'b',label=self.label_C)

    def up_line(self, x, B, A):
        return (x-B)/((A-B)*1.0)

    def down_line(self, x, B, A):
        return (A-x)/((A-B)*1.0)

    def fuzzifier(self, val, label):
        if label[0]=='1':
            return self.btm[val]
        elif label[0]=='2':
            return self.mid[val]
        else:
            return self.top[val]

class FiveNormal(object):
    def __init__(self, domain, A, B, C, D, E, title, label_A, label_B, label_C, label_D, label_E):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.title = title
        self.label_A = label_A
        self.label_B = label_B
        self.label_C = label_C
        self.label_D = label_D
        self.label_E = label_E
        self.domain = np.arange(domain+1)

        self.btm = np.zeros(len(self.domain))
        self.nbtm = np.zeros(len(self.domain))
        self.mid = np.zeros(len(self.domain))
        self.ntop = np.zeros(len(self.domain))
        self.top = np.zeros(len(self.domain))

        for i in self.domain:
            if i<=A:
                self.btm[i] = 1
                self.mid[i] = 0
                self.top[i] = 0
                self.ntop[i] = 0
                self.nbtm[i] = 0
            elif i<=B:
                self.btm[i] = (B-i)/((B-A)*1.0)
                self.mid[i] = 0
                self.top[i] = 0
                self.ntop[i] = 0
                self.nbtm[i] = (i-A)/((B-A)*1.0)
            elif i<=C:
                self.btm[i] = 0
                self.mid[i] = (i-B)/((C-B)*1.0)
                self.top[i] = 0
                self.ntop[i] = 0
                self.nbtm[i] = (C-i)/((C-B)*1.0)
            elif i<=D:
                self.btm[i] = 0
                self.mid[i] = (D-i)/((D-C)*1.0)
                self.top[i] = 0
                self.ntop[i] = (i-C)/((D-C)*1.0)
                self.nbtm[i] = 0
            elif i<=E:
                self.btm[i] = 0
                self.mid[i] = 0
                self.top[i] = (i-D)/((E-D)*1.0)
                self.ntop[i] = (E-i)/((E-D)*1.0)
                self.nbtm[i] = 0
            else:
                self.btm[i] = 0
                self.mid[i] = 0
                self.top[i] = 1
                self.ntop[i] = 0
                self.nbtm[i] = 0

    def draw(self,btm,top):
        plt.title(self.title)
        plt.gca().set_ylim([0,1])
        plt.gca().set_xlim([btm,top])
        plt.plot(self.domain,self.btm,'r',label=self.label_A)
        plt.plot(self.domain,self.mid,'g',label=self.label_B)
        plt.plot(self.domain,self.top,'b',label=self.label_C)
        plt.plot(self.domain,self.ntop,'m',label=self.label_D)
        plt.plot(self.domain,self.nbtm,'k',label=self.label_E)
