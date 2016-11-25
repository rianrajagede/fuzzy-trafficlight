import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class Rule(object):
    def __init__(self, antrian, ling_1, lebar, ling_2, mobil, ling_3, a, l, m, cons):
        self.ling_1 = ling_1
        self.ling_2 = ling_2
        self.ling_3 = ling_3
        self.antrian = antrian
        self.lebar = lebar
        self.mobil = mobil
        self.a = a
        self.l = l
        self.m = m
        self.cons = cons

    def set_ling_cons(self):
        compare = lambda x, y: Counter(x) == Counter(y)
        if self.ling_2==0:
            alt_2=2
        elif self.ling_2==2:
            alt_2=0
        else:
            alt_2=1
        if( compare([self.ling_1,alt_2,self.ling_3], [0,0,0]) ):
            self.cons_data = self.cons.btm
        if( compare([self.ling_1,alt_2,self.ling_3], [0,0,1]) ):
            self.cons_data = self.cons.nbtm
        if( compare([self.ling_1,alt_2,self.ling_3], [0,0,2]) ):
            self.cons_data = self.cons.nbtm
        if( compare([self.ling_1,alt_2,self.ling_3], [0,2,2]) ):
            self.cons_data = self.cons.ntop
        if( compare([self.ling_1,alt_2,self.ling_3], [0,1,1]) ):
            self.cons_data = self.cons.mid
        if( compare([self.ling_1,alt_2,self.ling_3], [0,1,2]) ):
            self.cons_data = self.cons.mid
        if( compare([self.ling_1,alt_2,self.ling_3], [1,1,1]) ):
            self.cons_data = self.cons.mid
        if( compare([self.ling_1,alt_2,self.ling_3], [1,1,2]) ):
            self.cons_data = self.cons.mid
        if( compare([self.ling_1,alt_2,self.ling_3], [1,2,2]) ):
            self.cons_data = self.cons.ntop
        if( compare([self.ling_1,alt_2,self.ling_3], [2,2,2]) ):
            self.cons_data = self.cons.top

    # Operating Min di implikasi
    def generate_fp(self):
        if self.ling_1==0:
            self.antrian_data = self.antrian.btm
        elif self.ling_1==1:
            self.antrian_data = self.antrian.mid
        else:
            self.antrian_data = self.antrian.top

        if self.ling_2==0:
            self.lebar_data = self.lebar.btm
        elif self.ling_2==1:
            self.lebar_data = self.lebar.mid
        else:
            self.lebar_data = self.lebar.top

        if self.ling_3==0:
            self.mobil_data = self.mobil.btm
        elif self.ling_3==1:
            self.mobil_data = self.mobil.mid
        else:
            self.mobil_data = self.mobil.top

        # print self.antrian_data
        # print self.lebar_data
        # print self.mobil_data
        # print self.antrian_data[self.a]
        # print self.lebar_data[self.l]
        # print self.mobil_data[self.m]
        return min(self.antrian_data[self.a], self.lebar_data[self.l], self.mobil_data[self.m])

    # Menggunakan implikasi mamdani
    def implication(self):
        self.ret = []
        self.set_ling_cons()
        self.fp = self.generate_fp()
        # print self.cons_data
        # print self.fp
        for i in xrange(len(self.cons_data)):
            self.ret.append(min(self.fp, self.cons_data[i]))
        return self.ret

    def draw(self):
        plt.subplot(411)
        plt.title('Antrian')
        plt.plot(self.antrian.domain,self.antrian_data,'r')
        plt.plot(self.a,self.antrian_data[self.a],'ob')
        plt.subplot(412)
        plt.title('Lebar Jalan')
        plt.plot(self.lebar.domain,self.lebar_data,'r')
        plt.plot(self.l,self.lebar_data[self.l],'ob')
        plt.subplot(413)
        plt.title('Banyak Mobil')
        plt.plot(self.mobil.domain,self.mobil_data,'r')
        plt.plot(self.m,self.mobil_data[self.m],'ob')
        plt.subplot(414)
        plt.gca().set_ylim([0,1])
        plt.title('Rule')
        plt.plot(np.arange(len(self.cons_data)),self.ret,'r')
        plt.tight_layout()
