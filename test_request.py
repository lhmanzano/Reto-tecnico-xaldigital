import pandas as pd
import requests
import json
import datetime


url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

response = requests.get(url)

data = json.loads(response.text)
data2 = data['items']
data2

#_____________Respuestas contestadas___________________________________________

def respuestas_contestadas():
    Contestadas=0
    for item in data2:
        if item['is_answered'] == True:
            Contestadas = Contestadas+1

    return{"Respuestas contestadas":Contestadas}


def test_respuestas_contestadas():
    result_contestadas = respuestas_contestadas()
    expected_contestadas = {"Respuestas contestadas":result_contestadas["Respuestas contestadas"]}

    assert result_contestadas == expected_contestadas

#_____________Respuestas contestadas___________________________________________


#_____________Respuestas no contestadas___________________________________________

def respuestas_nocontestadas():
    NoContestadas=0
    for item in data2:
        if item['is_answered'] == False:
            NoContestadas = NoContestadas+1
    
    return{"Respuestas no contestadas":NoContestadas}

def test_respuestas_nocontestadas():
    result_nocontestadas = respuestas_nocontestadas()
    expected_nocontestadas = {"Respuestas no contestadas":result_nocontestadas["Respuestas no contestadas"]}

    assert result_nocontestadas == expected_nocontestadas   

#_____________Respuestas no contestadas___________________________________________


#________________Respuesta con menor número de vistas________________________________________

def numero_vistas():
    Vistas = None
    for item in data2:
        if Vistas is None or item ['view_count'] < Vistas:
            Vistas = item ['view_count']
    
    return{"Menos vistas":Vistas}

def test_numero_vistas():
    result_vistas = numero_vistas()
    expected_vistas = {"Menos vistas":result_vistas["Menos vistas"]}

    assert result_vistas == expected_vistas

#________________Respuesta con menor número de vistas________________________________________


#________________Respuesta mas vieja________________________________________

def respuesta_vieja():
    FechaVieja = None
    for item in data2:
        if FechaVieja is None or datetime.datetime.fromtimestamp(item['creation_date']) < FechaVieja:
            FechaVieja = datetime.datetime.fromtimestamp(item['creation_date'])
    
    return{"Fecha vieja":FechaVieja}

def test_respuesta_vieja():
    result_fechavieja = respuesta_vieja()
    expected_fechavieja = {"Fecha vieja":result_fechavieja["Fecha vieja"]}

    assert result_fechavieja == expected_fechavieja

#________________Respuesta mas vieja________________________________________


#________________Respuesta actual________________________________________

def respuesta_actual():
    FechaActual = None
    for item in data2:
        if FechaActual is None or datetime.datetime.fromtimestamp(item['creation_date']) > FechaActual:
            FechaActual = datetime.datetime.fromtimestamp(item['creation_date'])
    
    return{"Fecha actual":FechaActual}

def test_respuesta_actual():
    result_fechaactual = respuesta_actual()
    expected_fechaactual = {"Fecha actual":result_fechaactual["Fecha actual"]}

    assert result_fechaactual == expected_fechaactual

#________________Respuesta actual________________________________________


#________________Mayor Reputacion________________________________________

def mayor_reputacion():
    reputacion = 0
    for item in data2:
        repu = item['owner']
        rate = repu.get('reputation')
        if type(rate) == int:
            if rate > reputacion:
                reputacion = rate
        else:
            continue
    #print("La respuesta con la mayor reputacion fue la que obtuvo: ", reputacion)
    return{"Mayor reputacion":reputacion}

def test_mayor_reputacion():
    result_reputacion = mayor_reputacion()
    expected_reputacion = {"Mayor reputacion":result_reputacion["Mayor reputacion"]}

    assert result_reputacion == expected_reputacion

#________________Mayor Reputacion________________________________________
