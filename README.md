![Ironhack logo](https://i.imgur.com/1QgrNNw.png)


# Proyecto_TESTEO_WEB


![Captura de pantalla 2023-05-22 a las 18 06 15](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/061f1799-9a84-469e-b30c-04014e6e7c44)



Para este proyecto hemos trabajado conjuntamente con el equipo de UX para analizar que diseño de una página web era el que más converión tenía.

El equipo de UI UX tenia ya el el proyecto definido que consistía en una librería feminista y nuestro objetivo como Data Analysts era analizar cuanto tiempo tardaba un cliente en realizar una compra dado un libro a comprar, para posteriormente realizar cambios en la página y ver como afectaban al proceso.

El objetivo de UI UX, era que podrían hacer ellos, para que con un cambio sea efectivo, disminuya el tiempo del cliente en la página web y la compra esa mas efectiva. 
Para ellos hicieron los siguientes cambios, haciendo es el testeo del A VS B. 

![Captura de pantalla 2023-05-22 a las 18 07 35](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/4ffc155d-3be0-4705-bf71-29d41152fcd2)


![Captura de pantalla 2023-05-22 a las 18 08 24](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/450a325a-28bc-4aad-ab1c-13c7239d5066)


![Captura de pantalla 2023-05-22 a las 18 08 59](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/32f21d1a-a09e-4479-b1aa-f8caa31c3d3d)


Este proyecto consistió en preguntar a la gente de la calle en tiempo record a hacer una compra ficticia, tanto como en la página web A, y una vez hecho el cambio volver a salir a la calle y hacer lo mismo con la página web B. 


Para realizarlo medimos diferentes factores.

  1.  :crystal_ball: Tiempo desde que entraba en la página hasta que finalizaba la compra
  2.  :crystal_ball: Si usaba o no usaba la barra de buscador
  3.  :crystal_ball: Si una vez que encontraba el libro usaba la pestaña de "Añadir a la cesta" o la de "comprar ya"
  4.  :crystal_ball: El tiempo lo medíamos en términos horarios (min:seg) y el resto de bariables en términos binarios(1 si lo usaba o 0 si no lo usaba)



Con estos puntos, obtenemos los siguientes datos:

******************************************

#A

![Captura de pantalla 2023-05-22 a las 18 16 44](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/712f9cb5-85b1-4355-8833-2c8ce803a0cd)


Análisis de tiempo: a.Sobre la media(que es 0:42 seg), tenemos 17 que convierten antes de la media y 13 que tardan más de la media en convertir. b. Nuestra tasa de conversión es de 56% --> El 56% de los sujetos que realizarn la compra tardaron menos que la media.

Análisis de buscador: a.Nuestra tasa de uso de buscador es del 76% --> El 76% de las personas usó el buscador

Análisis de cesta: a.Nuestra tasa de uso de cesta es del 53% --> El 53% de las peersonas usó la cesta frente al "comprar ya"

Una vez obtuvimos estos datos, el siguiente paso era realizar los cambios en la página y volver a salir a realizar test a otras personas diferentes para no contaminar la muestra.

******************************************

#B

![Captura de pantalla 2023-05-22 a las 18 20 07](https://github.com/Ironhack-Data-Madrid-Abril-2023/6.3-lab_two_sample_hypothesis_test/assets/125477881/c3fb1591-3288-4d75-8d68-468c5dcce602)

Una vez tubimos los datos, relizamos el segundo análisis, obteniendo los siguientes resultados:

Análisis de tiempo: a.Sobre la media(que es 0:46 seg), tenemos 15 que convierten antes de la media y 15 que tardan más de la media en convertir. b. Nuestra tasa de conversión es de 50% --> El 50% de los sujetos que realizarn la compra tardaron menos que la media.

Análisis de buscador: a.Nuestra tasa de uso de buscador es del 33% --> El 33% de las personas usó el buscador

Análisis de cesta: a.Nuestra tasa de uso de cesta es del 10% --> El 10% de las peersonas usó la cesta frente al "comprar ya"



#CONCLUSIONES  :bar_chart:  :



    1.  Con los cambios realizados en el test b, se reduce el tiempo en un 11% con una probabilidad del 69.44%
    2.  Con los cambios realizados en el test b, se reduce el numero de veces que usan el buscador en un 54% con una probabilidad del 99.96%
    3.  Con los cambios realizados en el test b, se reduce el numero de veces que usan el buscador en un 76% con una probabilidad del 99.98%
    
    
    
    
De igual manera, para reforzar el análisis, relizamos los siguientes gráficos:
