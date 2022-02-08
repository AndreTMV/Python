# Esta libreria ya viene descargada por default
import math

# Esta libreria ya viene descargada por default
import cmath

# Si desea correr el programa en su PC, instale estas librerias con el comando: pip install matplotlib (esto asumiendo que tenga ya instalado el interprete de python
import matplotlib.pyplot as plt

# Si desea correr el programa en su PC, instale estas librerias con el comando: pip install numpy (esto asumiendo que tenga ya instalado el interprete de python
import numpy as np

# Declaramos la funcion impedancia la cual nos va regresar el valor de la impedancia total en forma rectangular


def impedancias(valor_de_la_impedancia_del_resistor, valor_del_reactancia_capacitiva, valor_de_la_frecuencia):

    # Declaracion de numeros complejos
    forma_rectangular_resistor = valor_de_la_impedancia_del_resistor + 0j

    # Declaracion de numeros complejos usando la funcion complex y multiplicamos por -1 debido a que asi lo indica el formulario
    forma_rectangular_capacitor = complex(
        0,  (-1 * valor_del_reactancia_capacitiva))

    # Obtenemos el angulo para comprobar si esta entre 40 o 60, la funcion math.degrees es para convertir de radianes a grados y math.atan es tan^-1
    angulo_de_comprobacion = math.degrees(
        math.atan(valor_del_reactancia_capacitiva/valor_de_la_impedancia_del_resistor))

    # Sumamos las impedancias para obtener la impedancai total
    forma_rectangular_impedancia_total = forma_rectangular_capacitor + \
        forma_rectangular_resistor

    # Validamos que se cumpla la condicion del angulo
    if(angulo_de_comprobacion <= 40 or angulo_de_comprobacion >= 60):
        print("EL angulo {} no cumple con la condicion que deberia".format(
            angulo_de_comprobacion))

    # Regresamos el valor de la impedancia en forma rectangular
    return forma_rectangular_impedancia_total

# Declaracion de la funcion que nos va imprimir los valores hayados en el circuito RC en serie


def valores_del_circuito(impedancia_total, voltaje_eficaz, valor_de_resistencia, valor_de_la_reactancia_del_capacitor):

    # Convertimos voltaje eficaz a su forma rectangular
    voltaje_polar, angulo_voltaje = rectangular_a_polar(voltaje_eficaz)

    # Convertimos la impedancia a su forma polar
    impedancia_polar, angulo_impedancia = rectangular_a_polar(impedancia_total)

    # Calculamos la intensidad total
    intensidad_polar = voltaje_polar/impedancia_polar

    # Obtenemos el angulo de la intensidad
    angulo_intensidad = angulo_voltaje - (angulo_impedancia)

    # Calculamos el voltaje en el resistor
    voltaje_resistor_polar = intensidad_polar * valor_de_resistencia

    # Calculamos el angulo de desfasamiento del resistor
    angulo_resistor = 0 + (angulo_intensidad)

    # Calculamos el voltaje en el capacitor
    voltaje_capacitor_polar = valor_de_la_reactancia_del_capacitor * intensidad_polar

    # Calculamos el angulo de desfasamiento del capacitor
    angulo_capacitor = -90 + (angulo_intensidad)

    print("Valores obtenidos: \nIntensidad total: {}A *√2 *Senwt + {}º \nVoltaje total: {}V *√2 *Senwt + {}º V\nVoltaje en la resistencia: {}V *√2 *Senwt + {}º V\nVoltaje en el capacitor: {}V *√2 *Senwt {}º V\n".format(round(
        intensidad_polar, 5), round(angulo_intensidad, 2), round(voltaje_polar, 2), round(angulo_voltaje, 2), round(voltaje_resistor_polar, 2), round(angulo_resistor, 2), round(voltaje_capacitor_polar, 2), round(angulo_capacitor, 2)))

    # Regresamos todos los valores obtenidos para graficarlos
    return voltaje_polar, angulo_voltaje, intensidad_polar, angulo_intensidad, voltaje_resistor_polar, angulo_resistor, voltaje_capacitor_polar, angulo_capacitor

