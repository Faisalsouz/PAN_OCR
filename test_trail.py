import re
from pprint import pprint
# data = '''
# 05.04.0090
# 1
#
#
# erhältlichen Tableau Interfaces
# lassen sich zusätzliche GLT-Kontakte
# aufschalten. Das System kann
#
# die zwei Szenarien-Modi "Urlaub" und
# Abwesenheit" verwalten. Für beide
# Modi können bestimmte Parameter
# programmiert werden.
#
# Das WAREMA climatronic Bediengerät
# kann preisgleich auch
#
# in den Farben "schwarz" oder
# "schwarz/silber" geliefert werden.
# Liefern und montieren. 882,75 882,75
#
#
# 05.04.0091
# 100
# foo bar. 170,42 17042
# '''
#
# rx = r'''(?mx)
# ^
# (?P<item_code>\d\d\.\d\d\.\d{4})
# \s+
# (?P<quantity>\d+)
# \s+
# (?P<description>\S[\s\S]*?)
# [ ]+
# (?P<unit_price>\d+(?:,\d\d)?)
# [ ]+
# (?P<total_sum>\d+(?:,\d\d)?)
# $
# '''
# result = [m.groupdict() for m in re.finditer(rx, data)]
# pprint(result)
lines=[]
with open(r'C:\Users\fkhalil\primeStone\darknet\data\train.txt','r')as f:
    line=f.readlines()
    lines.append(line)
    print('finihed')
print(len(lines[0]))