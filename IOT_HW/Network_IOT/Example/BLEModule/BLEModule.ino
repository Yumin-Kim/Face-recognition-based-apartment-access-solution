#include <DHT.h>
#include <DHT_U.h>

#include <SoftwareSerial.h>  // 소프트웨어 시리얼 라이브러리 
#define rxPin 3 

#define txPin 2 
#define LedPin 13
#define LEDSWITH 11
#define SWITH 12
#define DHTPIN 7      // DHT핀을 2번으로 정의한다(DATA핀)

#define DHTTYPE DHT11  // DHT타입을 DHT11로 정의한다

DHT dht(DHTPIN, DHTTYPE);  // DHT설정 - dht (디지털2, dht11)
SoftwareSerial btSerial(rxPin,txPin); // SoftwareSerial NAME(TX, RX);

 

void setup() {
  Serial.begin(9600);   //시리얼모니터
  btSerial.begin(9600); //블루투스 시리얼
  pinMode(LedPin,OUTPUT);
 // pinMode(LEDSWITH,OUTPUT);
//  pinMode(SWITH,INPUT);
}

 
char data;
void loop() {

  if (btSerial.available()) {  
    data = btSerial.read();
    Serial.write(data);
    if(data == '1'){
      digitalWrite(LedPin, HIGH);
    }
    if(data == '2'){
      digitalWrite(LedPin, LOW);
    }

  }  

  if (Serial.available()) {         
    btSerial.write(Serial.read());  //시리얼 모니터 내용을 블루투스 측에 쓰기
   
  }

  /*
  if(digitalRead(SWITH)){
    digitalWrite(LEDSWITH,HIGH);
    btSerial.println("Turn on");

    btSerial.flush();
    delay(500);
    digitalWrite(LEDSWITH,LOW);
  }
  int h = dht.readHumidity();  // 변수 h에 습도 값을 저장 
*/

}
