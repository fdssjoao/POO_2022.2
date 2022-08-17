print("joão Felipe Dos Santos Sousa")
print("2020111MTDS0204")
print("TDS--286")
"""1. Utilizando a linguagem python, implemente a classe carro de acordo com as especificações
vistas em
sala de aula:
Métodos:
ligar() : este método deverá mudar o estado do carro para: “ligado” e imprimir este estado.
Desligar(): este método deverá mudar o estado do carro para: “desligado” e o carro deve
parar, para isto
você deverá chamar o método parar(). Imprimir o estado do carro.
Parar(): este método deverá mudar a velocidade atual do carro para 0 (zero). Imprimir a
mensagem: “carro parado”.
Acelerar(valor): este método deverá mudar a velocidade atual do carro para o valor que está
no
parâmetro. O carro só pode acelerar se ele estiver ligado (fazer a condição). Fazer a condição
para que a
velocidade atual não ultrapasse a velocidade máxima do carro. Imprimir a velocidade atual do
carro.
Crie 2 objetos do tipo carro.
O primeiro objeto tem os seguintes valores:
i. nome: fusca
ii. Ano: 1965
iii. Cor: Preto
iv. Veloc_max: 80
v. Veloc_.atual:20
vi. Estado: ligado
O segundo objeto tem os seguintes valores:
I. Nome: Ferrari_sr2000
II. Ano: 2014
III. Cor: vermelho
IV. Veloc.max: 300
V. Veloc.atual: 0

VI. Estado: desligado
Execute os objetos, invocando os métodos necessários de acordo como que se pede:
a) Acelere o fusca para a velocidade: 40
b) Acelere a ferrari para a velocidade: 200
c) Desligue o fusca
d) Ligue a ferrari
e) acelere a ferrari para: 320
f) Pare a ferrari.
g) Desligue a ferrari
h) Ligue o fusca
i) Acelere o fusca para: 100
j) Desligue o fusca"""
class Carro:
    nome= None
    ano= None
    cor= None
    velocidade_maxima= None
    velocidade_atual=None 
    estado= None

    def ligar(self):
        self.estado="ligado"
        print(f"O veículo está ligado!!")
        
    
    def parar(self):
        self.velocidade_atual=0
        print("veículo Parado!!")
        
    
    def desligar(self):
            Carro.parar(self)
            self.estado="desligado"
            print("Veículo desligado!!")
        
    def acelerar(self,velocidade):
        if self.estado=="ligado" and self.velocidade_atual<self.velocidade_maxima:
            self.velocidade_atual=self.velocidade_atual+velocidade
            print("O veículo está :",self.velocidade_atual,"km por hora")
        else:
            print("Não foi possivel acelerar!!")

#CARREGANDO OS OBJETOS
meu_fusca=Carro()
minha_ferrari=Carro()
#O primeiro Objeto 
meu_fusca.nome= "fusca"
meu_fusca.ano= 1965
meu_fusca.cor= "Preto"
meu_fusca.velocidade_maxima= 80
meu_fusca.velocidade_atual=20
meu_fusca.estado="ligado"
#O segundo objeto tem os seguintes valores:
minha_ferrari.nome= "Ferrari_sr2000"
minha_ferrari.ano= 2014
minha_ferrari.cor="vermelho"
minha_ferrari.velocidade_maxima= 300
minha_ferrari.velocidade_atual= 0
#a) Acelere o fusca para a velocidade: 40
print("A)")
meu_fusca.acelerar(40)
print("_"*100)
#b) Acelere a ferrari para a velocidade: 200
print("B)")
minha_ferrari.acelerar(200)
print("_"*100)
#c) Desligue o fusca
print("C)")
meu_fusca.desligar()
print("_"*100)
#d) Ligue a ferrari
print("D)")
minha_ferrari.desligar()
print("_"*100)
#e) acelere a ferrari para: 320
print("E)")
minha_ferrari.acelerar(320)
print("_"*100)
#f) Pare a ferrari.
print("F)")
minha_ferrari.parar()
print("_"*100)
#g) Desligue a ferrari
print("G)")
minha_ferrari.desligar()
print("_"*100)
#h) Ligue o fusca
print("H)")
meu_fusca.ligar()
print("_"*100)
#i) Acelere o fusca para: 100
print("I)")
meu_fusca.acelerar(100)
print("_"*100)
#j) Desligue o fusca
print("J)")
meu_fusca.desligar()
print("_"*100)


print("_-_"*100)
print("_-_"*100)
print("_-_"*100)
        
    
"""#Exemplo da classe Gato
Complete a classe Gato com os seguintes métodos/atributos:
adicionar os atributos:
-sexo (valores permitidos: M/F)
-fertil (True/False)
-cio (True/False)
-prenhe (True/False)
-puerpério (True/False)

MÉTODOS:
engordar() -> recebe um valor como argumento e adiciona este valor ao atributo peso atual do
objeto gato.
envelhecer -> Não possui argumentos. Aumenta em uma unidade o atributo idade do objeto
gato. Gatos se tornam férteis a partir de 1 ano de idade.
entrar_no_cio() -> muda o estado cio para: True. Somente para Fêmeas (F) e para idade >=1.
cruzar() -> recebe como atributo um objeto Gato como argumento. O sexo do objetos
envolvidos devem ser opostos. A Fêmea tem que estar no cio (cio==True) para poder cruzar.
Alterar o atributo prenhe da Fêmea para True em caso de sucesso.

parir() - Somente para Fêmeas que estão em estado prenhe==True. Cada parto gera um novo
gato. Mudar o estado puerpério para True. Enquanto o gato (Fêmea) estiver no puerpério não
pode cruzar."""

