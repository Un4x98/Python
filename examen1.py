notas = {}

#Bucle preguntar notas

while True:
    asignatura =input('Introduce asignatura: ')
    nota=float(input('Introduce tu nota :'))
    if  nota < 0:
        break
    else:
        notas[asignatura]=nota
print('Las asignaturas suspensas son: ')
for asignatura, nota in notas.items():
    if nota < 5:
        print(asignatura)
    