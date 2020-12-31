import json
import funcoes
import datetime

with open('C:\\Users\\Winar\\Documents\\VSCODE\\codigosPython\\PROJETO_BRINCANDO_COM_DATAS\\valores.json') as f:
    datasDelancamento = json.load(f)


nasc=input("Digite sua data de nascimeto sem colocar o 0 a esquerda no formato d/m/aaaa ")
numeros=nasc.split("/")
dia=int(numeros[0])
mes=int(numeros[1])
ano=int(numeros[2])
dataNasc=datetime.date(ano,mes,dia)



dataDosfilmes = []

for i in datasDelancamento:
    dataDosfilmes.append(i)

#tenho uma lista de string, quero uma lista de datas

datadataDosfilmes = []
for i in range(len(dataDosfilmes)):
    num=dataDosfilmes[i].split("/")
    datadataDosfilmes.append(datetime.date(int(num[2]),int(num[1]),int(num[0])))

#agora tenho uma lista de datas, eu quero comparar com a data que eu tenho (nascimento do usuario)

datadataDosfilmes.sort()
#deixei em ordem crescente

#agora preciso comparar cada um e achar a data mais próxima

for i in range(len(datadataDosfilmes)):
    elemento = datadataDosfilmes[i]

    if elemento < dataNasc:
       # print(f"O filme {datadataDosfilmes[i]} foi lançado antes da sua data de nascimento")
       pass

    elif elemento > dataNasc:
       # print(f"O filme {datadataDosfilmes[i]} foi lançado DEPOIS da sua data de nascimento")

        diferencaAnterior =abs( datadataDosfilmes[i-1] - dataNasc )
        diferencaPosterior =abs( datadataDosfilmes[i] - dataNasc )

       # print("Diferença ente data do filme anterior e sua data de nasc = ",diferencaAnterior)
       # print("Diferença ente data do filme atual e sua data de nasc = ",diferencaPosterior)

        if diferencaAnterior > diferencaPosterior:

            datanaoformatada = funcoes.retornarStringddmmaaaa( datadataDosfilmes[i].strftime("%d/%m/%Y") )

            print("O filme mais perto da sua data de nascimento sera: " ,datasDelancamento[datanaoformatada] , "\nLançado em", funcoes.retornarDataFormatada( elemento  ))
       
       
        elif diferencaAnterior < diferencaPosterior:

            datanaoformatada= funcoes.retornarStringddmmaaaa( datadataDosfilmes[i-1].strftime("%d/%m/%Y") )


            print("O filme mais perto da sua data de nascimento sera: " ,datasDelancamento[datanaoformatada] , "\nLançado em:", funcoes.retornarDataFormatada( datadataDosfilmes[i-1] ))
        
        else:
            print("Parece que sua data de nascimento está exatamente na metade do intervalo das duas datas")
        
        break



    