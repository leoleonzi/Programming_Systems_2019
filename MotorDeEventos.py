import regex as re
from Memoria import Memoria

class MotorDeEventos:
    def __init__(self):
        #"Declarando:"
        self.programCounter = 0 # Representa o PC e está em numero inteiro decimal do número do Byte
        #self.tipoInstr
        #self.operando1
        #self.operando2
        self.acumulador = 0  # Acumulador em hexadecimal
        self.endRetorno = 0

    def fluxoEventos(self,memoria):
        instrAtual = memoria.fetch(self.programCounter)
        if (str(instrAtual)[0]=='@'):
            self.programCounter += 1       
            instrAtual = memoria.fetch(self.programCounter)
            while ((str(instrAtual)[0] != '#') and (instrAtual != 0)):
                if (str(instrAtual)[2] == '0'): # É um Jump  
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5]) # '4'+'0'+'0'  = 400
                    self.programCounter = endereco
                
                elif (str(instrAtual)[2] == '1'): # Jump if zero
                    if (self.acumulador == 0):
                        endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                        self.programCounter = endereco
                    else:
                        self.programCounter += 1                        
                
                elif (str(instrAtual)[2] == '2'): # Jump if negative
                    if (self.acumulador < 0):
                        endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                        self.programCounter = endereco 
                    else:
                        self.programCounter += 1
        
                elif (str(instrAtual)[2] == '3'): # instrucoes de controle
                    #if (instrAtual[3] == '0'):
                        #fazer algo
                    #elif (instrAtual[3] == '1'):
                        #fazer algo...
                    self.programCounter += 1
        
                elif (str(instrAtual)[2] == '4'): # add
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    self.acumulador = self.acumulador + memoria.memoria[endereco]
                    self.programCounter += 1
        
                elif (str(instrAtual)[2] == '5'): # sub
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    self.acumulador = self.acumulador - memoria.memoria[endereco]
                    self.programCounter += 1
        
                elif (str(instrAtual)[2] == '6'): # mult
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    self.acumulador = self.acumulador * memoria.memoria[endereco]
                    self.programCounter += 1
                
                elif (str(instrAtual)[2] == '7'): # div
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    self.acumulador = self.acumulador / memoria.memoria[endereco]
                    self.programCounter += 1
                
                elif (str(instrAtual)[2] == '8'): # load from memory
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    self.acumulador = memoria.memoria[endereco]
                    self.programCounter += 1
        
                elif (str(instrAtual)[2] == '9'): #move to memory
                    endereco = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                    memoria.memoria[endereco] = self.acumulador
                    self.programCounter += 1
        
                elif (str(instrAtual)[2] == 'a'):   #SUBROUTINE CALL
                    self.endRetorno = self.programCounter + 1
                    self.programCounter = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
        
                elif (str(instrAtual)[2] == 'b'): #Fazer as 16 chamadas do sistema operacional
                    self.programCounter += 1
        
                elif (str(instrAtual)[0] == '@'):
                    self.programCounter = int(instrAtual[3]+instrAtual[4]+instrAtual[5])
                
                elif (str(instrAtual)[0] == '#'):
                    self.programCounter = 1 #fim do programa
                    
                instrAtual = memoria.fetch(self.programCounter)


            print("FIM DO PROGRAMA")

