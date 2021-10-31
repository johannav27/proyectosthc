#TallerHerramientasComputacionales. 31-Octubre-2021. Proyecto 1.
#Barbosa Olivares Keit Ehecatl
#González Navarrete Johan Jesús
#Hu Tang Wei Le
from random import randint
print("MULTIPLICACIÓN EGIPCIA\n=======================\n Se pedirán dos numeros a y b para los factores por defecto")

#Definimos la función, los valores por defecto serán ingresados por el usuario y el valor vf
#servirá para hacer el bucle
def productoegipcio(a=float(input("a: ")), b=float(input("b: ")), vf=True):
    """\nEsta función recibe dos numeros y los multiplica, pero usa el algoritmo de la multiplicación egipcia,
    es decir, se imprimirá paso por paso como se obtuvo el producto mediante dividiendo el segundo factor
    (ingresado por el usuario) por 2 de manera iterativa, y al mismo tiempo el primer factor ingresado por el
    usuario se irá duplicando y si llega a ser el caso que la división del segundo factor es inexacta, se 
    sumará el primer factor al producto y una vez el segundo factor sea 1 o -1, el algoritmo habrá completado 
    el resultado\n
    ===================================================================================================
    """
    print("Se hará el producto de {0} y {1}".format(str(a), str(b)))
    #Condición para volver a usar el programa
    while vf==True:
        #a y b serán para operar, x y y para denominar a los factores originales, y r el producto
        x=a
        y=b
        r=0
        print()

        #inicio de la parte lógica y operaciones
        #el bucle se detiene cuando b alcanza 1 o -1
        while b>=1 or b<=-1:
            
            #comprobar que b es impar si al dividirlo entre dos su residuo es 1
            if b%2==1:
                
                #suma de a en r
                print(b, " es impar, entonces se le suma ", a, " a ", r)
                r+=a
            
            #tabulación de valores por paso
            print("a:",a, "\tb:",b, "\tr:",r, "\n")
            
            #tomar únicamente el entero de b/2, y duplicar a
            b=float(int(b/2))
            a=a*2
        
        #ley de signos
        if (x<0 and y<0) or (x>0 and y>0):
            r=abs(r)
        else:
            r=-abs(r)
        
        #proyección de resultado
        print("El producto de ", x, " y ", y, " es ", r)
        
        #preguntar al usuario si quiere terminar el programa o volver a imprimir el producto
        z=int(input("\nOprima 1 para repetir el producto\nOprima 2 para terminar\n"))
        if z!=1:
            vf=False
        print("\n====================================================")
#Repetimos el programa 5 veces con enteros aleatorios, notar que se tendrá que terminar cada uso del
#con "2" para imprimir el siguiente resultado
for i in range(6): productoegipcio(float(randint(-100, 100)), float(randint(-100,100)))