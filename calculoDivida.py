import math
import decimal
from os import system

def clear():
    system('cls')

def round_up(x, place=2):
    context = decimal.getcontext()
    # get the original setting so we can put it back when we're done
    original_rounding = context.rounding
    # change context to act like ceil()
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)

def proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, extra, extra2, extra3, extra4, acadMes):
    nextFatura = 0
    if aFaltam > 0:
        nextFatura += aParcela
    if bFaltam > 0:
        nextFatura += bParcela
    if cFaltam > 0:
        nextFatura += cParcela
    if extra > 0:
        nextFatura += extra
    if extra2 > 0:
        nextFatura += extra2
    if extra3 > 0:
        nextFatura += extra3
    if extra4 > 0:
        nextFatura += extra4
    nextFatura += acadMes
    return nextFatura

def parcelaCompra(valor, parcelas):
    parcelado = []
    for i in range(parcelas):
        parcelado.append(valor/parcelas)
    return parcelado



meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

salarioBruto = 811.4
chequeEspecial = 300
livreCheque = 0


contaSky = 130
contaCondo = 300


motherboard = 338.24
moboCartao = 338.24
gabinete = 210
cpu = 576
fonte600w = 295
'''fonte650w = 288 + 34
f650wCartao = 339 + 34'''
fonteAli = 237.92
ram8 = 99.52
impostoRam8 = 20.38
totalRam8 = round_up(ram8 + impostoRam8)
ram16 = 155.42
impostoRam16 = 31.22
totalRam16 = round_up(ram16 + impostoRam16)
ram32 = 249.60
impostoRam32 = 51.14
totalRam32 = round_up(ram32 + impostoRam32)
ram = round_up(ram8 + impostoRam8 + ram16 + impostoRam16)
gpu = 952.45

componentes = [motherboard, gabinete, cpu, fonte600w, gpu]
comprados = [gpu, cpu, gabinete, motherboard]
faltaComprar = [componente for componente in componentes if componente not in comprados]

surplus = 0
maxCartao = 1100
livreCartao = 0
faturaAtual = 536.54
usoCheque = 63.61
aParcela = 0
aFaltam = 0
bParcela = 191.90
bFaltam = 2
cParcela = 22.15
cFaltam = 9
dParcela = 16.54
dFaltam = 4
acadMes = 130

duasContas = contaCondo + contaSky
duasContasEx = f"({contaCondo} + {contaSky})"

pcDict = {
    "2X 8GB de RAM": totalRam16,
    "fonte 600W": fonte600w
}
pcCartao = {
    "2X 8GB de RAM": totalRam16,
    "fonte 600W": fonte600w
}


avulso = 0
entrada = 's'
contLacos = 0
mesAtual = True
cont = 2
comprarParcela1 = []
comprarParcela2 = []
comprarParcela3 = []
comprarParcela4 = []



entrada = input(f"Quanto entrou em {meses[cont]}? ")
try:
    avulso = float(entrada)
except:
    pass

while(entrada != 'n'):
    compravel = []
    comprar = 0
    virgula = ''
    contLacos = 0
    comprando = ''
    cartaoOuPix = []

    pagar = round_up(faturaAtual + usoCheque + duasContas)
    pagarEx = f'{faturaAtual} + {usoCheque} + {duasContasEx}'
    usoCheque = 0
    livreCheque = 0
    montante = salarioBruto + avulso
    if mesAtual == True:
        pagar = round_up(faturaAtual)
        montante = 364.30 + avulso
        mesAtual = False
    avulso = 0
    resto = round_up(montante - pagar)
    livreCartao += faturaAtual
    
    if resto < 0 and resto >= -300:
        usoCheque = round_up(abs(resto))
        livreCheque = chequeEspecial - usoCheque
        resto = 0
    elif resto < -300:
        resto += 300
        usoCheque = 300
        livreCheque = 0
    else:
        livreCheque = chequeEspecial - usoCheque
        avulso = resto

    for i in list(pcDict):
        if contLacos > 0 and contLacos < len(list(pcDict)) and compravel:
            virgula = ', '
        if pcDict[i] <= avulso + livreCheque:
            compravel.append(f'{virgula}{i} por {pcDict[i]}')
            avulso -= pcDict[i]
            if avulso < 0:
                usoCheque = abs(avulso)
                avulso = 0
                livreCheque -= usoCheque
            cartaoOuPix.append('no pix')
            del pcDict[i]
            del pcCartao[i]
        contLacos += 1

    for i in list(pcCartao):
        if contLacos > 0 and contLacos < len(list(pcCartao)) and compravel:
            virgula = ', '
        if pcCartao[i] <= livreCartao:
            compravel.append(f'{virgula}{i} por {pcCartao[i]}')
            livreCartao -= pcCartao[i]
            comprar += pcCartao[i]
            cartaoOuPix.append('no cartão')
            del pcCartao[i]
            del pcDict[i]    
        contLacos += 1
        '''for i in parcelaCompra(comprar, 5):
            if not comprarParcela1:
                comprarParcela1.append(i)
            if not comprarParcela2:
                comprarParcela2.append(i)
            if not comprarParcela3:
                comprarParcela3.append(i)
            if not comprarParcela4:
                comprarParcela4.append(i)'''

    

    if compravel and compravel != 'Tudo foi comprado':
        for i in range(len(compravel)):
            comprando += f'{compravel[i]} {cartaoOuPix[i]}'

    livreCartao = round_up(livreCartao)
    printar = f'''Tanto que deve pagar: {pagar} ({faturaAtual} + Cheque Especial Usado + {duasContas})
Tanto que tem para pagar: {montante}
Tanto que sobrou: {resto}
Tanto que usou do cheque especial: {usoCheque}
Tanto que tem livre no cheque especial: {livreCheque}
Tanto que tem livre no cartão: {livreCartao}
Pode comprar: {comprando}
Falta comprar: {list(pcDict)}

'''
    print(printar)
    aFaltam -= 1
    bFaltam -= 1
    cFaltam -= 1

    if not comprarParcela1:
        comprarParcela1.append(0)
    if not comprarParcela2:
        comprarParcela2.append(0)
    if not comprarParcela3:
        comprarParcela3.append(0)
    if not comprarParcela4:
        comprarParcela4.append(0)

    faturaAtual = round_up(proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, comprarParcela1[0], comprarParcela2[0], comprarParcela3[0], comprarParcela4[0], acadMes))
    if comprarParcela1:
        comprarParcela1.pop(0)
    if comprarParcela2:
        comprarParcela2.pop(0)
    if comprarParcela3:
        comprarParcela3.pop(0)
    if comprarParcela4:
        comprarParcela4.pop(0)
    
    cont += 1
    if cont == 12:
        cont = 0
    entrada = input(f"Quanto entrou em {meses[cont]}? ")
    try:
        avulso += float(entrada)
    except:
        pass
    
    
