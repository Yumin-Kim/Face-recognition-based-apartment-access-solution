#define RED 11
#define GREEN 10
#define BLUE 9
#define RED_BUTTON 4
#define GREEN_BUTTON 3
#define BLUE_BUTTON 2

int r = 0 , g = 0 , b = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(RED_BUTTON,INPUT);
  pinMode(GREEN_BUTTON,INPUT);
  pinMode(BLUE_BUTTON,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(RED_BUTTON)==HIGH)
  {
    ++r;
    if(r>255)
      r = 0;
  }
  if(digitalRead(GREEN_BUTTON)==HIGH)
  {
    ++g;
    if(g>255)
      g = 0;
  }
  if(digitalRead(BLUE_BUTTON)==HIGH)
  {
    ++b;
    if(b>255)
      b = 0;
  }

  analogWrite(RED,r);
  analogWrite(GREEN,g);
  analogWrite(BLUE,b);
  delay(10); 
}
