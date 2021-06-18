#Sistema que programa la entrega de existencias de múltiples tipos de medicamentos en varias sucursales de una IPS para el tratamiento y prevención de la hipotensión y la hipertensión.
def op():
    M[u-1][tipo-1] = M[u-1][tipo-1] - existencias
    entregas[u-1][tipo-1] =entregas[u-1][tipo-1] + existencias
    pacientes[u-1] = pacientes[u-1] + 1

def op_2():
    M[u-1][tipo-1] = M[u-1][tipo-1] - 0
    entregas[u-1][tipo-1] =entregas[u-1][tipo-1] + 0
    pacientes[u-1] = pacientes[u-1] + 1

M = []
n = k = 0
while n < 1 or k < 1:
    n,k,m = map(int,input("Ingresa separado por espacios: número de sucursales, tipos de medicamento, cantidad de pacientes: ").split())

for i in range(n):
    M.append(input("Ingresa separado por espacios: Valores de las existencias para cada tipo de medicamento ").split())

for i in range(n):
    for j in range(k):
        M[i][j] = int(M[i][j])

pacientes = []

for i in range(n):
    pacientes.append(0)

entregas = []

for i in range(n):
    entregas.append([])
    for j in range(k):
        entregas[i].append(0)

for i in range(m):
    u,tipo,existencias,ps,pd = map(int,input("Ingresa separado por espacios: sucursal, tipo de medicamento, existencias a llevar, presión sistólica y presión diastólica: ").split())

    if(ps < 72) and (pd < 65):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()


    elif(ps >= 72 and ps < 107) and (pd >= 65 and pd < 73):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op_2()

         
    elif(ps >= 107 and ps < 124) and (pd >= 73 and pd < 81):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op_2()


    elif(ps >= 124 and ps < 138) and (pd >= 81 and pd < 93):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()

                        
    elif(ps >= 138 and ps < 156) and (pd >= 93 and pd < 102):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()

                        
    elif(ps >= 156 and ps < 175) and (pd >= 102 and pd < 114):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()

                
    elif(ps >= 175) and (pd >= 114):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()


    elif(ps >= 136) and (pd < 92):
        if u <= n and u > 0 and tipo > 0 and tipo <= k and existencias >=0:
            op()

for i in range(n):
    print(f"Sucursal: {i+1}")
    min_tipo = M[i][0]
    max_tipo = M[i][0]
    mn = 1
    mx = 1
    for j in range (k):
        if min_tipo > M[i][j]:
            min_tipo = M[i][j]
            mn=j+1
        if max_tipo < M[i][j]:
            max_tipo = M[i][j]
            mx=j+1
    min_entregada = min(entregas[i])
    max_entregada = max(entregas[i])

    suma = 0

    for j in range(k):
        suma = suma + entregas[i][j]
    prom1 = suma/k

    if pacientes[i] == 0:
        prom2 = 0
    else: 
        prom2 = suma/pacientes[i]

    mayor = entregas[0][0]
    menor = entregas[0][0]
    amayor = amenor = 1
    for l in range (n):
        if entregas[l][0]>mayor:
            mayor=entregas[l][0]
            amayor= l+1
        if entregas[l][0] < menor:
            menor = entregas[l][0]
            amenor = l+1

    prom1 = "{:.2f}".format(prom1)
    min_entregada = "{:.2f}".format(min_entregada)
    max_entregada = "{:.2f}".format(max_entregada)
    prom2 = "{:.2f}".format(prom2)
    print(f"Tipo de medicamento con menor cantidad de existencias entregadas: {mn} Cantidad de existencias del medicamento: {min_tipo}")
    print(f"Tipo de medicamento con mayor cantidad de existencias entregadas: {mx} Cantidad de existencias del medicamento: {max_tipo}")
    print(f" Cantidad mínima entregada: {min_entregada} Cantidad promedio entregada: {prom1} Cantidad máxima entregada: {max_entregada}")
    print(prom2)
print(f"N.Sucursal cantidad menor de medicamentos tipo 1 entregados: {amenor} Cantidad: {menor}")
print(f"N.Sucursal cantidad mayor de medicamentos tipo 1 entregados: {amayor} Cantidad: {mayor}")