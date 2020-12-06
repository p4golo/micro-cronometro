from microbit import *

zero = "99999:99999"
one = "00000:99999"
two = "90999:99909"
three = "90909:99999"
four = "99900:09999"
five = "99909:90999"
six = "99999:90999"
seven = "90900:99999"
eight = "99099:99099"
nine = "99900:99999"

fonts = (zero, one, two, three, four, five, six, seven, eight, nine)

columnas = 5
filas = 5

def mostrarNumeros():
    pass

def mostrarSegundos(segundos):
    if segundos > 9:
        decenas = segundos // 10
        unidades = segundos % 10
    else:
        unidades = fonts[segundos]
        unidades = unidades.split(":")
        for i in range(filas):
            display.set_pixel(3,i,int(unidades[0][i])) #Esto es lo que hay que usar para printear
        for i in range(filas):
            display.set_pixel(4,i,int(unidades[1][i]))

def mostrarHoras(segundos):
    pass

def mostrarMinutos(segundos):
    pass

def main():

    segundos = 0
    minutos = 0
    horas = 0

    while True:
        #display.set_pixel() Esto es lo que hay que usar para printear
        if button_a.is_pressed():
            mostrarHoras(segundos)
        if button_b.is_pressed():
            mostrarMinutos(segundos)
        mostrarNumeros(segundos)
        sleep(1000) # Para que el bucle tarde un segundo en hacerse
        segundos += 1
        display.clear()

if __name__ == "__main__":
    main()
