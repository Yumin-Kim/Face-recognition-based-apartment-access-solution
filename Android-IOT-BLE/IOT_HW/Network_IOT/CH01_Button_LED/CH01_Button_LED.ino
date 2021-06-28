#define BUTTON 7
#define LED 12

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON,INPUT);
  pinMode(LED,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(BUTTON) == HIGH){
    digitalWrite(LED,HIGH);
    delay(500);
    digitalWrite(LED,LOW);
  }
}
