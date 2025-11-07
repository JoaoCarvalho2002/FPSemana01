#repo FPSemana01 com .gitignore e README.md
#mostrar o valor mais alto

#inputs
#[['moira', (9, 2)], ['joao', (7, 1)], ['ulsa', (2, 1)]]
#Ataque Maria 15
#Defesa Raul 15

#primeira pessoa encontrada se empatar
nome1=input()
str(nome1)
ataque1=input()
int(ataque1)
defesa1=input()
int(defesa1)

nome2=input()
str(nome2)
ataque2=input()
int(ataque2)
defesa2=input()
int(defesa2)

nome3=input()
str(nome3)
ataque3=input()
int(ataque3)
defesa3=input()
int(defesa3)

nomeoutputAta=""
nomeoutputDef=""

dados=[
    [str(nome1),(int(ataque1),int(defesa1))],
    [str(nome2),(int(ataque2),int(defesa2))],
    [str(nome3),(int(ataque3),int(defesa3))]
]

listAtaque=[ataque1,ataque2,ataque3]
listAtaque.sort()

listDefesa=[defesa1,defesa2,defesa3]
listDefesa.sort()

print(dados)


#ataque
if(dados[0][1][0]== int(listAtaque[-1])):
    nomeoutputAta=(str(dados[0][0]))

elif(dados[1][1][0]== int(listAtaque[-1])):
    nomeoutputAta=(str(dados[1][0]))

elif(dados[2][1][0]== int(listAtaque[-1])):
    nomeoutputAta=(str(dados[2][0])) 

print("Ataque "+ nomeoutputAta ,listAtaque[-1]) 
#defesa
if(dados[0][1][1]== int(listDefesa[-1])):
    nomeoutputDef=(str(dados[0][0]))

elif(dados[1][1][1]== int(listDefesa[-1])):
    nomeoutputDef=(str(dados[1][0]))

elif(dados[2][1][1]== int(listDefesa[-1])):
    nomeoutputDef=(str(dados[2][0])) 
     
print("Defesa "+ nomeoutputDef ,listDefesa[-1])