# Funcion para separar el angulo y el vector de la forma rectangular, esto para poder convertir el angulo a grados y poder operar con los valores


def rectangular_a_polar(coordenada_rectangular):

    # Convertimos a la forma polar
    almacena_vector, almacena_angulo = cmath.polar(coordenada_rectangular)

    # Retornamos los valores y convertimos el angulo de radianes a grados
    return almacena_vector, math.degrees(almacena_angulo)

# Funcion para graficar el diagrama de Z


def graficar_z(Z):
    # Coordenadas del vector
    x, y = Z.real, Z.imag

    # Limites de la figura
    izda = min(-1, x-1)
    dcha = max(1, x+1)
    abajo = min(-1, y-1)
    arriba = max(1, y+1)

    # El metodo quiver pinta vectores, pero para que salgan de las
    # dimensiones correctas hay que usar los parámetros angles, scale y scale_units

    plt.quiver([x], [y], angles='xy', scale_units='xy', scale=1)

    # Pintamos lineas que pasan por el origen de coordenadas
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Fijamos límites, etiquetas y títulos
    plt.xlim([izda, dcha])
    plt.ylim([abajo, arriba])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafica de Z({},{})'.format(Z.real, Z.imag))
    plt.show()

# Funcion que nos va a ayudar a graficar los fasores


def graficar_ondas_senoidales(frecuencia, unidad_polar, angulo_de_la_unidad, nombre_de_la_grafica):

    # Declaramos y asignamos w
    w = 2*np.pi*frecuencia

    # Declaramos el tiempo
    t = np.linspace(-10, 10, 100)

    # Creamos la grafica, multiplicamos por la raiz de dos la unidad y por el seno de wt y le sumamos el angulo de desfasamiento
    grafica = (unidad_polar)*(np.sqrt(2))*np.sin((w*t) + angulo_de_la_unidad)
    plt.title("Grafica de {}".format(nombre_de_la_grafica))

    # Pintamos lineas que pasan por el origen de coordenadas
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Asignamos etiquetas
    plt.ylabel("{}".format(nombre_de_la_grafica))
    plt.xlabel("Tiempo")
    plt.plot(t, grafica, 'g')
    plt.show()


resistencia = float(input("Dame el valor de la resistencia: "))

capacitor = float(input("Dame el valor del capacitor: "))

frecuencia = float(input("Dame el valor de la frecuencia: "))

voltaje_pico = float(input("Dame el valor del voltaje pico: "))

# Convertimos de la forma rectangular a la forma polar con ayuda de la libreria cmath y redondeamos a dos decimales con round()
voltaje_eficaz = complex((voltaje_pico * .7071), 0)

# Redondeamos el valor de la reactancia a 2 decimales con round()
reactancia_del_capacitor = round(
    1.0/((2.0)*(math.pi)*(frecuencia)*(capacitor)), 2)

# Llamamos a la funcion impedancia
impedancia_total = impedancias(
    resistencia, reactancia_del_capacitor, frecuencia)

# Llamamos a la funcion para graficar el diagrama de Z
graficar_z(impedancia_total)

# Llamamos a la funcion valores_del_circuito
voltaje, angulo_voltaje, intensidad, angulo_intensidad, voltaje_resistor, angulo_resistor, voltaje_capacitor, angulo_capacitor = valores_del_circuito(
    impedancia_total, voltaje_eficaz, resistencia, reactancia_del_capacitor)

# Graficamos cada valor, uno por uno, para ver el siguiente, cierre el que esta activo(en caso de que desee correrlo en su PC)
graficar_ondas_senoidales(frecuencia, voltaje, angulo_voltaje, "Voltaje Total")
graficar_ondas_senoidales(frecuencia, intensidad,
                          angulo_intensidad, "Intensidad Total")
graficar_ondas_senoidales(frecuencia, voltaje_resistor,
                          angulo_resistor, "Voltaje en el resistor")
graficar_ondas_senoidales(frecuencia, voltaje_capacitor,
                          angulo_capacitor, "Voltaje en el capacitor")
