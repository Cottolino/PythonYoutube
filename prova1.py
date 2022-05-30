from classVideoSearchYoutube import SingleSearch
from classVideoSearchYoutube import Comments2


a = SingleSearch('magic the gathering', 5)
a.ordina()
a.stampa_links()
print('\n\n')
# a.asd()
a.stampa_views()
a.data_time()
a.stampa_ora()

a.stampa_ore_short()

b = Comments2(a)
# b.stampa()
# b.stampa_num_like(0)
# b.stampa_num_like(1)
# b.stampa_num_like(2)
# print(f'num like 0 :{b.get_num_like(0)}')
print(f'num like 1 :{b.get_num_like(0)}')
print(f'num like 2 :{b.get_num_like(1)}')
print(f'num like 3 :{b.get_num_like(2)}')
print(f'num like 4 :{b.get_num_like(3)}')

# print(b.get_num_like(3))
# print(b.get_num_like(4))
# print(f'num like 1 :{b.get_num_like(3)}')

# print(f'num like 1 :{b.get_num_like(0)}')

rannking = []
rannking = a.punteggio_views()

# print(rannking)

# v1 = a.get_view(0)
# v2 = a.get_view(1)
# v3 = a.get_view(2)
# v4 = a.get_view(3)
# v5 = a.get_view(4)

# print(v1)
# print(v2)
# print(v3)
# print(v4)
# print(v5)

print('\n\n')
r1 = a.punteggio_view(0,b.get_num_like(0))
r2 = a.punteggio_view(1, b.get_num_like(1))
r3 = a.punteggio_view(2, b.get_num_like(2))
r4 = a.punteggio_view(3, b.get_num_like(3))

# print(f'num like 0 :{b.get_num_like(0)}')
# r5 = a.punteggio_view(4, b.get_num_like(4))
print('\n')


print(f'Punteggio :{r1}')
print(r2)
print(r3)
print(r4)
# print(r5)


# print(a.get_len())




a2 = SingleSearch('arena mtg', 5)
a2.ordina()
a2.stampa_links()
print('\n\n')
# a.asd()
a2.stampa_views()
a2.data_time()
a2.stampa_ora()

a2.stampa_ore_short()

b2 = Comments2(a2)
# b.stampa()
# b.stampa_num_like(0)
# b.stampa_num_like(1)
# b.stampa_num_like(2)
# print(f'num like 0 :{b.get_num_like(0)}')
print(f'num like 1 :{b2.get_num_like(0)}')
print(f'num like 2 :{b2.get_num_like(1)}')
print(f'num like 3 :{b2.get_num_like(2)}')
print(f'num like 4 :{b2.get_num_like(3)}')

# print(b.get_num_like(3))
# print(b.get_num_like(4))
# print(f'num like 1 :{b.get_num_like(3)}')

# print(f'num like 1 :{b.get_num_like(0)}')

rannking2 = []
rannking2 = a2.punteggio_views()

# print(rannking)

# v1 = a.get_view(0)
# v2 = a.get_view(1)
# v3 = a.get_view(2)
# v4 = a.get_view(3)
# v5 = a.get_view(4)

# print(v1)
# print(v2)
# print(v3)
# print(v4)
# print(v5)

print('\n\n')
r12 = a2.punteggio_view(0,b2.get_num_like(0))
r22 = a2.punteggio_view(1, b2.get_num_like(1))
r32 = a2.punteggio_view(2, b2.get_num_like(2))
r42 = a2.punteggio_view(3, b2.get_num_like(3))

# print(f'num like 0 :{b.get_num_like(0)}')
# r5 = a.punteggio_view(4, b.get_num_like(4))
print('\n')


print(f'Punteggio :{r12}')
print(r22)
print(r32)
print(r42)
# print(r5)


# print(a.get_len())


