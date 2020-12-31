import datetime
def retornarDataFormatada(dataa=datetime.datetime.now):
    return (dataa.strftime("\nDIA---%d, %a\nMES---%m, %B\nANO---%Y"))

def retornarStringddmmaaaa(texto='01/02/2000'):
    #obetivo é transformar esse estilo em 1/2/2000
    #primeiro vou separar pelo / e se for igual ou maior que 10 permanece o mesmo numero
    #depois eu junto novamente a lista em uma string e a retorno
    #o ano fica inalterado 
    lista = texto.split("/")
    lretorno = []
    
    lretorno.append(int(lista[0]))
    lretorno.append(int(lista[1]))
    lretorno.append(int(lista[2]))

    sretorno = str(lretorno[0])+"/"+str(lretorno[1])+"/"+str(lretorno[2])
    return sretorno

