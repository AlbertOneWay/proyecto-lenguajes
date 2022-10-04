from Produccion import prod

#
productions = [["S", "S + P"], ["S", "P"], ["P", "P * K"], ["P", "? K"], ["K", "amd"], ["K", "( C )"], ["C", "id"]]
"""
S=> S + P | P
P=> P * K | ? K
K=> amd | ( C )
C=> id
"""
noTerminals = ["S", "P", "K", "C"]
# ??
z = []
# S
initial = "S"

result = prod(noTerminals, initial, productions)

print(result)