
import  tweepy
import numpy as np
import random
import time

class Bot():
    ''' Clase para enviar tweets de forma automatica cada cierto tiempo
    haciendo uso del mulo tweepy'''
    def __init__(self):
        pass

    # Realizar la conexin con la API de twitter
    def accesAPI(self, tweet):
        # Coloca dentro de las comillas tus claves...
        CONSUMER_KEY = '5HggmQuK7JsO7BjjlheOUItXN'
        CONSUMER_SECRET = 'buBeAmY1xhvflnQluVu95rzsFT9Sd8V9U8KzM2DUDkjbB6Jk2A'
        ACCESS_KEY = '958805551-I21UhGTtz3DMYd4MYzyzTwyy9EPzxJRkRfQL141O'
        ACCESS_SECRET = 'NutAa8lTn9yrLXByq1Csg1q0K3uKdBFqhuFAuYbKKyjXc'

        # En esta parte nos identifica para poder realizar operaciones
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        # update_status('mensaje' o variable) es para actualizar nuestro estado
        hack = tweepy.API(auth)

        hack.update_status(tweet)

        pass


    def tweetear(self):
        tweets = ["Inaguración del #FLISoLQro2016 a las 09:00 a.m en el Auditorio de la #UAQ ","El #InstallFes lo mejor del #FLISoLQro2016, lleva tu máquina e instala #GNU/Linux","A las 09:15, Jesús Pérez impartirá el taller: Tecnologías migradas o incluidas en el Kernel (avanzado) en #Salón. @Aztli_GNU #FlisolQro2016","A las 09:15, Beatriz Acoltzi nos estará hablando de : Entrar al mundo del Software Libre sin morir en el intento. @Aztli_GNU #FlisolQro2016","A las 09:15, Leslie J. Hernández impartirá el taller: #Gimp para principiantes en #LabPrincipiantes. @Aztli_GNU #FlisolQro2016","A las 09:15, Jesús Hernández impartirá el taller: De 0 a 100 en #github en #LabAvanzados. @Aztli_GNU #FlisolQro2016","A las 09:15, Franco Frías impartirá el taller: Hologramas en #SalaCulturaLibre  #FlisolQro2016","A las 10:30, Edgar López hablara sobre: Gestión de #LVM en #Linux en #SalónAvanzados @G3ekArmy #FlisolQro2016","A las 11:20, Concursos y dinámicas, para los que no estén en conferencia o taller en #SalaCulturaLibre  #FlisolQro2016","A las 11:20, Enrique Contreras: ¿Cómo gestionar un proyecto de desarrollo seas #freelanceo trabajes en oficina? en #Salon  #FlisolQro2016","A las 10:55, Mónica Hernández hablara de: Tecnologías emergentes #Hardware y #Software Libre en #Auditorio @HackerGirlMx  #FlisolQro2016","A las 11:45, Ivonne Lima impartirá el taller: Despejando tus ideas con #Inkscape en #LabPrincipiantes @Aztli_GNU  #FlisolQro2016","A las 11:45, Edgardo Sánchez impartirá el taller: Sistemas #criptográficos con #Gcc desde 0 en #Labavanzados @Aztli_GNU  #FlisolQro2016","A las 11:45, Raúl González impartirá el taller: Levantar una App con Spring 4, JavaScript y AngularJS en #SalaCulturaLibre #FlisolQro2016","A las 12:00, Franco Frías hablara sobre: Evolución de #Android hacia el #IoT en #Auditorio @google #FlisolQro2016","A las 13:45, Receso conferencia talleres en  #FlisolQro2016.","A las 14:20, Yuliana Reyna hablara de: #Womoz de Mozilla en #Auditorio @mozillamx  #FlisolQro2016.","A las 14:20, Andres Sabas hablara de: Hagamos el #IoT #DIY en #SalonAvanzados @InventorsHouse  #FlisolQro2016.","A las 14:20, Alejandra Sánchez impartirá el taller de: Modelado en 3D con Blenderen #LabPrincipiantes @Aztli_GNU  #FlisolQro2016.","A las 14:20, Tania Lucero impartirá el taller de: Mi primer #App híbrida con Ionic #LabAvanzados @Aztli_GNU  #FlisolQro2016.","A las 14:20, Enrique Contreras impartirá el taller de: #Wordpress como Framework para desarrollo web, en #SalaCulturaLibre  #FlisolQro2016.","A las 15:30, Raúl Granados de: Introducción al patrón de arquitectura: Microservicios, en #SalonAvanzados  #FlisolQro2016.","A las 15:20, Nicolás Pineda hablara  de: ¿Me están espiando? , en #Auditorio @G3ekArmy #FlisolQro2016.","A las 16:30, Concursos y dinámicas, para los que no estén en conferencia o taller en #SalaCulturaLibre  #FlisolQro2016","A las 16:40, Raúl Eduardo González hablara  de: #BigData, en #SalonAvanzados #FlisolQro2016.","A las 16:40, Francisco Constante impartirá el taller de: #Android para principiantes, en #LabPrincipiantes #FlisolQro2016.","A las 16:40, Mónica Hernández impartirá el taller de: #Android en #LabAvanzados, @HackerGirlMx #FlisolQro2016.","A las 16:40, Oliver Cuahutencos impartirá el taller de: De pixel a pixel creando un editor de Imagen en #SalaCulturaLibre, #FlisolQro2016.","A las 16:50, Gerardo Antonio Aguilar hablará de: ¿Qué? ¿Cómo? ¿Para qué? del #OpenData en #Auditorio, @InventorsHouse #FlisolQro2016.","A las 17:50, David Amador hablará de: El conocimiento abierto como arma de construcción masiva en #Auditorio, @InventorsHouse #FlisolQro2016","A las 18:40, Concursos y dinámicas, para terminar la jornada con regalitos y diversión en #Auditorio  #FlisolQro2016",]

        usado = [-1]
        contador = 0
        while True:

        	tweet = random.choice(tweets)
        	
        	self.sleep()
        	print(tweet)

        	self.accesAPI(tweet)
        	pass
        
        pass


    def sleep(se):
    	time.sleep(1800.0)

    	pass



    pass


app = Bot()
app.tweetear()