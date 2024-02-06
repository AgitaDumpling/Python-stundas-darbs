def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding= 'utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding= 'utf-8')
    fails.write(teksts)
    fails.close()
    
def nolasīt(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
        rindas = fails.readlines()
    return rindas
    
print(nolasīt("faili/teksts.txt"))

vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kaspers"]
vecums = [23,150,37,5]
dzimums = ["s", "s", "v", "v"]
precejies = ["Jā", "Nē", "Nē", "Jā"]

ierakstit("", "faili/cilvekiem.txt")
for i in range( len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis" 
    if precejies[i] == "Jā":
        rakstamais = "Ir precējies"   
    else:
        rakstamais = "Nav precējies"
    teksts = "{} {} - {}, {}\n".format(vardi[i],uzvardi[i],vecums[i],dzimums[i],precejies[i])
    pierakstit(teksts, "faili/cilvekiem.txt")


#Izveidojas fails kur katrā rindiņā ir vārds, uzvārds - vecums
#Anna Bērziņā - 23
#pierakstit("Sveiki, visi kabači!\n", "faili/teksts.txt")   
#Faili, kuru nosaukums ir cilveks0.txt
#Saturs - Anna Jūs esat laimējusi JAUNU AUTO!

visi = nolasīt("faili/cilveki.txt")
vardi = []
for cilveks in visi:
    info = cilveks.split("")
    vardi.append(info[0])
    vecums1 = (info[3].rsplit(","))
print(vardi)