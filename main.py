from Assembler import Assembler
from Memoria import Memoria
from MotorDeEventos import MotorDeEventos

def main():
    teste = './teste.txt'
    compMemoria = Memoria()
    motor = MotorDeEventos()
    assembler = Assembler()

    programCounter = motor.programCounter

    assembler.primeiroPasso(teste)
    instruCodMaq = assembler.segundoPasso(teste)
    
    compMemoria.loader(instruCodMaq) 
        
    motor.acumulador = 5
    
    compMemoria.memoria[200] = '0x0002'
    
    compMemoria.memoria[210] = '0x0003' 
    
    compMemoria.memoria[220] = '0x0005' 
    
    compMemoria.memoria[100] = 7
    
    

    #compMemoria.memoria[130] = 2
        
    motor.fluxoEventos(compMemoria)
    
    print()
    print("Acumulador:")
    print(motor.acumulador)
    print()
    print("Posição 0x100 da memória:")
    print(compMemoria.memoria[100])
    print()
    print("Memoria:")
    print(compMemoria.memoria)
    

main()



