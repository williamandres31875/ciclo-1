# Reto2 Pensun academico

pen = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2}, '4567': {'nombre': 'ingés', 'créditos': 1}}, {}, {}]


def modificar_materia(pensum, semestre, materia, nombre, creditos):
    if semestre <= 0 or semestre > len(pensum):

        mensaje = 'Ingrese un semestre válido'

    else:

        aux = pensum[semestre - 1]
        if aux == {}:
            mensaje = 'El semestre no tiene materias'

        else:

            est = materia in pensum[semestre - 1]
            if est:
                pensum[semestre - 1][materia]['nombre'] = nombre
                pensum[semestre - 1][materia]['créditos'] = creditos
                mensaje = 'Modificada con éxito'
            else:
                mensaje = 'La materia no existe'

    return mensaje


revisar = modificar_materia(pen, 1, '0123', 'lectoescritura', 3)
print(revisar)
print(pen)
