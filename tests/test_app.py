from app import agregar_deseo
def test_agregar_deseo():
    lista = []
    resultado = agregar_deseo(lista, "Viajar a Japón")
    assert resultado is True
    assert "Viajar a Japón" in lista