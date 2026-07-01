from app import borrar_deseo 

def test_borrar_deseo():
    lista = ["Viajar a Japón"]
    resultado = borrar_deseo(lista, "Viajar a Japón")
    assert resultado is True
    assert "Viajar a Japón" not in lista