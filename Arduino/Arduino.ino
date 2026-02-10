const int X_PIN = A0;
const int Y_PIN = A1;
const int SW_PIN = 3; // <---tự sửa thành cổng mà bạn cắm SW vào nhé ở đây mình cắm ở pin 3(Change this into the pin that you connect the SW to)

void setup() {
  Serial.begin(9600); 
  
  pinMode(SW_PIN, INPUT_PULLUP); 
}

void loop() {
  int xVal = analogRead(X_PIN);
  int yVal = analogRead(Y_PIN);
  int swState = digitalRead(SW_PIN);

  
  if (yVal < 200) {
    Serial.println("UP"); 
    delay(200);
  } 
  else if (yVal > 800) {
    Serial.println("DOWN"); 
    delay(200);
  }
  else if (xVal < 200) {
    Serial.println("LEFT"); 
    delay(400);
  }
  
  if (swState == LOW) {
    Serial.println("CLICK"); 
    delay(500); 
  }
}