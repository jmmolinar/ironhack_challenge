#JOSÉ MIGUEL MOLINA RONDÓN - 07/05/2020 - DD/MM/AAAA
#Challenge 1 - MARKET SEGMENTATION

#LISTA DE INDICE DE CLIENTES
customer_indices = [49200, 13590, 11580, 17925, 17115, 19630, 45710, 37190, 23455, 20815, 15515, 22505, 44260, 42545, 19565, 19149, 14253, 35412, 35046, 30801, 13974, 42399, 26796, 44508, 26001, 48926, 30589, 36997, 10271, 14866, 42599, 31388, 13492, 30328, 17564, 49499, 35116, 22289, 26048, 17299, 15271, 18029, 45196, 34294, 31507,31429, 27506, 42271, 20894, 35707, 48484, 42479, 27148, 13732, 49741, 14819, 22238, 34516, 20731, 36848, 22772, 37201, 38596, 48121, 23497, 11198, 16762, 16711, 26399, 18466, 27043, 48679, 42464, 26794, 22222, 26984, 48307, 15749, 14212, 49232, 41647, 28618, 14606, 13687, 15533, 28306, 11042, 41302, 49978, 14254, 49777, 27029, 33451, 48802, 24574, 34534, 16703, 49411, 15319, 19961]

#LONGITUD DE LISTA DE INDICE DE CLIENTES
print("CANTIDAD DE CLIENTES: ",len(customer_indices))

#CREACION DE LISTA DE SEGMENTACION
segmentation = customer_indices[:]

#CREACION DE LISTAS POR CADA TIPO DE CLIENTE
listLoyal = []
listVIP = []
listLoyalVIP = []
listRegular = []

#FUNCION PARA DETERMINAR EL MULTIPLO
def multiple(a, multiple):
  return True if a % multiple == 0 else False

#RECORRIDO DE LISTA DE INDICES Y CREACION DE SEGMENTACION
for value in range(len(customer_indices)):
  if (multiple(customer_indices[value],3)) and (multiple(customer_indices[value],5)):
    segmentation[value] = "Loyal-VIP"
    listLoyalVIP.append(customer_indices[value])
  else:
    if multiple(customer_indices[value],3):
      segmentation[value] = "Loyal"
      listLoyal.append(customer_indices[value])
    else:
      if multiple(customer_indices[value],5):
        segmentation[value] = "VIP"
        listVIP.append(customer_indices[value])
      else:
        segmentation[value] = "Regular"
        listRegular.append(customer_indices[value])


#SALIDA DE LISTA DE SEGMENTACION
print("\nSEGMENTATION = ",segmentation," Total = ", len(segmentation))

#LISTAS DE INDICES POR CADA TIPO DE CLIENTE
print("\nLoyal-VIP = ", listLoyalVIP)
print(" Total = ", len(listLoyalVIP))
print("\nLoyal = ", listLoyal)
print(" Total = ", len(listLoyal))
print("\nVIP = ", listVIP)
print(" Total = ", len(listVIP))
print("\nRegular = ", listRegular)
print(" Total = ", len(listRegular))
