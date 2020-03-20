# Pregunta 1 entrevista Tomas Burotto


def fetch_value(array, name):
    # En primer lugar filtro el array por aquellos names que existan dentro de el diccionario
    result = list(filter(lambda x: x['name'] == name, array))
    # Reviso el caso en que no hayan resultados y retorno el string 'not found'
    if len(result) == 0:
        return 'not found'
    # Reviso el caso en que el resultado sea 1 solo y retorno el value
    if len(result) == 1:
        return result[0]['value']
    # El ultimo caso posible es que hayan varias diccionarios con name buscado, en ese caso retorno un array
    # con los values que correspondan al name
    else:
        return list(map(lambda x: x['value'], result))


if __name__ == '__main__':
    # Aca pruebo el codigo con un array en el caso que posea 2 diccionarios con el name 'Guia'
    arr = [
        {
            'name': 'Guia',
            'value': '1234'
        },
        {
            'name': 'Guia',
            'value': '12345'
        },
        {
            'name': 'Orden de Compra',
            'value': '88331'
        },
        {
            'name': 'Boleto',
            'value': '321'
        },
    ]
    value = fetch_value(arr, "Boleto")
    print(value)
