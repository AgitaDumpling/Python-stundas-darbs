def dienas_mekletajs(sis_gads,sis_menesis,si_diena,dz_gads,sis_datums,dz_menesis,dz_datums):
    menesu_dienu_skaits = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 30, 30]
    #Skaitām cik dienas pagājušas
    #Pārbaude, vai šogad jau ir bijusi dzimšanas diena
    pagajusas_dienas = 0
    pagajusie_gadi = sis_gads-dz_gads
    return "OK"

if vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums) == False:
    pagajusie_gadi = pagajusie_gadi-1 

pagajusas_dienas = pagajusie_gadi*365

garie_gadi = 0
parbaudes_gads_sakums = dz_gads

    if vai_sogad_jau_bija_dzd(dz_menesis, dz_datums, 2, 29) == True:
       parbaudes_gads_sakums = parbaudes_gads_sakums+1

parbaudes_gads_beigas = sis_gads

   if vai sis_datums(sis_menesis, sis_datums, 2, 29) == False:
     parbaudes_gads_beigas = sis_gads-1

for gads in range(parbaudes_gads_sakums, parbaudes_gads_beigas, dz_gads, sis_gads+1, 1):
    if gads%4 == 0:
       garie_gadi = garie_gadi+1
    if gads%100 == 0 and gads % 400 != 0:
       garie_gadi = garie_gadi-1

pagajusas_dienas
return "OK"


def vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums):
    if sis_menesis>dz_menesis:
        return True
    if sis_menesis<dz_menesis:
        return False
    if sis_datums>=dz_datums:
        return False
    return True

