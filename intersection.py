from linguistic import *
from rule import *
import matplotlib.pyplot as plt

class Intersection(object):

    def __init__(self, id):
        self.id = id
        self.antrian = ThreeNormal(60,10,30,50,'Antrian','1_Pendek','2_Sedang','3_Panjang')
        self.lebar = ThreeNormal(10,2,5,8,'Lebar Jalan','1_Sempit','2_Sedang','3_Lebar')
        self.mobil = ThreeNormal(24,4,12,20,'Banyak Mobil','1_Sedikit','2_Sedang','3_Banyak')
        self.waktu = FiveNormal(144,24,48,72,96,120,'Waktu','1_Lebih Cepat','2_Cepat', \
                            '3_Sedang','4_Lama','5_Lebih Lama')

    def inference(self, a_input, l_input, m_input, debug=False):
        self.Q = []
        for i in xrange(3):
            for j in xrange(3):
                for k in xrange(3):
                    if i!=1 and j!=3:
                        self.R1 = Rule(self.antrian, i, \
                                  self.lebar, j, \
                                  self.mobil, k, \
                                  a_input, l_input, m_input, self.waktu)
                        self.Q.append(self.R1.implication())
                        if i==2 and j==0 and k==2 and debug==True:
                             plt.figure(5)
                             self.R1.draw()

        # Inference
        self.waktu_star = np.zeros(len(self.waktu.domain))
        for i in self.waktu.domain:
            self.waktu_star[i] = 0
            for j in xrange(len(self.Q)):
                self.waktu_star[i] = max(self.waktu_star[i],self.Q[j][i])

        # Defuzified
        self.sum_of_weight = 0
        self.sum_of_center_weight = 0
        for i in xrange(len(self.Q)):
            self.left = False
            self.right = False
            self.left_id = 0
            self.right_id = 0
            self.weight = 0
            for j in self.waktu.domain:
                if self.Q[i][j]!=0 and self.left==False and self.right==False:
                    self.left = True
                    self.left_id = j
                elif self.Q[i][j]==0 and self.left==True and self.right==False:
                    self.right = True
                    self.right_id = j
                self.weight = max(self.weight,self.Q[i][j])
            if self.right==False:
                self.right_id = self.waktu.domain[-1]
            self.sum_of_weight = self.sum_of_weight + self.weight
            self.sum_of_center_weight = self.sum_of_center_weight + (self.left_id+(self.right_id-self.left_id)/2)*self.weight
            # if i==11:
            #     print weight
            #     print left_id
            #     print right_id

        self.result = self.sum_of_center_weight/(self.sum_of_weight*1.0)
        # print sum_of_center_weight
        # print sum_of_weight
        return self.result


    def draw_inference(self, fig_number, label):
        plt.gca().set_ylim([0,1])
        plt.title('Persimpangan '+label)
        plt.plot(self.waktu.domain, self.waktu_star, 'r')
        plt.axvline(self.result,ls='--',c='b')

    def draw(self):
        # plt.figure(1)
        plt.subplot(411)
        self.antrian.draw(0,60)
        plt.subplot(412)
        self.lebar.draw(2,10)
        plt.subplot(413)
        self.mobil.draw(0,24)
        plt.subplot(414)
        self.waktu.draw(15,144)
        # plt.tight_layout()
