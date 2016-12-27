from linguistic import *
from rule import *
from intersection import *
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

number_of_intersection = 4
x = PrettyTable(["Attribut", "Persimpangan 1", "Persimpangan 2", "Persimpangan 3", "Persimpangan 4"])
x.align["X"] = "l" # Left align city names
x.padding_width = 1 # One space between column edges and contents (default)

def main(a_input, l_input, m_input):
    intersection = []
    for i in xrange(number_of_intersection):
        intersection.append(Intersection(i))

    plt.figure(1)
    # draw intersection linguistic rule
    intersection[0].draw()
    plt.tight_layout()

    result = []
    for i in xrange(number_of_intersection):
        # for debugging purpose, below code will print example of implication
        # if i==0:
        #     debug=True
        result.append(intersection[i].inference(a_input[i], l_input[i],
                        m_input[i], debug))
        plt.figure(8)
        plt.subplot(410 + (i+1))
        # draw intersection result Defuzified
        intersection[i].draw_inference(8+i,str(i))
    plt.tight_layout()

    result = np.around(np.asarray(result),decimals=2)
    x.add_row(['Panjang Antrian',a_input[0],a_input[1],a_input[2],a_input[3]])
    x.add_row(['Lebar Jalan',l_input[0],l_input[1],l_input[2],l_input[3]])
    x.add_row(['Banyak Mobil',m_input[0],m_input[1],m_input[2],m_input[3]])
    x.add_row(['Lama Hijau',result[0],result[1],result[2],result[3]])
    print x
    plt.show()

if __name__=='__main__':
    # Define Fact
    a_input = np.asarray([46, 11, 20, 18])
    l_input = np.asarray([3, 7, 4, 5])
    m_input = np.asarray([16, 4, 8, 10])
    main(a_input, l_input, m_input)
