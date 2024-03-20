class Lista:
    def __init__(self,info=None):
        self.info= info 
        self.prox= None

def criaLista():
    return None
    
def listaInsere(lst,valor):
    novo= Lista(valor)
    novo.prox= lst
    return novo  

def listaImprime(lst):
    atual=lst
    while atual is not None:
        print(atual.info)
        atual= atual.prox

def listaVazia(lst):
    return lst is None

def listaBusca(lst,valor):
    atual= lst
    while atual is not None:
        if atual.info==valor:
            return True
        atual=atual.prox 
    return False

def listRemove(lst,valor):
    atual= lst
    if atual is None:
        return
    
    if atual.info==valor:
        lst= atual.prox
        atual= None
        return
    
    prev=None
    while atual:
        if atual.info==valor:
            break
        prev= atual
        atual=atual.prox

    if atual is None:
        return
    
    prev.prox= atual.prox 
    atual= None

def listComprimento(lst):
    cont=0
    atual=lst

    while atual:
        cont+= 1
        atual= atual.prox 
    return cont

def maiores(lst,n):
    cont= 0
    atual= lst

    while atual:
        if atual.info>n:
            cont+=1
        atual=atual.prox 

    return cont

def ultimo(lst):
    atual= lst
    if atual is None:
        return None
    
    while atual.prox: 
        atual= atual.prox 

    return atual.info

def concatenate(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    atual= l1
    while atual.prox:
        atual= atual.prox 
    atual.prox=l2

    return l1

def listInsereFinal(lst,valor):
    novoNo= Lista(valor)
    if lst is None:
        lst= novoNo
        return
    
    last= lst
    while last.prox:
        last=last.prox 
    last.prox= novoNo




def listaCalculaMedia(lst):
    if lst is None:
        return None
    
    total= 0
    cont= 0
    atual= lst

    while atual:
        total= total+atual.info
        cont+= 1
        atual= atual.prox

    return total/cont

def listAltera(lst):
    atual= lst

    while atual:
        atual.info= -atual.info
        atual= atual.prox

def listRetiraAnt(lst,v):
    if lst is None or lst.prox is None:
        return
    if lst.info==v:
        return
    
    atual=lst.prox 
    prev=lst

    while atual.prox:
        if atual.prox.info==v:
            prev.prox=atual.prox 
            return
        prev=atual
        atual=atual.prox

lst2=criaLista()
lst= criaLista()
print(listaVazia(lst))
lst=listaInsere(lst, 50)
lst=listaInsere(lst,60)
lst=listaInsere(lst,10)
lst2= listaInsere(lst2,100)
lst2= listaInsere(lst2,200)
lst2= listaInsere(lst2,300)
print("------------")
print("Números da Lista:")
listaImprime(lst)
print("------------")
print("Busca dos número na Lista:")
print(listaBusca(lst,50))
print("------------")
print(listaBusca(lst,100))
print(listRemove(lst,60))
print("------------")
print("Números da Lista:")
listaImprime(lst2)
print("------------")
print("Números da Lista:")
listaImprime(lst)
print("------------")
print(f"Número de nós da lista: {listComprimento(lst)}")
print("------------")
print(f"Números de nós maiores que n: {maiores(lst,15)}")
print("------------")
print(f"Valor do último nó: {ultimo(lst)}")
print("------------")
contLst=concatenate(lst,lst2)
print("Lista Concatenada:")
listaImprime(contLst)
print(f"Média: {listaCalculaMedia(lst)}")
print("------------")
listInsereFinal(lst,-10)
listInsereFinal(lst,-20)
listInsereFinal(lst,-30)
print("Números da Lista:")
listaImprime(lst)
listAltera(lst)
print("------------")
listaImprime(lst)
listRetiraAnt(lst,30)
print("------------")
print("Números da Lista:")
listaImprime(lst)