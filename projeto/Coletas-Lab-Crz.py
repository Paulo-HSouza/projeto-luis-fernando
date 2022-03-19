from copy import deepcopy

class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        caminho = caminho[::-1]
        return caminho
    
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        if atual is None:
            #caminho.append(valor)
            return caminho

        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

class busca(object):

    def amplitude(self, inicio, fim1):
        
        fim = deepcopy(fim1)
        """print("Destinos: ",fim)"""
        caminho = []
        
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            if atual is None: break

            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo in fim:
                        
                    
                    
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        fim.remove(novo)
                        if len(fim) != 0:
                            inicio = novo
                        else:
                            return caminho

        return "caminho não encontrado"


    def profundidade(self, inicio, fim1):
        
       
        fim = deepcopy(fim1)
        """print("Destinos: ",fim)"""
        caminho = []
        
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o ultimo da fila
            atual = l1.deletaUltimo()
            ind = nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo in fim:
                        
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        fim.remove(novo)
                        if len(fim) != 0:
                            inicio = novo
                            # manipular a FILA para a busca
                            l1 = lista()

                            # cópia para apresentar o caminho (somente inserção)
                            l2 = lista()
                            
                            # controle de nós visitados
                            visitado = []
                            linha = []
                            linha.append(inicio)
                            linha.append(0)
                            visitado.append(linha)
                        else:
                            return caminho

        return "caminho não encontrado"
    

"""
********************************************************************
        PROBLEMA 1: DE CRUZEIRO
********************************************************************
"""

nos= ["Vila Romana",
      "Vila Batista",
      "Vila Maria",
      "Vila Paulo Romeu",
      "Vila Canevari",
      "Centro",
      "Itagaçaba",
      "Jardim America",
      "Jardim Europa",
      "Vila Ana Rosa",
      "Regina Celia",
      "KM4",
      "Vila Biondi",
      "Comerciarios",
      "Vila Juvenal",
      "Parque Primavera",
      "Cecap",
      "Vila Brasil"]

grafo= [
            ["Vila Paulo Romeu", "Vila Canevari", "KM4"],                                       # VR
            ["Vila Canevari", "Centro","Regina Celia"],                                         # VB
            ["Itagaçaba", "Jardim America","Vila Ana Rosa"],                                    # VM
            ["Vila Romana","Vila Canevari","Centro","Cecap"],                                   # VPR
            ["Vila Romana","Vila Batista","Vila Paulo Romeu"],                                  # VC
            ["Vila Batista","Vila Paulo Romeu","Jardim America","Regina Celia"],                # CEN
            ["Vila Maria","Jardim America","Vila Biondi"],                                      # IT
            ["Vila Maria", "Centro", "Itagaçaba","KM4","Vila Biondi"],                          # JA
            ["Vila Ana Rosa", "Comerciarios", "Parque Primavera"],                              # JE
            ["Vila Maria", "Jardim Europa","Regina Celia", "Vila Juvenal","Parque Primavera"],  # VAR
            ["Vila Batista", "Centro", "Vila Ana Rosa"],                                             # RC
            ["Vila Romana","Jardim America", "Vila Juvenal"],                                   # KM4
            ["Itagaçaba", "Jardim America", "Comerciarios", "Vila Juvenal", "Cecap"],           # VBI
            ["Vila Juvenal", "Cecap", "Vila Brasil"],                                           # CO
            ["Vila Ana Rosa", "KM4", "Vila Biondi", "Comerciarios", "Vila Brasil"],             # VJ
            ["Jardim Europa", "Vila Ana Rosa"],                                                 # PP
            ["Vila Paulo Romeu", "Vila Biondi", "Comerciarios"],                                # CEC
            ["Comerciarios", "Vila Juvenal"]                                                    # VBR
       ]

"""
nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
       "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
       "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
       "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
       "URZICENI", "VASLUI", "ZERIND"]

# ORDEM DECRESCENTE

grafo = [
            ["ZERIND", "TIMISOARA", "SIBIU"],                 #0
            ["URZICENI", "PITESTI", "GIORGIU", "FAGARAS"],
            ["RIMNICU VILCEA", "PITESTI", "DOBRETA"],
            ["MEHADIA", "CRAIOVA"],
            ["HIRSOVA"],
            ["SIBIU", "BUCARESTE"],
            ["BUCARESTE"],
            ["URZICENI", "EFORIE"],
            ["VASLUI", "NEAMT"],
            ["TIMISOARA", "MEHADIA"],
            ["LUGOJ", "DOBRETA"],
            ["IASI"],
            ["ZERIND", "SIBIU"],
            ["RIMNICU VILCEA", "CRAIOVA", "BUCARESTE"],
            ["SIBIU", "PITESTI", "CRAIOVA"],
            ["RIMNICU VILCEA", "ORADEA", "FAGARAS", "ARAD"],
            ["LUGOJ", "ARAD"],
            ["VASLUI", "HIRSOVA", "BUCARESTE"],
            ["URZICENI", "IASI"],
            ["ORADEA", "ARAD"]
       ]
"""
"""
# ORDEM CRESCENTE

nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
       "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
       "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
       "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
       "URZICENI", "VASLUI", "ZERIND"]
# ORDEM CRESCENTE

grafo = [
            ["SIBIU", "TIMISOARA", "ZERIND"], 
            ["FAGARAS", "GIORGIU", "PITESTI", "URZICENI"], 
            ["DOBRETA", "PITESTI", "RIMNICU VILCEA"],
            ["CRAIOVA", "MEHADIA"], 
            ["HIRSOVA"],
            ["BUCARESTE", "SIBIU"],
            ["BUCARESTE"], 
            ["EFORIE", "URZICENI"], 
            ["NEAMT", "VASLUI"],
            ["MEHADIA", "TIMISOARA"], 
            ["DOBRETA", "LUGOJ"], 
            ["IASI"], 
            ["SIBIU", "ZERIND"],
            ["BUCARESTE", "CRAIOVA", "RIMNICU VILCEA"],
            ["CRAIOVA", "PITESTI", "SIBIU"], 
            ["ARAD", "FAGARAS", "ORADEA", "RIMNICU VILCEA"],
            ["ARAD", "LUGOJ"],
            ["BUCARESTE", "HIRSOVA", "VASLUI"], 
            ["IASI", "URZICENI"], 
            ["ARAD", "ORADEA"]        
        ]
"""

""" 
********************************************************************
        PROBLEMA 2: GRAFO GENÉRICO
********************************************************************
"""


sol = busca()
caminho = []


# PROBLEMA A
origem  = "Itagaçaba"
destino = ["Vila Romana","Jardim America","Vila Ana Rosa"]

print("\n----------------------------------------------------------------\n")

caminho = sol.amplitude(origem,destino)
print("\nAmplitude...........: ",caminho)

print("\n----------------------------------------------------------------\n")

caminho = sol.profundidade(origem,destino)
print("\nProfundidade........: ",caminho)

print("\n----------------------------------------------------------------\n")

"""
caminho = sol.profundidade_limitada(origem,destino,2)
print("\nProf. Limitada (2)..: ",caminho)

caminho = sol.profundidade_limitada(origem,destino,3)
print("\nProf. Limitada (3)..: ",caminho)

caminho = sol.profundidade_limitada(origem,destino,4)
print("\nProf. Limitada (4)..: ",caminho)


caminho = sol.aprofundamento_iterativo(origem,destino)
print("\nAprof. Iterativo...:",caminho)

caminho = sol.bidirecional(origem,destino)
print("\nBidirecional.......: ",caminho)
"""