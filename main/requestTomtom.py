import requests

api_key = 'jRJzo9EsGRhQol947cFzSrGNzIYPAsCH'

caminhos = ["Pedro Alvares Cabral - Doca:",'-1.40932,-48.4489','-1.43663,-48.49174'], ["Duque de Caixias - Doca: ",'-1.40951,-48.46381','-1.44609,-48.48798'], ["Pedro Miranda - Doca: ",'-1.40951,-48.46381','-1.44357,-48.48765']

def medir_rota(nomeDaRota,partida, destino):

    # Ponto de partida (latitude e longitude)
    start_point = partida

    # Ponto de chegada (latitude e longitude)
    end_point = destino

    url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_point}:{end_point}/json?key={api_key}&traffic=true'

    # solicitação HTTP GET
    response = requests.get(url)
    varreturn = []
    
    if response.status_code == 200:
       
        route_data = response.json()
        
        # print(route_data)
        for i in route_data["routes"]:
            varreturn.append(f"""{nomeDaRota} {int((i["summary"]["travelTimeInSeconds"])/60)} minutos""")
    else:
        print('Erro ao fazer a solicitação:', response.status_code)
    return varreturn

def verrotas():
    x = []
    for i in caminhos:       
        x.append(medir_rota(i[0],i[1],i[2]))

        #medir_rota(i[0],i[1],i[2])
    return x
verrotas()

#site das coordenadas: https://wego.here.com/discover/belem?map=-1.42841,-48.46095,15.74,omv