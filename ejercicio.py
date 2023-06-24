
def pC(name):
    out = open(f'./{name}', 'a')

    print ("""
    PREGUNTA (C)
    En esta seccion debera explora bases de datos para comprender un poco mas
    el gen y su relacion con la enfermedad, para esto responda las siguientes preguntas
    consultando las bases de datos del siguiente listado:

    BASES DE DATOS:
    https://www.genecards.org/
    https://genome.ucsc.edu/
    https://string-db.org/


    """)

    Q5 = "\nCuantas Variantes patogenicas OMIM tiene el gen? : "
    Q6 = "\nCon cuantos otros genes INTERACTUA este gen? : "
    Q7 = "\nCuantas enfermedades asociadas tiene el gen que usted trabajo? : "
    Q8 = "\nEn donde esta ubicado el Gen? ej: chr22:12234234-12312312, : "
    Q9 = "\nCual es la funcion del gen? : "
    Q10 = "\nCon base en lo visto en la teoria como se relaciona lo encontrado para el gen? : "

    A5 = input(Q5)
    A6 = input(Q6)
    A7 = input(Q7)
    A8 = input(Q8)
    A9 = input(Q9)
    A10 = input(Q10)

    out.write(f"{Q5}\t{A5}\n")
    out.write(f"{Q6}\t{A6}\n")
    out.write(f"{Q7}\t{A7}\n")
    out.write(f"{Q8}\t{A8}\n")
    out.write(f"{Q9}\t{A9}\n")
    out.write(f"{Q10}\t{A10}\n")

    input ("\n\nHAS TEMINADO, DALE ENTER PARA REGRESAR AL MENU Y ENVIAR TU EJERCICIO")

    out.close()

def pB(name):
    os.system('clear')
    out = open(f'./{name}', 'a')
    print ("""
    PREGUNTA (B)
    En esta sección debera hacer una fracción pequeña de codigo, para esto debe
    completar el siguiente codigo utilizando un nuevo script, SUYO en pythonanywhere

    OJO, este nuevo codigo lo debe llamar p2.py

    1. Copie esta fraccion
    2. Ejecutelo para garantizar que funcione
    3. Completelo segun se describe en el codigo

    """)

    mes = ("""
    ################### FRACCION DE CODIGO###################
    fasta = input("Escriba el nombre de la molecula en formato fasta, eje, TP53.fasta: ")
    file = open(f'{fasta}')
    rfile = file.readlines()
    #LAS SIGUIENTES LINEAS CARGAN LA SECUENCIA Y LA DEJA LISTA PARA HACER CALCULOS
    nombre_seq = rfile[0].strip()
    secuencia = ""
    for i in rfile[1:]:
    \tsecuencia += i.strip()
    #DE AQUI EN ADELANTE DEBES CONTAR LOS AMINOCIDOS QUE HAY EN TOTAL 
    #Y HACER UNA GRAFICA DE BARRAS DE LOS 20 AMINOACIDOS
   

    ## BUENA SUERTE

    print (secuencia)
    ##########################################################
        """)
    print (mes.replace("    ", ""))
    int = 1
    input('\n\nPara continuar debes estar seguro de guardar el codigo como p2.py!! esta guardado correctamente? SOLO DA ENTER SI ESTA CORRECTO')
    out.write(f'Q4\tready\t{int}\n')

    out.close()
def dis():
    d = ["Niemann-Pick Disease",
        "Tay-Sachs Disease",
        "Gaucher's Disease",
        "Cystic Fibrosis",
        "Alagille Syndrome 1",
        "Type 2 Diabetes Mellitus",
        "Scheie Syndrome",
        "Fabry Disease",
        "Krabbe Disease",
        "Glycogen Storage Disease",
        "Farber Lipogranulomatosis"]
    pd = random.randint(0,len(d))
    pd = random.randint(0,len(d))
    return(d[pd])
def pAQ3():
    os.system('clear')
    Q3 = """
    PREGUNTA (A)
    PASO 2

    Consulte la secuencia de aminoacidos de la proteina que codifica el gen en formato FASTA
    y guardela en un archivo de pythonanywhere colocando como cabezera la sigla de la molecula,

    OJO: ESTE ARCHIVO DEBE NOMBRARLO CON LA SIGLA DE LA MOLECULA Y CON EXTENCION .fasta

    ejemplo: este es el nombre que debe tener el archivo con su respectiva sigla TP53.fasta

    Esto es lo que debe estar dentro del archivo:

    >TP53
    CAUYBCTUBACUASKDICLJGMNVHTKDJUT
    KDJJLDDIKDNJGNLDLOPNJDNMJAMKSHE
    SKLKMSNUMSMSJHDNAGFW

    """
    print (Q3)
    input ("Presione ENTER despues de que haya guardado la secuencia para Continuar\n")

    fastas = os.listdir('./')
    getfas = ''

    rep = 1
    for i in fastas:
        if '.fasta' in i:
            file = open(f'./{i}')
            rfile = file.readlines()
            getfas = "".join(rfile)
            cont = input(f'\n{getfas}\n\nESTO ES LO QUE HA CARGADO, esta bien? s/n : ')
            if cont == 's':
                return(getfas, rep)
            else:
                print ("\n\nINTENTELO NUEVAMENTE, VEA BIEN EL EJEMPLO)\n\n")
                rep+=1
                pAQ3()
