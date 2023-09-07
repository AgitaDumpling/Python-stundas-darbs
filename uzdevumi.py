def tests(parametrs):
    a = parametrs #darbības ar parametriem
    return a #funkcijas rezultāts

print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

print("The result is", pirmais(20,30) )


def otrais(sakums = 0, beigas = 10, solis = 1):
    esosais = 0 
    ieprieksejais = 0
    for i in range(sakums, beigas, solis):
        iepriksejais = esosais
        esosais = 1
        summa = ieprieksejais+esosais
        print("Current Number" , esosais, "Previous Number", ieprieksejais, "Sum:", summa)
        return

otrais()

def tresais(teksts):
    print("Sakotnejais teksts ir ", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print (teksts[i])
    return

tresais()   

def ceturtais(teksts, n ):
    print("teksts:", teksts)
    print("Noņemot pirmos",n,"burtus sanāk",teksts[n:])
    return

ceturtais("pynative",4)

def piektais():