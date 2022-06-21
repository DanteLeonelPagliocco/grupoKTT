from numpy import size
from ventanas import Menu
a=[]

a=Menu.listadeDirecciones(a)

for i in range(len(a)):
    for j in range(5):
        if(j==5):
            break
        else:
            print("imprimo esto")
            print(a[i][j])
           
        
