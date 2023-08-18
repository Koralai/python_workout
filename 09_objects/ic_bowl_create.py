from ice_cream import Scoop
from ice_cream import Bowl
from ice_cream import BigBowl

s_1 = Scoop('coffee')
s_2 = Scoop('vanilla')
s_3 = Scoop('chocolate fudge')
s_4 = Scoop('caramel swirl')
s_5 = Scoop('mint chip')

b = Bowl()
b.add_scoops(s_1)
b.add_scoops(s_2, s_3)
b.add_scoops(s_4)
print(b)

bb = BigBowl()
bb.add_scoops(s_4, s_2)
bb.add_scoops(s_5, s_5, s_5, s_5)
print(bb)
print(bb.MAX_SCOOPS)
