from linguistic import *
from rule import *
import matplotlib.pyplot as plt

def init_var():
    antrian = ThreeNormal(60,10,30,50,'Antrian','1_Pendek','2_Sedang','3_Panjang')
    lebar = ThreeNormal(10,2,5,8,'Lebar Jalan','1_Sempit','2_Sedang','3_Lebar')
    mobil = ThreeNormal(24,4,12,20,'Banyak Mobil','1_Sedikit','2_Sedang','3_Banyak')
    waktu = FiveNormal(144,24,48,72,96,120,'Waktu','1_Lebih Cepat','2_Cepat', \
                        '3_Sedang','4_Lama','5_Lebih Lama')
    plt.figure(1)
    plt.subplot(411)
    antrian.draw()
    plt.subplot(412)
    lebar.draw()
    plt.subplot(413)
    mobil.draw()
    plt.subplot(414)
    waktu.draw()
    plt.tight_layout()

    return antrian, lebar, mobil, waktu


def main(a_input, l_input, m_input):
    antrian, lebar, mobil, waktu = init_var()  # init all variables linguistic

    # Implikasi
    # R1 = Rule(antrian, 2, lebar, 0, mobil, 2, a, l, m, waktu)
    # print R1.implication()
    # plt.figure(2)
    # R1.draw()

    Q = []
    for i in xrange(3):
        for j in xrange(3):
            for k in xrange(3):
                if i!=1 and j!=3:
                    R1 = Rule(antrian, i, lebar, j, mobil, k, a_input, l_input, m_input, waktu)
                    Q.append(R1.implication())
                    if i==2 and (j==0) and k==2:
                        plt.figure(2)
                        R1.draw()

    # Inference
    waktu_star = np.zeros(len(waktu.domain))
    for i in waktu.domain:
        waktu_star[i] = 0
        for j in xrange(len(Q)):
            waktu_star[i] = max(waktu_star[i],Q[j][i])

    plt.figure(4)
    plt.title("Waktu'")
    plt.gca().set_ylim([0,1])
    plt.plot(waktu.domain, waktu_star, 'r')

    # Defuzified
    sum_of_weight = 0
    sum_of_center_weight = 0
    for i in xrange(len(Q)):
        left = False
        right = False
        left_id = 0
        right_id = 0
        weight = 0
        for j in waktu.domain:
            if Q[i][j]!=0 and left==False and right==False:
                left = True
                left_id = j
            elif Q[i][j]==0 and left==True and right==False:
                right = True
                right_id = j
            weight = max(weight,Q[i][j])
        if right==False:
            right_id = waktu.domain[-1]
        sum_of_weight = sum_of_weight + weight
        sum_of_center_weight = sum_of_center_weight + (left_id+(right_id-left_id)/2)*weight
        # if i==11:
        #     print weight
        #     print left_id
        #     print right_id

    result = sum_of_center_weight/(sum_of_weight*1.0)
    # print sum_of_center_weight
    # print sum_of_weight
    print result
    plt.axvline(result,ls='--',c='b')

    plt.show()

if __name__=='__main__':
    # Define Fact
    a_input = 46 # 11  - 46
    l_input = 3 # 7 - 3
    m_input = 16 # 8 - 16
    main(a_input, l_input, m_input)
