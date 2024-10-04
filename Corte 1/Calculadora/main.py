# Paola Andrea Herrera 20162005881
# --- CALCULADORA PRIMER CORTE ---

import operaciones
while True:
        menu = operaciones.Menu()
        menu.showOptions()

        option = menu.chooseOption()

        if option == 1:
                object1 = operaciones.Enter_Data()
                a = object1.enterA()
                b = object1.enterB()

                object1 = operaciones.Add_Sub()
                print(f"Resultado: {object1.add(a, b)}")
                time.sleep(1)

        if option == 2:
                object1 = operaciones.Enter_Data()
                a = object1.enterA()
                b = object1.enterB()

                object1 = operaciones.Add_Sub()
                print(f"Resultado: {object1.sub(a, b)}")
                time.sleep(1)

        if option == 3:
                object1 = operaciones.Enter_Data()
                a = object1.enterA()
                b = object1.enterB()

                object1 = operaciones.Mult_Div()
                print(f"Resultado: {object1.mult(a, b)}")
                time.sleep(1)

        if option == 4:
                object1 = operaciones.Enter_Data()
                a = object1.enterA()
                b = object1.enterB()

                object1 = operaciones.Mult_Div()
                print(f"Resultado: {object1.div(a, b)}")
                time.sleep(1)

        if option == 5:
                object1 = operaciones.Enter_Data()
                a = object1.enterA()

                object1 = operaciones.Square(a)
                print(f"Resultado: {object1.getValue()}")
                time.sleep(1)
