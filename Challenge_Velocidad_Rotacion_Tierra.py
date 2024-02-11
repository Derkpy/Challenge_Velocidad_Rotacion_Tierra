import math

# 18.60646, -90.73780
# -38.373825292521154, -69.67405073588125

class Conocer_Velocidad_Rotacion_Tierra:

    def calcular_velocidad_rotacion(self, latitud, longitud):
        # Frecuencia de rotación
        f_r = 1 / 86400

        # Velocidad angular
        vel_rot =( 2 * 3.14159 ) * f_r

        angulo = int(latitud.split(".")[0])
        numeros = int(longitud.split(".")[0])

        radio_tierra = (6.37* (10 ** 6)) # Radio del ecuador expresado en metros
        radianes = math.radians(angulo)
        radio_punto = radio_tierra * math.cos(radianes)

        print("Radio de la tierra donde se situan las coordenadas: \n" + str(radio_punto) + " m")

        velocidad = radio_punto * vel_rot
        print("Velocidad en kilómetros por hora: \n" + str(velocidad * 3.6) + " km/h")

if __name__ == "__main__":
    calcular = Conocer_Velocidad_Rotacion_Tierra()
    entrada = input("A continuación ingresa la latitud y la longitud: \n"
                    "--------------- (latitud, longitud) -------------\n")
    latitud, longitud = entrada.split(",")
    calcular.calcular_velocidad_rotacion(latitud, longitud)