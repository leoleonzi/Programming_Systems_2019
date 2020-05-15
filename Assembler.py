import regex as re
import sys

class Assembler:
    def __init__(self):
        self.tabelaDeSimbolos = []

    def leitura(self,arquivo):
        f=open(arquivo, "r")
        f1 = f.readlines()
        instrucoes = []
        for x in f1:
            instrucoes.append(x)            
        return instrucoes

    def primeiroPasso(self,arquivo):
        ehRotulo = 0
        instrucoes = self.leitura(arquivo)
        for numInstrucao in range (len(instrucoes)): 
            #Separa os termos da instrução e guarda num array de strings
            self.instr = re.findall(r"[^,.:;' ]+|[,.:;' ]", instrucoes[numInstrucao])
            if (self.instr[0] != ' '):
                ehRotulo = 1
                self.tabelaDeSimbolos.append([self.instr[0], numInstrucao, ehRotulo]) #montagem tabela de simbolos 
            elif(self.instr[0] == ' '):
                self.tabelaDeSimbolos.append([self.instr[2], numInstrucao, ehRotulo])
        

        encontrouSimbolo = False  
        for i in range (len(self.tabelaDeSimbolos)):
            if (self.tabelaDeSimbolos[i][2]==0): #não eh rótulo
                if (self.tabelaDeSimbolos[i][0] == 'JP' or self.tabelaDeSimbolos[i][0]  == 'J'): 
                    encontrouSimbolo = True    

                elif (self.tabelaDeSimbolos[i][0] == 'JZ' or self.tabelaDeSimbolos[i][0]  == 'Z'): 
                    encontrouSimbolo = True    

                elif (self.tabelaDeSimbolos[i][0] == 'JN' or self.tabelaDeSimbolos[i][0]  == 'N'): 
                    encontrouSimbolo = True    

                elif (self.tabelaDeSimbolos[i][0] == 'CN' or self.tabelaDeSimbolos[i][0]  == 'C'): 
                    encontrouSimbolo = True    

                elif (self.tabelaDeSimbolos[i][0] == '+'): 
                    encontrouSimbolo = True    

                elif (self.tabelaDeSimbolos[i][0] == '-'): 
                    encontrouSimbolo = True  

                elif (self.tabelaDeSimbolos[i][0] == '*'): 
                    encontrouSimbolo = True

                elif (self.tabelaDeSimbolos[i][0] == '/'): 
                    encontrouSimbolo = True     

                elif (self.tabelaDeSimbolos[i][0] == 'LD' or self.tabelaDeSimbolos[i][0]  == 'L'): 
                    encontrouSimbolo = True 

                elif (self.tabelaDeSimbolos[i][0] == 'MM' or self.tabelaDeSimbolos[i][0]  == 'M'): 
                    encontrouSimbolo = True 
        
                elif (self.tabelaDeSimbolos[i][0] == 'SC' or self.tabelaDeSimbolos[i][0]  == 'S'): 
                    encontrouSimbolo = True 
                
                elif (self.tabelaDeSimbolos[i][0] == 'OS' or self.tabelaDeSimbolos[i][0]  == 'O'): 
                    encontrouSimbolo = True 

                elif (self.tabelaDeSimbolos[i][0] == 'IO' or self.tabelaDeSimbolos[i][0]  == 'I'): 
                    encontrouSimbolo = True 

                elif(self.tabelaDeSimbolos[i][0] == '@'):
                    encontrouSimbolo = True

                elif(self.tabelaDeSimbolos[i][0] == '#'):
                    encontrouSimbolo = True

                elif(self.tabelaDeSimbolos[i][0] == '$'):
                    encontrouSimbolo = True

                elif(self.tabelaDeSimbolos[i][0] == 'K'):
                    encontrouSimbolo = True

                if (encontrouSimbolo == False):
                    print("Erro: Instrução inválida")
                    sys.exit() #parar sistema

    def segundoPasso(self, arquivo):
        instrucoes = self.leitura(arquivo)
        instruCodMaq = [0]*4097
        for numInstrucao in range (len(instrucoes)): 
            self.instr = re.findall(r"[^,.:;' ]+|[,.:;' ]", instrucoes[numInstrucao]) #Separo os termos da instrução e guardo num array de strings
            self.tipoInstr = self.instr[2]

            if (self.tipoInstr == 'JP' or self.tipoInstr == 'J'): #JP yxxx
                comando = '0x0'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'JZ' or self.tipoInstr == 'Z'): #JP if acum = 0
                comando = comando = '0x1'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'JN' or self.tipoInstr == 'N'): #JP if acum<0
                comando = '0x2'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'CN' or self.tipoInstr == 'N'): #Controle
                comando = comando = '0x3'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '+'):
                comando = '0x4'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '-'):
                comando = '0x5'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '*'):
                comando = '0x6'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '/'):
                comando = '0x7'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'LD' or self.tipoInstr == 'L'):
                comando = '0x8'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'MM' or self.tipoInstr == 'M'):
                comando = '0x9'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'SC' or self.tipoInstr == 'S'):
                comando = '0xa'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando
                
            elif (self.tipoInstr == 'OS' or self.tipoInstr == 'O'):
                comando = '0xb'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == 'IO' or self.tipoInstr == 'I'):
                comando = '0xc'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '?' or self.tipoInstr == '?'):
                comando = '0xd'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '@'):
                comando = '@0x'+ str(self.instr[4])
                instruCodMaq[numInstrucao] = comando

            elif (self.tipoInstr == '#'):
                comando = '#'
                instruCodMaq[numInstrucao] = comando
        
        return instruCodMaq
            

            