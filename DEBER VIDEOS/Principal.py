
from optparse import Option
from ssl import Options
from Menu import principal
from modulos.funciones_matematicas  import multiplicar, sumar
import time
import os
os.system("cls")
var = principal()
lis = ["1)","2)","3)","4)","5)","6)","7)","8) ","9)","10)","11)","12)","13)","14)","15)","16)","17)","18)","19)","20)","21)","22)","23)","24)","25)","26)","27)","28)","29)","30)","31)","32)","33)","34)","35)","36 )","37 )",]
opcion = ""
while opcion != "27":
    os.system("cls")
    opcion = var.menu(lis)
    os.system("cls")
    if opcion == "1": 
        print ("Hola Mundo")
        time.sleep(1)
    elif opcion== "2":
        os.system("cls")
        Nombre = "Flori"
        print (Nombre) 
        edad=25
        print (edad)
        edad= True
        print (edad)
        sueldo= 205.10
        print (sueldo)
        time.sleep(2)
    elif opcion == "3": 
        os.system("cls") 
        numero1 ="35"
        numero2 ="18"
        print (numero1 + numero2)
        num1 = int (numero1) 
        num2 = int (numero2)
        print (numero1 + numero2)
        sueldo = 1200.43
        sueldoEntero= int (sueldo)
        print (sueldoEntero)
        valor = "450.89"
        ValorDecimal =float (valor)
        print (ValorDecimal*3)
        edad=100
        print(len(str(edad)))
        time.sleep(1)
    elif opcion == "4":
        os.system("cls")
        entero=23
        decimal=31.78
        complejo=12+5j
        # Booleano= True
        """
        Print (entero)
        print (decimal)
        print (boleano)
        """

        num1 =20
        num2 = 4
        print("suma:", (num1+ num2))
        print("resta:", (num1- num2))
        print("multiplicacion:", (num1* num2))
        print("Division:", (num1/ num2))
        print("division exacta:", (num1// num2))
        print("Potencia:", (num1** num2))
        time.sleep(1)
    elif opcion == "5":
        os.system("cls")
        texto1 ="Hola"
        texto2 ="Mundo"
        textoFinal = texto1 + "" + texto2
        print (textoFinal)

        print("El saludo es: %s %s" % (texto1, texto2))

        SaludoFinal="saludo:{0} {1}".format (texto1, texto2)
        print (SaludoFinal)
        saludoFina12="saludo:{x} {y}".format (x=texto1, y=texto2)
        print (saludoFina12)
        time.sleep(1)
    elif opcion == "6":
        os.system("cls")
        texto = "bienveNIdos al canal de uskokrum2010"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())
        print(texto.find("al")) 
        print(texto.count("e")) 
        textoFinal = texto.replace("e", "3")
        print(textoFinal)
        valor = texto.isnumeric() 
        print(valor)
        cadenaSeparada = texto.split(" ")
        print(cadenaSeparada)
        time.sleep(1)
    
                    

    elif opcion == "7":
        os.system("cls")
    
        tupla= (1,2,3)
        print (tupla)
        tupla2 =(7, "oscar,true 4,50.1, 16+ 7j ,15,""felicidad,false")
        print (tupla)
        tupla3 =(9,3,4,5,6)
        print (tupla)
        print (tupla2 [1])

 
        print(tupla2[-1]) #Acceder al
        print (tupla2[0:4])
        print(tupla2[-2])

        a,b,c = tupla
        print (a)
        print (b)
        print (c)

        tuplafinal=tupla+tupla3
        print (tuplafinal)

        print (tuplafinal.count(21))
        print (tuplafinal.index(3))
        time.sleep(1)

    elif opcion=="8":

        os.system("cls")
        

        lista1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])        
        print(lista1[3:])

        lista1.append("UskoKruM2010")
        print(lista1)

        lista1.insert(4, "Perú")
        print(lista1)

        lista1.extend(["Alejandro", 110, False])
        print(lista1)

        print(lista1.index("Flavio"))

        lista1.remove(56.3)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = ["Chiclayo", "Irma"]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 4)

        print("UskoKruM2010" in lista1)
        time.sleep(1)
    
    
    elif opcion == "9":

        os.system("cls")
       

        miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
        print(miDiccionario["Perú"])
        print(miDiccionario)

        miDiccionario["Venezuela"] = "Caracas"
        print(miDiccionario)

        miDiccionario["España"] = "Barcelona"
        print(miDiccionario)

        del miDiccionario["España"]
        print(miDiccionario)

        dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
        print(dic2[25])

        llaves = ("España", "Francia", "Inglaterra")
        dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
        print(dicPaises)

        datosPersonales = {"Ape": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])

        print(datosPersonales.get('Apel', "Oscar"))

        print(datosPersonales.keys())
        valores = tuple(datosPersonales.values())
        print(valores)
        time.sleep (1)


    elif opcion == "10":
        os.system ("cls")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))
        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) será:", edadFutura)
        print("Tu sueldo es:", sueldo)
        time.sleep(1)

    elif opcion == "11":

        os.system("cls")
        edad=int(input ("Ingrese su edad:"))
        if edad >=18:

         print("Eres Mayor de edad.")
        elif edad==18:

         print("Tienes 18 años!")

        else:

         print("No eres mayor de edad.")
        time.sleep(1)

 

    elif opcion == "12":

        os.system("cls")

        def saludar():

            print("García")

            print("Oscar")

            print("UskoKruM2010")
            return "Hola"
        print(saludar())
        def evaluarSueldoMinimo(sueldo):

            if sueldo >= 850:
                print("Cumples con el sueldo")
            else:
                print("Ganas menos que el sueldo mínimo")
                evaluarSueldoMinimo(100)
        time.sleep(1)

    elif opcion=="13":
       os.system("cls")
    
       distancia=1200
       numerohermanos=2
       salarioPadres=1500
       tieneBeneficio=False
       if(distancia >100 and numerohermanos>2)or salarioPadres:
        tieneBeneficio=True
        print(not tieneBeneficio)
        if (5>3) and (8 < 6):
         print("Verdad")
        else:      
         print("Es mentira")
         time.sleep(1)

    elif opcion=="14":
      os.system("cls")
      """
      String sexo;
      sexo = (10 > 20) ? "Masculino" : "Femenino";
      """
      sexos = ("Hombre", "Mujer")
      posicion = True
      sexo = sexos[posicion] # Mujer
      print(sexo)
      sexo = sexos[not posicion] # Hombre
      print(sexo)
      time.sleep(1)

    elif opcion=="15":
      os.system("cls")
     
      numeros = range(5)  
      print(numeros[1])
      numeros1 = range(4, 10)  
      print(numeros1[5])
      numeros2 = range(10, 100, 8)
      print(numeros2[9]) 
      time.sleep(1)
    elif opcion=="16":
      os.system("cls")
     
      for i in range(1, 13):

        print("{0} x {1} es: {2}".format(i, i, (i * i)))
        for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
         print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
        time.sleep(1)
    elif opcion=="17":
        os.system("cls")
        print("-- Cursos --")
        print("Matematica - Biologia - Lenguaje - Ciencias")

        curso = input("Ingrese el curso deseado: ")

        if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
         print("Curso {0} seleccionado.".format(curso))
        else:
         print("No existe ese curso...")
         time.sleep(1)
    elif opcion=="18":
        os.system("cls")
        
        numero = int(input("Ingrese un número: "))
        factorial = 1
        for n in range(1, (numero + 1)):
            factorial = factorial * n
        print("El factorial de {0} es: {1}".format(numero, factorial))
        time.sleep(1)

    elif opcion=="19":
        os.system("cls")


        """
        indice = 1
        while indice < 10:
        print("Valor actual: {0}".format(indice))
        indice = indice + 1
        print("Hemos terminado el bucle while.")
        # Continua el programa.
        """

        inicio = 2
        while inicio <= 100:
            print("Número par: {0}".format(inicio))
            inicio += 2
            print("Hemos terminado el bucle while.")
            time.sleep(1)


    elif opcion=="20":
        os.system("cls")
     

        """
        for numero in range(1, 6):
        if numero == 3:
        break  # Descanso o interrupción en este punto.
        print("El número es: {0}".format(numero))
        print("Bucle terminado.")
        """

       

        """
        for numero in range(1, 6):
        if numero == 3:
        continue  # Continúa con el resto del bucle.
        print("El número es: {0}".format(numero))
        print("Bucle terminado.")
        """
   
        for numero in range(1, 6):
            if numero <= 3:
        
             pass
        else:
          print("El siguiente valor es mayor a 3:")
          print("El número es: {0}".format(numero))
          print("Bucle terminado.")
          def funcionSinImplementar():
           pass
        time.sleep(1)

    elif opcion=="21":
        os.system("cls")
        

        """
        def generaMultiplos7(limite):
        numero = 1
        listaNumeros = []
        while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
        return listaNumeros  # Retorna toda la lista creada.
        print(generaMultiplos7(10))
        """
        def generadorMultiplos7(limite):

            numero = 1
            while numero <= limite:
                yield numero * 7  
                numero = numero + 1
        obtieneMultiplos7 = generadorMultiplos7(10)
        """
         print(obtieneMultiplos7)
        for n in obtieneMultiplos7:
        print(n)
        """
        
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de código...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de código...")
        print(next(obtieneMultiplos7))

        time.sleep(1)

    elif opcion=="22":
        os.system("cls")
       
        """
        def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
        yield leng
        """
        def devuelveLenguajes(*lenguajes):
         for leng in lenguajes:
          yield from leng
        lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        time.sleep(1)
    elif opcion=="23":
        os.system("cls")
        
        numero1 = 20
        numero2 = 2
        try:
            resultado = numero1 / numero2
            # except:
        except ZeroDivisionError:
         print("No se puede dividir entre 0...")
        finally:
            print("Yo siempre aparezco.")
            print("Aquí termina mi programa.")
            time.sleep(1)

    elif opcion=="24":
        os.system("cls")
        def evaluarNota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto...")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")
        evaluarNota(-7)
        print("Este es el fin de mi programa.")
        time.sleep(1)

    elif opcion=="25":
        os.system("cls")
        print("LA SUMA ES:{}".format(sumar(5, 6)))
        print("LA MULTIPLICACION ES:{}".format(multiplicar(5, 6)))
        time.sleep(1)
    
    elif opcion=="26":
        os.system("cls")
        class Persona():
            apellidos = ""
            nombres = ""
            edad = 0
            despierta = False
            def despertar(self):

               self.despierta = True
               print("Buen día.")

        persona1 = Persona()

        persona1.apellidos = "García Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)
        persona2 = Persona()
        persona2.apellidos = "Paz Torres"
        print(persona2.apellidos)
        print(persona2.despierta)
        time.sleep(1)

    elif opcion=="27":
        os.system("cls")
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)

        curso2 = Curso("Lenguaje", 5, "Ingeniera en Software")
        print(curso2.nombre)
        time.sleep(1)
    elif opcion=="28":
        os.system("cls")

        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)
        curso1.mostrar()
        time.sleep(1)
    elif opcion=="29":
        os.system("cls")
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))
                docenteAsignado = selfs.__verificardocente()
                if docenteAsignado:
                    print("Docente Asignado")
                else:
                    print("No es necesario asignar docente")

            def __verificardocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False
        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)
        curso1.mostrar()
        time.sleep(1)
        time.sleep(1)
    elif opcion==("30"):
        os.system("cls")
        class cuenta():
            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            
            def get_Saldo(self):
                return self.__saldo

            def get_propietario(self):
                return self.__propietario

            def get_moneda(self):
                return self.__moneda

 

            def set_moneda(self, moneda):
                self.__moneda = moneda

        cuenta1 = cuenta("Andy Contreras", 8000, "dólares")
        print(cuenta1.get_Saldo())
        cuenta1.set_moneda("soles")
        print(cuenta1.get_moneda())
        time.sleep(1)

    elif opcion =="31":
        os.system("cls")
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))
                docenteAsignado = selfs.__verificardocente()
                if docenteAsignado:
                    print("Docente Asignado")
                else:
                    print("No es necesario asignar docente")

            def __verificardocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "Nombre: {} - Créditos: {}"
                return texto.format(self.nombre, self.creditos)


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1)
        curso1.mostrar()
        time.sleep(1)
    elif opcion=="32":
        os.system("cls")
        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro


        estu1 = estudiantes("Torres", "Lopez", "Juan", "Ingeniería Civil")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        time.sleep(1) 
        time.sleep(1)

    elif opcion=="33":
        os.system("cls")
        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesion {}".format(self.profesion))


        estu1 = estudiantes("Torres", "Lopez", "Juan", "Ingeniería Civil")
        estu1.datos()
        time.sleep(1)
    elif opcion=="34":
        os.system("cls")

        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesion {}".format(self.profesion))


        estu1 = estudiantes("Torres", "Lopez", "Juan", "Ingeniería Civil")
        print(isinstance(estu1, estudiantes))
        per1 = persona("Torres", "Lopez", "Juan")
        print(isinstance(per1, estudiantes))
        time.sleep(1)


        time.sleep(1)
    elif opcion =="35":
        os.system("cls")
        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2


        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class claseX(ClaseA, ClaseB):
            pass
        cX1 = claseX(15, 21)
        time.sleep(1)

    elif opcion =="36":
        os.system ("cls")
        class Estudiante():
            def describir(self):
                print("Soy un buen estudiante.")


        class docente():
            def describir(self):
                print("Me dedico a enseñar curso.")


        class trabajador():
            def describir(self):
                print("Trabajo dentro de una gran empresa.")


        def describirPersona(persona):
            persona.describir()


        doc1 = docente()
        describirPersona(doc1)
        time.sleep(1)
    elif opcion=="37":
        os.system("cls")
        class Pais():

            def __init__(self, nom, pre):

                self.nombre = nom
                self.presidente = pre

            def __str__(self):

                txt = "Pais: {} - Presidente: {} "
                return txt.format(self.nombre, self.presidente)


        class ciudad():
            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitante = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad: {} - Nº Habitantes: {} ({}) "
                return txt.format(self.nombre, self.habitante, self.pais)


        class Urbanizacion():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización: {} ({})"
                return txt.format(self.nombre, self.ciudad)
        pais1 = Pais("Perú", "Martín Vizcarra")
        print(pais1)

        ciudad1 = ciudad("Chiclayo", 150000, pais1)
        print(ciudad1)

        urbanizacion1 = Urbanizacion("María de los Angeles", ciudad1)
        print(urbanizacion1)
        time.sleep(1)


      
