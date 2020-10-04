int LED1 = D1;
int LED2 = D2;
int LED3 = D3;
int LED4 = D4;

 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("setup() START");
  
  pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
      pinMode(LED3, OUTPUT);
        pinMode(LED4, OUTPUT);
        
}
 
void loop() {
  // put your main code here, to run repeatedly:
 
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
  digitalWrite(LED3, HIGH);
  digitalWrite(LED4, HIGH);
  delay(1000);
  digitalWrite(LED1, LOW);
  delay(1000);
}
