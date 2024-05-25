
#include <WiFi.h>       
#include <HTTPClient.h> 

// config do WiFi
const char* ssid = "Fernandes";
const char* password = "w17l19g19";

void setup() {

  Serial.begin(115200);
  Serial.println();
  delay(1000);

  WiFi.disconnect(); 
  WiFi.mode(WIFI_STA);
  Serial.println("[SETUP] Tentando conexão com o WiFi...");
  WiFi.begin(ssid, password); // Conecta-se à rede
  if (WiFi.waitForConnectResult() == WL_CONNECTED) 
  {
    Serial.println("[SETUP] WiFi iniciado com sucesso!");
  } else
  {
    Serial.println("[SETUP] Houve falha na inicialização do WiFi. Reiniciando ESP.");
    ESP.restart();
  }

  HTTPClient http; 

  Serial.println("[HTTP] começar...");
  http.begin("http://192.168.0.14:5000/get_data"); //URL para fazer requisição

  Serial.println("[HTTP] GET...");
  int httpCode = http.GET(); // inicia uma conexão e envia um cabeçalho HTTP para o URL do servidor configurado
  Serial.print("[HTTP] GET... código: ");
  Serial.println(httpCode);
  if (httpCode == HTTP_CODE_OK) 
  {
    Serial.println("[HTTP] GET... OK! Resposta: ");

    String payload = http.getString(); // armazena a resposta da requisição
    Serial.println(payload); // imprime a resposta da requisição
  } else // se não, ...
  {
    Serial.print("HTTP GET... Erro. Mensagem de Erro: ");
    Serial.println(http.errorToString(httpCode).c_str()); // Imprime a mensagem de erro da requisição
  }

  http.end();// Fecha a requisição HTTP

  // entra em um laço de repetição infinito
  while (1);
}

void loop() {}