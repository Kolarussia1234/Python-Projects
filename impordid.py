# Tüüpkuju, pikem väljakutse, aga on selge millisest moodulist mingi omadus pärineb
import math 
math.sin(3.14)

# Lühike väljakutse, aga võimalikud konfliktid programmis/moodulites
# sisalduvatenimede vahel
from math import *
sin(3.14)

# Lühike väljakutse, impordi sisu selge, pikk deklaratsioon
from math import sin, cos, tan


# Mooduli lokaalne ümber nimetamine (alias)
import math as m
m.sin(0)
