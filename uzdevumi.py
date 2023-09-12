
def tests(parametrs):
    a = parametrs #darbības ar parametriem
    return a #funkcijas rezultāts

# print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

# print("The result is", pirmais(20,30) )

def otrais(): #def otrais(sakums = 0, beigas = 10, solis = 1)
    esosais = 0
    ieprieksejais = 0
    for i in range(10): #range(sakums, beigas, solis)
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais+esosais
        print("Current Number", esosais, "Previous Number", ieprieksejais, "Sum:", summa)
    return

# otrais()

def tresais(teksts):
    print("Sākotnējais teksts ir ", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print(teksts[i])
    return

#tresais("pynative")

def ceturtais(teksts, n):
    print("Teksts:", teksts)
    print("Noņemot pirmos",n,"burtus sanāk:",teksts[n:])
    return

# ceturtais("pynative",4)

def piektais(saraksts):
    print("Dotais saraksts:", saraksts)
    print("Result is", saraksts[0]==saraksts[-1])
    return

#skaitli1 = [10, 20, 30, 40, 10]
#skaitli2 = [75, 65, 35, 75, 30]

#piektais(skaitli2)

def sestais(saraksts):
    print("dotais saraksts:", saraksts)
    print("Ar 5 dalās")
    for elements in saraksts:
        if elements%5 == 0:
            print (elements)
        return

skaitli = [4, 65, 32, 88]    
sestais(skaitli)    