def borrar_deseo(lista, deseo):
    if deseo in lista:
        lista.remove(deseo)
        return True
    return False