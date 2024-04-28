import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API da TomTom
api_key = 'jRJzo9EsGRhQol947cFzSrGNzIYPAsCH'

caminhos = ["Pedro Alvares Cabral - Doca:",'-1.40932,-48.4489','-1.43663,-48.49174'], ["Duque de Caixias - Doca: ",'-1.40951,-48.46381','-1.44609,-48.48798']

def medir_rota(rota,partida, destino):

    # Ponto de partida (latitude e longitude)
    start_point = partida

    # Ponto de chegada (latitude e longitude)
    end_point = destino

    # Construa a URL da solicitação de roteamento
    url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_point}:{end_point}/json?key={api_key}&traffic=true'

    # Faça a solicitação HTTP GET
    response = requests.get(url)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Processar os dados da resposta (em formato JSON)
        route_data = response.json()
        # Aqui você pode extrair informações sobre a rota, como distância, tempo de viagem, etc.
        # print(route_data)
        for i in route_data["routes"]:
            print(f"""
                    {rota} {int((i["summary"]["travelTimeInSeconds"])/60)} minutos
                    """
                    #distancia: {(i["summary"]["lengthInMeters"])/1000} KM,
                    # atrasos devido a engarrafamentos: {i["summary"]["trafficDelayInSeconds"]} segundos,
                    # Saida: {i["summary"]["departureTime"]},
                    # chegada: {i["summary"]["arrivalTime"]}"
                    
            )
    else:
        print('Erro ao fazer a solicitação:', response.status_code)

for i in caminhos:
    medir_rota(i[0],i[1],i[2])

#site das coordenadas: https://wego.here.com/discover/belem?map=-1.42841,-48.46095,15.74,omv