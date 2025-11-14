#repo FPSemana01 com .gitignore e README.md
#mostrar o valor mais alto

#inputs
#[['moira', (9, 2)], ['joao', (7, 1)], ['ulsa', (2, 1)]]
#Ataque Maria 15
#Defesa Raul 15

#primeira pessoa encontrada se empatar
nome1 = input()
ataque1 = int(input())
defesa1 = int(input())

nome2 = input()
ataque2 = int(input())
defesa2 = int(input())

nome3 = input()
ataque3 = int(input())
defesa3 = int(input())

nomeoutputAta=""
nomeoutputDef=""

dados=[
    [nome1,(ataque1,defesa1)],
    [nome2,(ataque2,defesa2)],
    [nome3,(ataque3,defesa3)]
]
print(dados)

#ataque
maior_ataque = max(ataque1, ataque2, ataque3)

if dados[0][1][0] == maior_ataque:
    nomeoutputAta = dados[0][0]

elif dados[1][1][0] == maior_ataque:
    nomeoutputAta = dados[1][0]

else:
    nomeoutputAta = dados[2][0]

# defesa
maior_defesa = max(defesa1, defesa2, defesa3)

if dados[0][1][1] == maior_defesa:
    nomeoutputDef = dados[0][0]

elif dados[1][1][1] == maior_defesa:
    nomeoutputDef = dados[1][0]

else:
    nomeoutputDef = dados[2][0]

print("Ataque", nomeoutputAta, maior_ataque)
print("Defesa", nomeoutputDef, maior_defesa)