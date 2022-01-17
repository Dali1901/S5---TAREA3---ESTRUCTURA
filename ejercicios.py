class ejercicios:

    def video_variables (self):
        print("***** VARIBALES ****")
        print("\n¿Que guarda la variable X en cada uno de los siguientes casos?")
        print("\n***** Caso 1 *****")
        X =  46
        X = 15
        x = 30
        print("X = 46\nX = 15\nx = 30")
        print("La variable X es igual a: ", X,"\n")
        print("\n***** Caso 2 *****")
        X =  10*2
        X -= 5
        print("X = 10*2\nX -= 5")
        print("La variable X es igual a: ", X,"\n")
        print("\n***** Caso 3 *****")
        X =  10-2
        10 + 2
        print("X = 10-2\n10 + 2")
        print("La variable X es igual a: ", X,"\n")
        print("\n***** Caso 4 *****")
        Y =  3*(4+2)
        X = Y + 2
        Z = 5
        X = Y-Z
        print("X = 3*(4+2)\nX = Y + 2\nz = 5\nX = Y- Z")
        print("La variable X es igual a: ", X,"\n")
        print("\n***** Caso 5 *****")
        X =  25
        X + 10
        print("X = 25\nX + 10")
        print("La variable X es igual a: ", X,"\n")
        print("\n***** Caso 6 *****")
        X = 3
        Y = X+6
        X = Y-1
        print("X = 3\nY = X + 6\nX = Y - 1")
        print("La variable X es igual a: ", X,"\n")
        
    def video_tipodedatos(self):
        print("***** TIPOS DE DATOS ****")
        print("\n¿De qué tipo es cada uno de los siguientes datos?\n")
        print ("100/5 es de tipo: ",type(100/5))
        print ("7/2 es de tipo: ",type(7/2))
        print ("7//2 es de tipo: ",type(7//2))
        print ("7%2 es de tipo: ",type(7%2))
        print ("'a' es de tipo: ",type('a'))
        print ("'tiza' + '.' es de tipo:" ,type("tiza" + "."))
        print ("'hola'[1+1] es de tipo: ",type("hola"[1+1]))
        print ("len('hola') es de tipo: ",type(len("hola")))
        print ("int('145') es de tipo: ",type(int("145")))
        print ("float('145') es de tipo: ",type(float("145")))
        print ("str(32) es de tipo: ",type(str(32)))
        print ("1+2!=3 es de tipo: ",type(1+2!=3))
        print ("177%2==0 es de tipo: ",type(177%2==0))
        print ("len('nube') <= 20 es de tipo: ",type(177%2==0))
        print("\n¿Qué guardan las variables luego de cada operación?\n")
        print("n= 167/10\nn=", 167/10,"\n")
        print("n= 167//10\nn=", 167//10,"\n")
        print("n= 167%10\nn=", 167%10,"\n")
        print("letra = 'a'")
        letra = "a"
        print("letra =",letra,"\n")
        print("saludo = 'hola' + letra")
        saludo = "hola" + letra
        print("saludo =", saludo,"\n")
        print("C = saludo[0]\nC=", saludo[0],"\n")
        print("C = saludo[1+3]\nC=", saludo[1+3],"\n")
        print("L=len(saludo)")
        L = len(saludo)
        print("L =", L,"\n")
        print("C=saludo[len(saludo)-1]")
        C = saludo[len(saludo)-1]
        print("C =", C)
        print("\nmenor = 'a' < 'b'")
        menor = "a" < "b"
        print("menor = ", menor)
        print("\nD=1!=1")
        D=1!=1
        print("D =", D)
        print("\nD='cinta' >= 'canto'")
        D = "cinta" >= "canto"
        print("D =", D)
        print("\nc='z'+'a'+'paz'[0]")
        c ='z'+'a'+'paz'[0]
        print("c =", c)
        print("x=c[0] == 'z'")
        x=c[0]=="z"
        print("x = ", x)
        print("\n¿Cuáles de las siguientes operaciones arrojan error?\n")
        print("11-(4%2+10) ---> No da error")
        print("'30' + 2 ---> Da error")
        print("'30' + '2' ---> No da error")
        print("'hola'[len('hola')] ---> Da error ")
        print("len 124 ---> Da error")
        print("'hola'['fin')] ---> No da error")
        print("'hola'[11-(4%2+10)] ---> No da error")
        print("int('4') ---> No da error")
        print("int(4) ---> No da error")
        print("'z' ---> Da error")
        print("int(4.) ---> Da error")
        print("4<'f ---> Da error")
        print("'palabra' = 'rama' ---> Da error")
        print("'palabra' == 'rama' ---> No da error")

    def video_tablas (self):
        print("***** TABLAS DE VERDAD ****")
        print("\n¿Que resultados (True/False) dan las siguientes operaciones?\n")
        x = not True
        print("not True = ", x)
        x = not(1+2!=3)
        print("not(1+2!=3) = ", x)
        x = (len("jugar")>5) and (len("jugar")<10)
        print("x = (len('jugar')>5) and (len('jugar')<10) =",x)
        y = "alto"[2] == "t" and x
        print("'alto'[2] == 't' and x = ", y)
        print("842913%10!=3 and len('cafe') == 3 =",842913%10!=3 and len('cafe') == 3)
        print("0!=0 or 'a' < 'y' =", 0!=0 or 'a' < 'y')
        print("True or int('50')>= 50 = ",True or int('50')>= 50 )
        edad=20
        print("edad=20\nnot(x) or edad%2==0 =", not(x) or edad%2==0)
        es_cliente = False
        print("es_cliente=False\nnot (es_cliente and not(edad<18)) = ", not (es_cliente and not(edad<18) ))
        print("\n¿Qué errores tienen estas proposiciones?¿Cómo deben corregirse?\n")
        print("El número no puede ser menor que 0 ni mayor que 100.\nnúmero<0 and número>100\nCorrección: número>=0 and número<=100\n")
        print("La edad debe estar entre 10 y 20.\nedad>10 and <20\nCorrección: edad>=10 and edad<=20\n")
        print("La longitud de la cadena no debe ser superior a 10 caracteres.\nlen(cadena)<10\nCorreción: len(cadena)<=10")
        print("\n¿Cómo expresarías las siguientes operaciones?. Suponer la existencia de variables conteniendo los datos necesarios\n")
        print("1. El número es múltiplo de 4 también es negativo.\nR = num%4==0 and num<0\n")
        print("2. Decidiste comprar un auto usado, pero debe cumplir ciertas condiciones: El kilometraje debe ser menor a 30000 y el modelo de estar entre 2015 y 2017.\nR = km<30000 and (modelcar>=2015 and modelcar<=2017)\n")
        print("3. Una agrupación académica tiene ciertos requisitos para cualquier estudiante que desea ingresar:")
        print("Debes tener mas del 30% de sus estudios completos y no debe ser miembro de otra agrupación académica de la misma universidad\nR = porcen_estudios>30 and not(miembro_agrup)\n")
        print("4. Una persona paa frío si es invierno y además no tiene calefacción ni está abrigada\nes_invierno = True\nR = es_invierno and not(calefaccion) and not(abrigada)")
    
    def video_string (self):
        print("***** STRINGS *****")
        print("\n1. cadena='si, profe, es cierto... yo me comí la tarea'")
        cadena="si, profe, es cierto... yo me comí la tarea"
        print("\n¿Cuál es elresultado?")
        x = cadena[10]
        print("\ncadena[10]\ncadena = ", x)
        x = cadena[-1]
        print("\ncadena[-1]\ncadena = ", x)
        x = cadena[0:9]
        print("\ncadena[0:9]\ncadena = ", x)
        x = cadena[::3]
        print("\ncadena[::3]\ncadena = ", x)
        print("\n¿Cómo obtener?")
        print("\nLa cadena al revés es: 'aerat al ímoc em oy ...otreic se ,eforp ,ís'\nR = cadena[::-1]")
        print("\nLa subcadena 'profe'\nR = cadena[4:9]")
        print("\n2. Dada la variable s='   hola, ¿cómo estás?' con 3 espacios al inicio, ¿qué se obtiene en cada una de las siguientes operaciones?")
        s='   hola, ¿cómo estás?'
        x = s[::-1]
        print("\ns[::-1]\ns = ", x)

        #x = s[len(s)]
        print("\ns[len(s)]\ns = Da error, correción: s[len(s)-1] ")
        x = s.count("o")
        print("\ns.count('o')\ns = ", x)
        x = s.count("Hola")
        print("\ns.count('Hola'')\ns = ", x)
        x = s[-4:]
        print("\ns[-4:]\ns = ", x)
        x = s[15:]
        print("\ns[15:]\ns = ", x)
        x = s.find("o")
        print("\ns.find('o')\ns = ", x)
        x = s.strip()
        print("\ns.strip()\ns = ", x)
        x = s.upper()
        x = x == s
        print("\nx = s.upper()\nx == s\ns = ", x)
        x = s[14:].upper()
        print("\ns[14:].upper()\ns = ", x)
        x = len(s)%2!=0
        print("\nlen(s)%2!=0\ns = ", x)
        x = s.replace(" ", "*")
        print("\ns.replace(' ', '*')\ns = ", x)
        x = s.replace("z", "Z")
        print("\ns.replace('z', 'Z')\ns = ", x)
    
    def video_entradaysalida (self):
        print("**** ENTRADA Y SALIDA POR PANTALLLA *****")
        N = input("\n1. Ingrese su nombre: ")
        print("Ahora estás en la matrix, ", N)
        costo = float(input("\n2. Ingrese el costo de su cena: $"))
        ser = (costo * 0.062) 
        pro = costo * 0.10
        costo = costo+ser+pro
        print("El valor total a pagar con servicio y propina es: $",costo)
        dia = (input("\n3. Ingrese el día de su coumpleaños: "))
        mes = (input("Ingrese el mes de su coumpleaños: "))
        año = (input("Ingrese el año de su coumpleaños: "))
        #Si utilizo tipo int, aparece el formato con espacios.
        print("La fecha de su cumpleaños en formato dd/mm/aaaa, es: "+dia+"/"+mes+"/"+año)
        #GUARDAR EN UNA SOLA VARIABLE
        #fecha = int(input("\nIngrese su fecha de nacimiento en formato DDMMAAAA: "))
        #año = fecha%10000
        #dia = fecha//1000000
        #mes = (fecha // 10000) % 100
        #print("La fecha que ud ingreso es: ",dia,"/",mes,"/",año)
        #SI FUERA STRING
        fecha = (input("\nIngrese su fecha de nacimiento en formato DDMMAAAA: "))
        dia = fecha[:2]
        mes = fecha[2:4]
        año = fecha[4:]
        print("La fecha que ud ingreso es: ",dia,"/",mes,"/",año)
        km = int(input("4. Ingrese cuantos km puede recorrer su moto con 1 litro de combustible: "))
        cap = float(input("¿Que capacidad en litros tiene el tanque de su moto?: "))
        km1 = float(input("¿Cuántos km en total recorrerán en el viaje?: "))
        total = km1/(km*cap)
        print("En todo el viaje gastarán un total de: ",total," tanques de combustible.")
        m2 = float(input("\nIngrese cuántos m2 tiene el estadio: "))
        gradas = int(input("¿Cuántas personas estan disponibles en las gradas?: "))
        banda = float(input("Banda, ¿Cuál es el porcentaje del estadio que necesitan para el escenario?: "))
        m2gr = m2 * 0.2
        m2ban = m2 * (banda/100)
        m2disp = m2-m2gr-m2ban
        totalper = (m2disp*4)+gradas
        print("En el estadio entran un total de: ",totalper, "personas")
        entrada1 = float(input("Ingrese el precio de la entra especial: $"))
        entrada2 = float(input("Ingrese el precio de la entra normal: $"))
        precio1= (totalper*0.3)*entrada1
        precio2= (totalper*0.7)*entrada2
        print("El total de ventas es: $", precio1 + precio2)

    def video_if (self):
        print("***** CONDICIONALES: IF - ELSE - ELIF *****")
        num = int(input("\n1. Ingrese su número: "))
        if num>= 0:
            print(num)
        else:
            num1 = num * -1
            print("El valor absoluto de",num,"es: ", num1) 
        nom1 = input("\n2. Ingrese el nombre 1: ")
        nom2 = input("Ingrese el nombre 2: ")
        if nom1[0] == nom2[0] or nom1[-1] == nom2[-1]:
            print("Hay coincidencia")
        else:
            print("No hay coincidencia")
        voto = input("\n3. Ingrese el candidato por el que desea votar: ")
        if voto == "A" or voto == "a":
            print("Ud va votado por el partido rojo")
        elif voto == "B" or voto == "b":
            print("Ud va votado por el partido verde")
        elif voto == "C" or voto == "c":
            print("Ud va votado por el partido azul")
        else:
            print("Opción errónea, no ha votado por ninguna de la lista disponible")
        letra = input("\n4. Ingrese una letra: ")
        vocal = "aeiou"
        if len(letra)!=1:
            print("Ha ingresado mas de una letra, sólo es una")
        elif letra.lower() in vocal:
            print("Es una vocal")
        else:
            print("No es una vocal")
        año = int(input("\n5. Ingrese un año: "))
        if año%4!=0:
            print("No es bisiesto")
        elif año%100 != 0 or año%400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
        fecha = input("5. Ingrese la fecha en formato 'Día, DD/MM': ")
        fecha = fecha.lower()
        dia = fecha[0:fecha.find(",")]
        dia1 = int(fecha[fecha.find(" ")+1:fecha.find("/")])
        mes = int(fecha[fecha.find("/")+1:])
        if dia1>31 or mes>12:
            print("Fecha incorrecta")
        else:
            if dia.lower() == "lunes" or dia == "martes" or dia == "miercoles":
                examen = input("¿Le tomaron exámenes? S/N ")
                if examen.lower() == "s":
                    aprobados = int(input("Ingrese la cantidad de aprobados: "))
                    reprobados = int(input("Ingrese la cantidad de reprobados: "))
                    print("Porcentaje que aprobaron: ", (aprobados*100)/(aprobados+reprobados),"%")
            elif dia.lower() == "jueves":
                asistencia = int(input("Ingrese porcentaje de asistencias: "))
                if asistencia>50:
                    print("Asistió la mayor parte")
                else:
                    print("No asistió la mayor parte")
            elif dia.lower() == "viernes":
                if dia1 == 1 and (mes==1 or mes==7):
                    print("Comienzo de nuevo ciclo")
                    alumnos = int(input("Ingrese la cantidad de alumnos: "))
                    dinero = float(input("Ingrese el dinero ingresado por alumno: $"))
                    print("El ingreso total por todos los alumnos es: $",alumnos*dinero)
            else:
                print("Fecha incorrecta")
        print("FIN DEL SISTEMA")
    
    def video_for (self):
        print("***** BUCLES FOR *****")
        print("\n1. Sumatoria de numeros del 1 al 100.")
        res = 0
        for x in range(101):
            res=res+x
        print("La suma de los números del 1 al 100 es: ", res)

        print("\nSumatoria de numeros del 1 al 100 que sean múltiplos de 3.")
        res = 0
        for x in range(101):
            if x%3==0:
                res+=x
        print("La suma de los npumeros del 1 al 100 multiplos de 3 es: ", res)
        num = int(input("\n 2. Ingrese un número para sacar factorial: "))
        f = 1
        if num == 0:
            print("El factorial de",num, "es: 1")
        elif num>0:
            f=1
            for x in range(1,num+1):
                f*=x
            print("El factorial de ",num, "es: ",f)
        else:
            print("El número ingresado debe ser mayor a 0")
        print("\n3. Sucesión de Fibonacci")
        n1 = 0
        n2 = 1
        for x in range(8):
            n3 = n1+n2
            print(n3)
            n1 = n2
            n2 = n3
        sumpo = 0
        sumne = 0
        posi = 0
        for x in range(6):
            n1=int(input("4. Ingrese el valor :"))
            if n1>=0:
                posi+=1
                sumpo+=n1
            else:
                sumne+=n1
        print("Suma de los númerosnegativos es: ", sumne)
        if posi!=0:
            print("Promedio de números positivos: ", sumpo/posi)
        else:
            print("No ingreso valores positivos")
        print("\n5. Encriptación")
        corrimiento = int(input("Corrimiento: "))
        abecedario= "abcdefghijklmnñopqrstuvwxyz"
        for x in range(5):
            mensaje=input("Ingrese el mensaje que desea encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in abecedario:
                    ind=abecedario.find(caracter.lower())
                    ind=(ind+corrimiento)%27
                    encriptado+=abecedario[ind]
                else:
                    encriptado+= caracter
            print("***El mensaje encriptado: ", encriptado)
    
    def video_while(self):
        print("****** BUCLES WHILE *****")
        total = 0
        valor=float(input("\n1. Ingrese el valor de una venta: $"))
        while valor!=0:
            if valor<0:
                print("Valor erróneo")
            else:
                total+=valor
            valor=float(input("Ingrese el valor de una venta: $"))
        if total>1000:
            total-=total*0.10
        print("El valor total a pagar es de: $", total)
        pares=0
        impar=0
        num=int(input("\n2. Ingrese un numero: "))
        while num!=0:
            par=0
            impar1=0
            while num!=0:
                ud=num%10
                if ud%2==0:
                    par+=1
                    pares+=1
                else:
                    impar1+=1
                    impar+=1
                num=num//10
            print("El número que ud ingresó tiene",par,"número(s) par(es) y",impar1,"número(s) impar(es)")
            num=int(input("Ingrese un numero: "))
        print("Hay un total de: ",pares,"números pares")
        print("Hay un total de: ",impar,"números impares")
        valoreslin=0
        cantlineas=0
        titulo = input("\n3. Ingrese el título del libro: ")
        while titulo!="*":
            if titulo == "/":
                cantlineas+=1
                print("Línea entera. Hay ",valoreslin, "digitos numéricos." )
                valoreslin=0
            else:
                for x in titulo:
                    if x in "0123456789":
                        valoreslin+=1
            titulo=input("Ingrese el título del libro: ")
        print("Final. Se leyeron un total de:",cantlineas,"líneas completas.")

    def video_breakcontinue(self):
        print("***** BREAK Y CONTINUE *****")
        cant=0
        num = int(input("\n 1. Ingrese un número: "))
        while num!=0:
            primo=True
            for x in range(2,num):
                if num%x==0:
                    primo=False
                    break
            if primo:
                cant+=1
            num=int(input("Ingrese un número: "))
        print("Numeros primos en total: ", cant)
        año1 = int(input("\n2. Ingrese el año 1:"))
        año2 = int(input("Ingrese el año 2:"))
        for x in range(año1,año2+1):
            if x%10==0:
                if x%4==0:
                    if x%100!=0 or x%400==0:
                        print(x)
                    
    def video10_3 (self):
        def coordenadaZ(x,y):
            x+=10
            y+=15
            return x+y
        # programa principal
        x = int(input("Coordenada eje x: "))
        y = int(input("Coordenada eje y: "))
        for i in range(3):
            z = coordenadaZ(x,y)
            x+=1
            y+=1
        print(x," . ",y)
    def vide10_3_1 (self):
        def maximo(a,b):
            if a > b:
                return a
            else:
                return b

        def minimo(a,b):
            if a < b:
                return a 
            else:
                return b
        # programa principal
        
        x = int(input("Un número: "))
        y = int(input("Otro número: "))
        print(maximo(x-3, minimo(x+2, y-5)))

    def video10_4(self):
        def DNIvalido(dni):
            cantidad=0
            while dni != 0:
                cantidad+=1
                dni//=10
            return cantidad == 7 or cantidad ==8
        print(DNIvalido(340))
        print(DNIvalido(12345678))

    def video10_4_2(self):
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud == 0:
                return 0
            cantidad = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    cantidad+=1
                else:
                    if cadena[i] == " " and i<(longitud-1) and cadena[i+1] != " ":
                        cantidad = 0
            return cantidad
        print(lenUltimaPalabra("hola soy"))
    def video10_4_3(self):
        def DNIvalido(dni):
            cantidad=0
            while dni != 0:
                cantidad+=1
                dni//=10
            return cantidad == 7 or cantidad ==8 
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud == 0:
                return 0
            cantidad = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    cantidad+=1
                else:
                    if cadena[i] == " " and i<(longitud-1) and cadena[i+1] != " ":
                        cantidad = 0
            return cantidad
        def primerosTresDigitos(numero):
            while numero >= 1000:
                numero /= 10
            return(int(numero))
        def obtenerIdentificador(nombre,dni):
            nombre=nombre.strip()
            i = nombre[0:nombre.find(" ")]
            i=i+str(lenUltimaPalabra(nombre))
            i = i + str(primerosTresDigitos(dni))
            return i
        nombre=input("Nombre del socio: ")
        while nombre != "":
            dni = int(input("DNI del socio: "))
            while not(DNIvalido(dni)):
                print("Número inválido")
            dni = int(input("DNI del socio: "))
            identificador=obtenerIdentificador(nombre,dni)
            print("El identificador del socio es: ",identificador)
            nombre= input("Nombre del socio: ")
        
    def video11_1(self):
        L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]
        print('L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]')
        print('1. Cuál de estos elementos pertenecen a ella?\n85.7    0   True    [True]    85    "a"    [1,2,3]\n')    
        S = [85.7, 0, True, [True], [(0,0,1)], 85, "a", [1,2,3]]
        for i in S:
            if i in L:
                print(i,"si está en L",)
        
        print("\n2. Cómo obtener la posición en que se encuentra el elemento (0,0,1)?")
        print('L.index((0,0,1))', "=",L.index((0,0,1)))
        
        print("3. Cómo eliminar el último elemento, independientemente de cuántos elementos haya en la lista?")
        print('L.pop(len(L)-1)',"=", L.pop(len(L)-1),"\n",L)
 
        print('4. Utilizar una operación para contar cuántas veces aparece el string "a"')
        print('L.count("a")',"=",L.count("a")) 

    def video11_1_2(self):
        def sumatoria(lista):
            suma = 0
            for n in lista:
                suma+= n
            return suma
        def numerosMenores(lista, limite):
            nueva = []
            for n in lista:
                if n < limite:
                    nueva.append(n)
            return nueva
        def frecuencias(lista):
            nueva=[]
            for n in lista:
                if (n, lista.count(n)) not in nueva:
                    nueva.append((n, lista.count(n)))
            return nueva
        #!1
        numeros=[]
        nro=int(input("Número: "))
        while nro != 0:
            numeros.append(nro)
            nro=int(input("Número: "))
        #!2
        eliminar = int(input("Número a eliminar: "))
        if eliminar in numeros:
            numeros.remove(eliminar)
        else:
            print("Ese número no está entre los ingresados")
        #!3
        print("Sumatoria de los números: ", sumatoria(numeros))
        #!4
        limite=int(input("Filtrar números menores a: "))
        for n in numerosMenores(numeros, limite):
            print(n)
        #!5
        print("Frecuencias:")
        for tupla in frecuencias(numeros):
            print(tupla[0], "aparece", tupla[1], "veces")
    def video11_2(self):
        def agregarPasajeros(pasajeros):
            nombre = input("Nombre -x para cortar: ")
            while nombre != "x":
                dni=int(input("DNI: "))
                destino = input("Ciudad destino: ")
                pasajeros.append((nombre, dni, destino))
                nombre = input("Nombre -x para cortar: ")
            return pasajeros
        def agregarCiudades(ciudades):
            ciudad = input("Ciudad -x para cortar: ")
            while ciudad != "x":
                pais = input("Pais: ")
                ciudades.append((ciudad,pais))
                ciudad = input("Ciudad -x para cortar: ")
            return ciudades
        def buscarCiudad(pasajeros, dni):
            for viaje in pasajeros:
                if viaje[1]==dni:
                    return viaje[2]
            return ""
        def cantidadPasajerosCiudad(pasajeros, ciudad):
            cantidad = 0
            for viaje in pasajeros:
                if viaje[2] == ciudad:
                    cantidad+=1
            return cantidad
        def buscarPaisDestino(pasajeros, ciudades, dni):
            ciudadBuscada=buscarCiudad(pasajeros, dni)
            for ciudad in ciudades:
                if ciudad[0] == ciudadBuscada:
                    return ciudad[1]
            return ""
        def cantidadPasajerosPais(pasajeros, ciudades, pais):
            cantidad = 0
            for viaje in pasajeros:
                if pais == buscarPaisDestino(pasajeros, ciudades, viaje[1]):
                    cantidad+=1
            return cantidad
        pasajeros =[("Manuel Juarez", 12345678, "Liverpool"),("Silvana Paredes", 22709128, "Buenos Aires"),("Rosa Ortiz", 12534563, "Inglaterra")]
        ciudades = [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]
        while True:
            print("1. Agregar pasajeros\n2. Agregar ciudades \n3. Buscar ciudad destino mediante el DNI \n4. Cantidad de pasajeros que viajan a una ciudad \n5. Buscar país destino mediante DNI \n6. Cantidad de pasajeros que viajan a un país\n7. Salir del programa")
            opcion = int(input("Acción a ejecutar: "))
            if opcion == 1:
                print("AGREGAR PASAJEROS")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion == 2:
                print("AGREGAR CIUDADES")
                ciudades=agregarCiudades(ciudades)
            elif opcion == 3:
                dni=int(input("DNI: "))
                print("El pasajero viaja a", buscarCiudad(pasajeros, dni))        
            elif opcion == 4:
                ciudad = input("Ciudad: ")
                print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad),"pasajeros")
            elif opcion == 5:
                dni = int(input("DNI: "))
                print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
            elif opcion == 6:
                pais=input("País: ")
                print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais),"pasajeros")
            elif opcion == 7:
                break
    def video12_1(self):
        A={"z", 8, "9",(10,20,30),8,9,8}
        B={7,8,9}
        print('\n Dados los siguientes conjuntos: \nA={"z", 8, "9",(10,20,30),8,9,8}\nB={7,8,9}\n¿Cuántos elementos tiene el conjunto A?')
        print(len(A))

        print('\n¿Cómo se podrían agregar en el conjunto B los números 1, 2, 3, en una única operación?')
        print('B.update([1,2,3])', "=", B.update([1,2,3]))

        print("\n¿Es A menor que B o B menor que A?\nNinguna de las dos. Cada uno tiene elementos únicos")
    
    def video12_1_2(self):
        def cargarNombres(alumnos):
            nombre = input("Nombre: ")
            while nombre != "x":
                alumnos.add(nombre)
                nombre= input("Nombre: ")
            return alumnos

        primaria = set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria = cargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria = cargarNombres(secundaria)

        print("NOMBRES DE TODOS LOS ALUMNOS: ")
        for nombre in primaria|secundaria:
            print(nombre)

        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)

        print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA")
        for nombre in primaria-secundaria:
            print(nombre)
    def video12_1_3(self):
        def direcciones(ventas):
            domicilios=set()
            for venta in ventas:
                domicilios.add(venta[3])
            return domicilios
        
        direcc = [("Nuria Costa", 5, 12790.78, "Calle las Flores 355"), ("Jorge Russo", 7, 669, "Mirasol 218"), ("Nuria Costa", 9, 532.90, "Calle las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
        print(direcciones(direcc))
    def video13_1(self):
        E = {1:"a", "prueba":[1,2,3,5], (4,5):3}
        print('Dado el siguiente diccionario:\n E = {1:"a", "prueba":[1,2,3,5], (4,5):3}')
        print("\n¿Es el 1 un elemento de E?\n No, los elementos sólo pueden ser pares formados por clave: valor")

        print("\n¿Cuántos elementos tiene E?\nTiene 3 elementos")

        print("\n¿Por qué da error la instrucción E[0]?\nPorque la clave 0 no existe en E")

        print('¿Qué retorna la instrucción 1 en E.values0()?\nFalse, El número 1 existe como clave y también existe dentro de la lista E["prueba"] pero no existe entre los valores del diccionario E')

        print('\n¿Qué retorna E["prueba"][2] y por qué?\n3, porque E["prueba"] es una lista y su posición 2 almacena al número 3')
    def video13_1_2(self):
        contadores = {}
        for i in range(3):
            cadena = input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter.lower() not in contadores.keys():
                    contadores[caracter]=1
                else:
                    contadores[caracter]+=1
        
        for caracter,cantidad in contadores.items():
            print(caracter, ":", cantidad)
    def video13_1_3(self):
        def funcion1(pacientes):
            e=0
            t=0
            for datos in pacientes.values():
                if datos[2]:
                    e+=datos[1]
                    t+=1
            if t>0:
                return e/t
            else:
                return 0

        def funcion2(pacientes, medicos, dni):
            for medico in medicos:
                if medico[0] == pacientes[dni][3]:
                    return medico[1]
            return ""
        pacientes = {10267489:["Marta Ramos",68,True,829], 22819922: ["Lucas Pérez", 47, False, 437], 40526661: ["Facundo Lucero", 29, True, 829]}
        print(funcion1(pacientes))
        medicos = {(829,"Gabriela Ríos"),(437, "Pedro Olivares"), (561, "Soledad Fuentes")}
        print(funcion2(pacientes,medicos,22819922))
    def video13_2(self):
        def cargarSocios(socios):
            numero = int(input("Número de socio:"))
            while numero != 0:
                nombre = input("Nombre y apellido: ")
                fecha = input("Fecha de ingreso: ")
                cuota = input("Cuota al día s/n: ")
                pago = cuota.lower() == "s"
                socios[numero] = [nombre,fecha,pago]
                numero = int(input("Número de socio: "))
            return socios 
    
        def modificarFecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]= fecha_nueva
            return socios

        def numeroSocio(socios,nombre):
            for numero, datos in socios.items():
                if datos[0].lower() == nombre.lower():
                    return numero
            return 0

        def formatoFecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
            for numero, datos in socios.items():
                print("-Número: ",numero)
                print("-Nombre: ",datos[0])
                print("-Fecha de ingreso: ",formatoFecha(datos[1]))
                if datos[2]:
                    print("-Cuota al día")
                else:
                    print("-En deuda")
                print("~~~~~~~~~~~~")
            return None
        socios_activos={1:["Amanda Núñez", "17032009", True], 2:["Bárbara Molina","17032009"], 3:["Lautaro Campos","17032009"]}
        print("***Cargar Socios")
        socios_acitvos=cargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero = int(input("Número de socio: "))
        socios_activos[numero][2] = True

        print("***Modificando fecha de ingreso...")
        socios_activos = modificarFecha(socios_activos, "13032018", "14032018")
        
        print("***Eliminar socio: ")
        nombre = input("Nombre y Apellido: ")
        numero = numeroSocio(socios_activos, nombre)
        del socios_activos[numero]

        imprimirListado(socios_activos)


#creamos un objeto de la clase.
ej = ejercicios()

#Acá llamamos el metodo que deseemos, cada metodo son los ejercicios de cada vídeo.
ej.video_variables()
#ej.video_tipodedatos()
#ej.video_tablas()
#ej.video_string()
#ej.video_entradaysalida()
#ej.video_if()
#ej.video_for()
#ej.video_while()
#ej.video_breakcontinue()
#ej.video10_3()
#ej.vide10_3_1()
#ej.video10_4()
#ej.video10_4_2()
#ej.video10_4_3()
#ej.video11_1()
#ej.video11_1_2()
#ej.video11_2()
#ej.video12_1()
#ej.video12_1_2()
#ej.video12_1_3()
#ej.video13_1()
#ej.video13_1_2()
#ej.video13_1_3()
#ej.video13_2()


