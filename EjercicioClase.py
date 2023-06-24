import plotly.graph_objects as go

def programa(rfile, fasta):
    
    #LAS SIGUIENTES LINEAS CARGAN LA SECUENCIA Y LA DEJA LISTA PARA HACER CALCULOS
    nombre_seq = rfile[0].strip()
    secuencia = ""
    for i in rfile[1:]:
            secuencia += i.strip()
    #DE AQUI EN ADELANTE DEBES CONTAR LOS AMINOCIDOS QUE HAY EN TOTAL
    #Y HACER UNA GRAFICA DE BARRAS DE LOS 20 AMINOACIDOS
    print("\n\n")
    print(secuencia)
    print(f"\nEn total hay: {len(secuencia)} aminoacidos\n")

    ########################################################### Aminoacidos presentes
    aminoacidos = []
    for i in secuencia:
        if i not in aminoacidos:
            aminoacidos+=i
    print(f"\nEn la molecula hay {len(aminoacidos)} tipos de aminoacidos: {aminoacidos}\n")

    ########################################################## Conteo de cada tipo de aminoacido
    lConteo = []
    for a in aminoacidos:
        count = secuencia.count(a)
        lConteo += [[count,a]]

    ########################################################## CREAR GRAFICA
    lista_strings = []
    lista_numeros = []

    # Recorrer la lista original y agregar cada elemento a la lista adecuada
    for elemento in lConteo:
        for x in elemento:
            if isinstance(x, str):
                lista_strings.append(x)
            elif isinstance(x, (int, float)):
                lista_numeros.append(x)

    print(lista_numeros, lista_strings)

    # Crear los datos de ejemplo
    x = lista_strings
    y = lista_numeros

    # Crear la gráfica de barras
    fig = go.Figure(data=go.Bar(x=x, y=y))

    # Añadir títulos y etiquetas a los ejes
    fig.update_layout(title=f'Conteo de {fasta}',
                    xaxis_title='Aminoácidos',
                    yaxis_title='Veces en la proteína')

    # Mostrar la grafica 
    #fig.show()

    # Guardar el gráfico como un archivo HTML
    #fig.write_html('grafica_de_barras.html')

    # Guardar el gráfico como un archivo PNG
    fig.write_image(f'{fasta}.png')

def main():
    ################### FRACCION DE CODIGO###################
    listaFastas = ["BDNF.fasta","MAOB.fasta","MPO.fasta"]
    for fasta in listaFastas:
        #fasta = input("Escriba el nombre de la molecula en formato fasta, eje, TP53.fasta: ")
        file = open(f'{fasta}')
        rfile = file.readlines()
        programa(rfile, fasta)
main()

"""cambio de la nueva rama"""

