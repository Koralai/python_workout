from ic_scoop import Scoop
from ic_scoop import Bowl

s_1 = Scoop('coffee')
s_2 = Scoop('vanilla')
s_3 = Scoop('chocolate fudge')
s_4 = Scoop('caramel swirl')

b = Bowl()
b.add_scoops(s_1)
b.add_scoops(s_2, s_3)
b.add_scoops(s_4)
print(b)
