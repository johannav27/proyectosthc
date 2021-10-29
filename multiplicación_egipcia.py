print("MULTIPLICACIÓN EGIPCIA")
vf=True

#condición para volver a usar el programa
while vf==True:
    print("\nIntroduzca dos números enteros que desee multiplicar\n")
    
    #solicitar los dos factores
    #a y b serán para operar, x y y para denominar a los factores originales, y r el producto
    x=a=float(input("a: "))
    y=b=float(input("b: "))
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
    
    #preguntar al usuario si quiere seguir usando el programa
    z=int(input("\n¿Desea volver a utilizarlo?\n1: Sí\n2: No\n"))
    if z!=1:
        vf=False
    print("\n====================================================")