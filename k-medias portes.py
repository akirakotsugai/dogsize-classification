import math
import matplotlib.pyplot as plt

#FUNÇÃO QUE CALCULA A DISTANCIA ENTRE UM PONTO E OUTRO
def distancia(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#LEITURA DA BASE DE DADOS
bf = open("baseApenasPesoAltura.txt", "r")
bf2 = bf.readlines()
todosCachorros = [] #todos os pesos e alturas
for linha in bf2:

    divisao = linha.strip().split(";")
    peso = divisao[3]
    altura = divisao[4]
    todosCachorros.append([peso,altura,""]) #o ultimo indice é o porte pertencente que irá variar até finalizar o programa.

#CENTROS PARA SEREM AJUSTADOS COM VALORES INICIAIS PRÉ-DEFINIDOS (ACHÔMETRO)
portes = {    ##indice 0 é peso em kg e indice 1 é altura em cm.
    "mini": {"centroNovo" : [3,14], "centroAntigo" : [9999,9999], "quantidade" : 0},
    "pequeno" : {"centroNovo" : [10.5,31.5], "centroAntigo" : [9999,9999], "quantidade" : 0},
    "medio" : {"centroNovo" : [20,42.5], "centroAntigo" : [9999,9999], "quantidade" : 0},
    "grande" : {"centroNovo" : [35,59.5], "centroAntigo" : [9999,9999], "quantidade" : 0},
    "gigante" : {"centroNovo" : [52.5,79.5], "centroAntigo" : [9999,9999], "quantidade" : 0}
}


rodar = True
while(rodar):  ###OS CENTROS SERÃO REAJUSTADOS ATÉ QUE A DISTANCIA ENTRE O CENTRO ATUAL E O ANTIGO SEJA MUITO PEQUENA.
    if distancia(portes["mini"]["centroNovo"][0],portes["mini"]["centroNovo"][1],portes["mini"]["centroAntigo"][0],portes["mini"]["centroAntigo"][1]) < 0.01:
        if distancia(portes["pequeno"]["centroNovo"][0],portes["pequeno"]["centroNovo"][1],portes["pequeno"]["centroAntigo"][0],portes["pequeno"]["centroAntigo"][1]) < 0.01:
            if distancia(portes["medio"]["centroNovo"][0],portes["medio"]["centroNovo"][1],portes["medio"]["centroAntigo"][0],portes["medio"]["centroAntigo"][1]) < 0.01:
                if distancia(portes["grande"]["centroNovo"][0],portes["grande"]["centroNovo"][1],portes["grande"]["centroAntigo"][0],portes["grande"]["centroAntigo"][1]) < 0.01:
                    if distancia(portes["gigante"]["centroNovo"][0],portes["gigante"]["centroNovo"][1],portes["gigante"]["centroAntigo"][0],portes["gigante"]["centroAntigo"][1]) < 0.01:
                        rodar = False

    #PESOS E ALTURAS ATUAIS DE CADA CACHORRO QUE USAREMOS PARA PLOTAR GRAFICAMENTE
    pesosMini = []
    alturasMini = []
    pesosPequeno = []
    alturasPequeno = []
    pesosMedio = []
    alturasMedio = []
    pesosGrande = []
    alturasGrande = []
    pesosGigante = []
    alturasGigante = []

    #PERCORRE TODOS OS CACHORROS
    #SE A DISTANCIA NÃO FOR TÃO PEQUENA, ITERA SOBRE TODOS OS VALORES A SEREM AGRUPADOS, ENCONTRA QUAL CENTRO ESTÁ MAIS PERTO E O ADICIONA A ESTE GRUPO.
    for cachorro in todosCachorros:
        distancias = {}
        for key,value in portes.items():
            distancias[key] = distancia(value["centroNovo"][0],value["centroNovo"][1],float(cachorro[0]), float(cachorro[1]))
        maisPerto = min(distancias.values())
        for key, value in distancias.items():
            if value == maisPerto:
                cachorro[2] = key

        if cachorro[2] == "mini":
                pesosMini.append(cachorro[0])
                alturasMini.append(cachorro[1])
        elif cachorro[2] == "pequeno":
                pesosPequeno.append(cachorro[0])
                alturasPequeno.append(cachorro[1])
        elif cachorro[2] == "medio":
                pesosMedio.append(cachorro[0])
                alturasMedio.append(cachorro[1])
        elif cachorro[2] == "grande":
                pesosGrande.append(cachorro[0])
                alturasGrande.append(cachorro[1])
        else:
            pesosGigante.append(cachorro[0])
            alturasGigante.append(cachorro[1])

    #APÓS DEFINIR O GRUPO DE CADA ELEMENTO, PRECISAMOS ENCONTRAR UM NOVO CENTRO PARA O GRUPO.
    #PARA ISSO É PRECISO TIRAR UMA MÉDIA ENTRE TODOS OS ELEMENTOS PERTENCENTES A DETERMINADO GRUPO.
    #ENTÃO PRIMEIRO CONTAMOS QUANTOS ELEMENTOS PERTENCEM A CADA GRUPO
    miniQnt = 0
    pequenoQnt = 0
    medioQnt = 0
    grandeQnt = 0
    giganteQnt = 0

    for cachorro in todosCachorros:
        if cachorro[2] == "mini":
            miniQnt += 1
        elif cachorro[2] == "pequeno":
            pequenoQnt += 1
        elif cachorro[2] == "medio":
            medioQnt += 1
        elif cachorro[2] == "grande":
            grandeQnt += 1
        else:
            giganteQnt += 1

    #AQUI ANEXAMOS A QUANTIDADE TOTAL DE ELEMENTOS PARA CADA GRUPO AO SEU RESPECTIVO GRUPO
    #ESSA ATRIBUIÇÃO NÃO É NECESSÁRIA. APENAS FOI IMPORTANTE PARA VISUALIZAÇÃO DURANTE O DESENVOLVIMENTO OU PODE SER
    #UTIL NO FUTURO

    portes["mini"]["quantidade"] = miniQnt
    portes["pequeno"]["quantidade"] = pequenoQnt
    portes["medio"]["quantidade"] = medioQnt
    portes["grande"]["quantidade"] = grandeQnt
    portes["gigante"]["quantidade"] = giganteQnt


    #AGORA SOMAMOS TODOS OS PESOS E TODAS AS ALTURAS DE CADA GRUPO.
    miniSoma = [0,0] #indice 0 = peso e indice 1 = altura
    pequenoSoma = [0,0]
    medioSoma = [0,0]
    grandeSoma = [0,0]
    giganteSoma = [0,0]

    for cachorro in todosCachorros:
        if cachorro[2] == "mini":
            miniSoma[0] += float(cachorro[0])
            miniSoma[1] += float(cachorro[1])
        elif cachorro[2] == "pequeno":
            pequenoSoma[0] += float(cachorro[0])
            pequenoSoma[1] += float(cachorro[1])
        elif cachorro[2] == "medio":
            medioSoma[0] += float(cachorro[0])
            medioSoma[1] += float(cachorro[1])
        elif cachorro[2] == "grande":
            grandeSoma[0] += float(cachorro[0])
            grandeSoma[1] += float(cachorro[1])
        else:
            giganteSoma[0] += float(cachorro[0])
            giganteSoma[1] += float(cachorro[1])

    ##CENTRO ATUAL DO GRUPO SERÁ O CENTRO ANTIGO PORQUE O NOVO SERÁ CALCULADO NO PRÓXIMO BLOCO
    portes["mini"]["centroAntigo"] = portes["mini"]["centroNovo"]
    portes["pequeno"]["centroAntigo"] = portes["pequeno"]["centroNovo"]
    portes["medio"]["centroAntigo"] = portes["medio"]["centroNovo"]
    portes["grande"]["centroAntigo"] = portes["grande"]["centroNovo"]
    portes["gigante"]["centroAntigo"] = portes["gigante"]["centroNovo"]

    ## TIRANDO MEDIA DE TODOS OS ELEMENTOS DE CADA GRUPO, NA POSIÇÃO X E NA POSIÇÃO Y.
    #AQUI OCORRE A DIVISÃO DO SOMATÓRIO DE PESOS E ALTURAS PELA QUANTIDADE DE ELEMENTOS
    miniNovoCentro = [miniSoma[0] / portes["mini"]["quantidade"], miniSoma[1] / portes["mini"]["quantidade"]]
    pequenoNovoCentro = [pequenoSoma[0] / portes["pequeno"]["quantidade"], pequenoSoma[1] / portes["pequeno"]["quantidade"]]
    medioNovoCentro = [medioSoma[0] / portes["medio"]["quantidade"], medioSoma[1] / portes["medio"]["quantidade"]]
    grandeNovoCentro = [grandeSoma[0] / portes["grande"]["quantidade"], grandeSoma[1] / portes["grande"]["quantidade"]]
    giganteNovoCentro = [giganteSoma[0] / portes["gigante"]["quantidade"], giganteSoma[1] / portes["gigante"]["quantidade"]]

    ## ATRIBUIÇÃO DOS NOVOS CENTROS PARA CADA PORTE.
    portes["mini"]["centroNovo"] = miniNovoCentro
    portes["pequeno"]["centroNovo"] = pequenoNovoCentro
    portes["medio"]["centroNovo"] = medioNovoCentro
    portes["grande"]["centroNovo"] = grandeNovoCentro
    portes["gigante"]["centroNovo"] = giganteNovoCentro

    #PLOTAGEM DE CADA ITERAÇÃO
    print("Posição central do porte mini")
    print("Peso: " + str(portes["mini"]["centroNovo"][0]) + "kg ~ Altura: " + str(portes["mini"]["centroNovo"][1]) + "cm\n")
    print("Posição central do porte pequeno")
    print("Peso: " + str(portes["pequeno"]["centroNovo"][0]) + "kg ~ Altura: " + str(portes["pequeno"]["centroNovo"][1]) + "cm\n")
    print("Posição central do porte medio")
    print("Peso: " + str(portes["medio"]["centroNovo"][0]) + "kg ~ Altura: " + str(portes["medio"]["centroNovo"][1]) + "cm\n")
    print("Posição central do porte grande")
    print("Peso:" + str(portes["grande"]["centroNovo"][0]) + "kg ~ Altura: " + str(portes["grande"]["centroNovo"][1]) + "cm\n")
    print("Posição central do porte gigante")
    print("Peso: " + str(portes["gigante"]["centroNovo"][0]) + "kg ~ Altura: " + str(portes["gigante"]["centroNovo"][1]) + "cm\n")
    print("\n")
    plt.scatter(pesosMini,alturasMini, label="Porte Mini", color="blue", marker=".")
    plt.scatter(pesosPequeno,alturasPequeno, label="Porte Pequeno", color="black", marker=".")
    plt.scatter(pesosMedio,alturasMedio, label="Porte Medio", color="green", marker=".")
    plt.scatter(pesosGrande,alturasGrande, label="Porte Grande", color="red", marker=".")
    plt.scatter(pesosGigante,alturasGigante, label="Porte Gigante", color="orange", marker=".")
    plt.axis('off')
    plt.title("Agrupamento de cachorros por Porte")
    plt.legend()
    plt.show()

    if rodar == True:
        input("Tecle Enter para avançar para o próximo ajuste.")
    else:
        print("Finalizado.")