class Gato:
    raca=None
    nome=None
    peso=None
    idade=None
    sexo=None
    fertil=None
    cio=None
    prenche=None
    puerperio=None
    filhotes=None
    
#Definindo as funções da classe gato:
    
    def mudar_nome(self,nome):
        print("O nome anterior é: ",self.nome)
        self.nome=nome  
        print("o nome agora é :",self.nome)
    def engordar(self,kilos):
        print(f"O peso anterior é: {self.peso}")
        self.peso+=kilos
        print(f"O peso atual de {self.nome} é: {self.peso}")
    def envelhecer(self):
        print("a idade anterior é: ",self.idade,"/-------/","o estado fertil: ",self.fertil)
        self.idade=self.idade+1
        if self.idade >=1 :
            self.fertil=True
            print("A idade atual é : ",self.idade)
        else:
            print("não foi possivel envelhecer!!")
        
    def entrar_no_cio(self):
        print("o estado anterior é cio:",self.cio,"/------/ fertil: ",self.fertil)
        if self.sexo=="F" and self.idade >= 1 :
            self.cio=True
            self.fertil=True
            print("o estado atual é cio:",self.cio," fertil: ",self.fertil)
        else:
            print(f"{self.nome} não está no cio!!")
    
    
    def cruzar(self,animal2):
        sexo_do_parceiro=animal2.sexo
        if sexo_do_parceiro!=self.sexo and self.cio==True  and self.fertil==True and self.puerperio==False:
            print(animal2.nome," está cruzando com ",self.nome ,"!!")
            self.prenche=True
            print("tá gravida!!")
        else:
            print("Não foi possivel cruzar!!")
    
        
        
    def parir(self,novo_nome):
        if self.prenche==True and self.sexo=="F":
            self.cio==True
            self.fertil==True
            self.puerperio=True
            print(f"A {self.nome} está tendo filhotes !!")
            identidade=novo_nome
            novo_nome=Gato()
            novo_nome.nome=identidade
            print(f" nasceu, {novo_nome.nome} criado")
            self.filhotes+=1
            meu_felino.filhotes+=1
        else:
            print(f"Não foi possivel gerar filhotes para {self.nome}!!")
#Definindo os parametros do primeiro animal    

minha_felina=Gato()
minha_felina.raca="amerians"
minha_felina.nome="Luna"
minha_felina.peso=1
minha_felina.idade=2
minha_felina.sexo="F"
minha_felina.fertil=True
minha_felina.cio=False
minha_felina.prenche=False
minha_felina.puerperio=False
minha_felina.filhotes=0

#Definindo os parametros do segundo animal
meu_felino=Gato()
meu_felino.raca="cansas"
meu_felino.nome="Frederico"
meu_felino.peso=3
meu_felino.idade=2
meu_felino.sexo="M"
meu_felino.fertil=True
meu_felino.cio=True
meu_felino.prenche=False
meu_felino.puerperio=False
meu_felino.filhotes=0

#Chamando as funções 
print("testando mudar o nome dos animais: ")
print("#"*10)
minha_felina.mudar_nome("MELISSA")
print("#"*10)
meu_felino.mudar_nome("CHICÃO")
print("_"*100)
print("testando mudar o peso dos animais: ")
print("#"*10)
minha_felina.engordar(2)
print("#"*10)
meu_felino.engordar(1)
print("_"*100)
print("testando envelhecer os animais: ")
print("#"*10)
minha_felina.envelhecer()
print("#"*10)
meu_felino.envelhecer()
print("_"*100)
print("testando colocar a fêmea no cio: ")
print("#"*10)
minha_felina.entrar_no_cio()
print("#"*10)
print("tentando bugar o macho e colocar ele no cio: ")
meu_felino.entrar_no_cio()
print("_"*100)
print("tstando colocar os animais para cruzar: ")
print("#"*10)
minha_felina.cruzar(meu_felino)
print("#"*10)
meu_felino.cruzar(minha_felina)
print("_"*100)
print("testando o nascer de novos individuos: ")
print("#"*10)
minha_felina.parir(str(input("digite o nome: ")))
print("#"*10)
minha_felina.parir(str(input("digite o nome: ")))
print("#"*10)
minha_felina.parir(str(input("digite o nome: ")))
print("#"*10)
print("testando o bug do individuo macho que nao pode ter filhos: ")
meu_felino.parir("melkzedek")
print("_"*100)

#imprimindo o resultado do parto e os individuos 
print("_"*10)
print("nome: ",minha_felina.nome,"-------peso: ",minha_felina.peso,"------sexo: ","/",minha_felina.sexo,"/","-------Filhotes: ",minha_felina.filhotes)
print("nome: ",meu_felino.nome,"-------peso: ",meu_felino.peso,"------sexo: ","/",meu_felino.sexo,"/","-------Filhotes: ",meu_felino.filhotes)
print("_"*10)
print(meu_felino.nome)
print("_"*10)

#joão Felipe Dos Santos Sousa
#2020111MTDS0204
#TDS--286


            
        
            
        
        
        