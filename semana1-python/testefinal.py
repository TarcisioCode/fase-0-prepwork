# Uma função media(numeros) que recebe uma lista e devolve a média — devolvendo None ou mensagem amigável se a lista for vazia (via if ou try/except, escolha de vocês).
# Um dicionário estoque = {"arroz": 12, "feijao": 8, "cafe": 3} → um loop que imprime produto: quantidade linha a linha, e ao final o total geral.
# Ler um arquivo .txt qualquer e imprimir quantas linhas contêm uma palavra escolhida. (Criem o txt na hora com 5–6 linhas.)
# O chefão: dado um texto em string, contar a frequência de cada palavra com dicionário e imprimir as 5 mais comuns. Se esse sair sem consulta, o cap 9 está pago.
# ===========================
#          ITEM 1
# ===========================

# def media(lst):
#     count = 0
#     soma = 0 
#     for i in lst:
#         count = count + 1 
#         soma = i + soma
#     if count > 0:
#         media = soma/count
#         return media
   
# lista = []
# average = media(lista)
# print(average)



# ===========================
#          ITEM 2
# ===========================

# dc = dict()
# dc = {"arroz": 12, "feijao": 8, "cafe": 3}
# soma = 0
# for (p, q) in dc.items():
#     print(p, q)
#     soma =  soma + q
# print("Total Geral:", soma)

# ===========================
#          ITEM 3
# ===========================

# palavra escolhida = "and"


# count = 0 
# iword = input("Escolha uma palavra: ")
# with open("txtexemplofdinal.txt") as fh:
#     for line in fh:
#         splitada = line.split()
#         if iword in splitada:
#             count = 1 + count   

# print(count)

# ===========================
#          ITEM 4
# ===========================
dct = dict()

try:
    with open("txtexemplofinal.txt") as fh:
        for line in fh:
            splitada = line.split()
            for word in splitada:
                dct[word] = dct.get(word,0) + 1
    dict_ordenado = sorted([(v, k) for k, v in dct.items()], reverse=True)
    for (k,v) in dict_ordenado[:5]:
        print(k,v)
except FileNotFoundError:
    print("aRQUIVO NAO EXISTE")
    quit()
    



        
