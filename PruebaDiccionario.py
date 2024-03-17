import time

meme_dict = {
            "CRINGE": "▶Algo excepcionalmente raro o embarazoso◀",
            "LOL": "▶Una respuesta común sobre algo gracioso◀",
            "ROFL": "▶Una respuesta a una broma◀",
            "SHEESH": "▶Ligera desaprobación◀",
            "CREEPY": "▶Significa algo aterrador, siniestro◀",
            "AGGRO": "▶Significa ponerse agresivo/enojado◀",
            "XD": "▶Significa una risa descontrolada◀", 
            "BTW": "▶Significa a propósito, por cierto. Se utiliza cuando se está hablando sobre un tema concreto y se quiere añadir algo que tiene relación con eso que se está hablando◀"
            }

print("¡Hola!, aquí tienes un diccionario con algunas palabras que se usan hoy en día.")
time.sleep(2)
print("Es simple de usar solo tienes que elegir una de las palabras que saldrán a continuación^^")
time.sleep(2)
print("CRINGE, LOL, ROFL, SHEESH, CREEPY, AGGRO, XD, BTW")
time.sleep(2)
for i in range(5):
    
    word = input("❖Escribe una palabra que no entiendas (¡con mayúsculas!)❖ : ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Lo sentimos, no se encontró la palabra que buscas...")
