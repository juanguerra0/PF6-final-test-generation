import json
import requests


resultado = requests.get("https://api-colombia.com/api/v1/TypicalDish")
platos = json.loads(resultado.content)




def dish_fetch(eleccion):
   #eleccion = int(input())
   respuesta = platos[eleccion]

   return respuesta




def main():

    #print("¡Hola! Bienvenido al programa")
    #print("Selecciona el plato del cuál quieres saber mas información (Numero del 1 al )")

    eleccion = int(input())
    
    print(dish_fetch(eleccion))

    #print("¡Hola, estudiantes!")


if __name__=="__main__":
    main()  