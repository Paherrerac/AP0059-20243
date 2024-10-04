class Menu:
    def showOptions(self):
        print("\n--- Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
      
    def chooseOption(self):
        option = int(input("Seleccione la operación: "))
        return option

class Enter_Data:
    def enterA(self):
        a = int(input("Digite un valor: "))
        return a
    
    def enterB(self):
        b = int(input("Digite otro valor: "))
        return b
    
class Add_Sub:
    def add(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b

class Mult_Div:
    def mult(self, a, b):
        return a*b
    
    def div(self, a, b):
        return a/b
    