def pA(name):
    out = open(f'./{name}', 'a')
    d = dis()
    out.write(f'Enfermedad de {name} fue {d}\n')
    print (f"""
    PREGUNTA (A)
    PASO 1

    En esta sección debera consultar una molécula problema, la cual trabajará
    durante todo el ejercicio, para esto deberá consultar la enfermedad que 
    aparecera a continuacion, y responder las preguntas


    ENFERMEDAD ASIGNADA: {d}

    Consulte esta enfermedad en Malacards y responda:

    """)
    Q1 = "Cuantos genes en total estan asociados a la enfermedad? : "
    A1 = input(Q1)
    out.write(f'Q1\t{Q1}\t{A1}\n')
    Q2 = "\nCual es el gen de categoria \"Protein Coding\" principalmente asociado a la enfermedad, ej. APOE : "
    A2 = input(Q2)
    out.write(f'Q2\t{Q2}\t{A2}\n')
    Q3a, Q3b = pAQ3()
    out.write(f'Q3 SECUENCIA\t\n{Q3a}\nIntentos\t{A2}\n')

    out.close()
def sep(l):
    sr = f"""
    #########################################################################
    -------EL RESULTADO DE LA FUNCIÓN ({l}) ESTA DEBAJO DE ESTA LÍNEA--------
    #########################################################################
    """
    return(sr)
def menu(name):
    os.system('clear')
    print (sep('MENU'))
    print ("""\t\t\tEjercicios de Bioinformática
    \t\tCurso de Biología Celular y Molecular
    \t\t\t\t2022-II
    El siguiente código presenta ejercicios que debe realizar
    LEA atentamente cada paso para poder responder con exito
    el ejercicio. Tenga en cuenta que se le presentaran links y
    resultados que deberá utilizar para poder responder las
    preguntas. Muchos exitos

    PREGUNTAS:

    a. Consulte su molécula problema e informacion de la molecula
    b. Calcule la cantidad de aminoacidos "Complete la funcion"
    c. Consulart informacion en bases de datos
    x. GUARDAR Y ENVIAR
    """)
    sel = input('\tescriba la letra correspondiente a cada pregunta y presione ENTER, ejemplo a: ')
    mes = 'Se ejecuto correctamente presione ENTER para regresar al MENU'
    if sel == 'a':
        os.system('clear')
        print (sep('a'))
        pA(name)
        input(mes)
        menu(name)
    elif sel == 'b':
        os.system('clear')
        print (sep('b'))
        pB(name)
        input(mes)
        menu(name)
    elif sel == 'c':
        os.system('clear')
        print (sep('c'))
        pC(name)
        input(mes)
        menu(name)

    elif sel == 'x':
        resname = name.replace('examen_', '')
        os.system('clear')
        os.system(f"zip -P pass {resname}.zip ./*")
        os.system(f"rm -rf ./{name} ./p2.py ./*.fasta")
        print ("""
        Has finalizado el ejercicio, ve a la carpeta del script nuevamente
        ahi aparecera un archivo con tu nombre, Verifica que en efecto se encuentre
        NO LO BORRES; EL PROFESOR LO CALIFICARA'
        """)
    else:
        os.system('clear')
        print (sep('menu'))
        input('\tNo ingreso una respuesta correcta, de ENTER eh intente nuevamente')
        menu(name)
import os
import statistics as sts
import random
from datetime import datetime
import pytz 

os.system('clear')
nameF = 'n'
files = os.listdir('./')
for f in files:
    if 'examen_' in f:
        nameF = f
if nameF == 'n':
    name = input("\nHOLA\nEscriba su apellido y nombre separado por un guion y sin tildes, ejemplo: Tobar_Fabian: ")
    nameF = f'./examen_{name}'
    out = open(f'{nameF}', 'w')
else:
    out = open(f'./{nameF}', 'a')
now = datetime.now(pytz.timezone('America/Bogota')).strftime("%H:%M:%S")
out.write(f'>>>>>>HORA DE INICIO {now}\n')
out.close()
menu(nameF)