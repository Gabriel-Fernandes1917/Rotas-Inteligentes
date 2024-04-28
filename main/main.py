import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API da TomTom
api_key = 'jRJzo9EsGRhQol947cFzSrGNzIYPAsCH'

# Ponto de partida (latitude e longitude)
start_point = '-1.455792,-48.490833'

# Ponto de chegada (latitude e longitude)
end_point = '-1.2921,-47.9267'  # Exemplo: Vaticano, Roma, Itália

# Construa a URL da solicitação de roteamento
url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_point}:{end_point}/json?key={api_key}'

# Faça a solicitação HTTP GET
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Processar os dados da resposta (em formato JSON)
    route_data = response.json()
    # Aqui você pode extrair informações sobre a rota, como distância, tempo de viagem, etc.
    # print(route_data)
    for i in route_data["routes"]:
        print(i)
else:
    print('Erro ao fazer a solicitação:', response.status_code)
