
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(50,OUTPUT); //ron
  pinMode(51,OUTPUT); //coca cola
  pinMode(52,OUTPUT); //zumo de limon
  pinMode(53,OUTPUT); //sprite

}

void loop() {
  // put your main code here, to run repeatedly:
    if(Serial.available())
    {
      char numero = Serial.read();
      if(numero=='1')
      {
        // Mojito
        digitalWrite(50,HIGH);
        digitalWrite(53,HIGH);
        for(int i=0;i<6;i++){
         delay(1000); 
        }
        digitalWrite(50,LOW);
        digitalWrite(53,LOW);
        digitalWrite(52,HIGH);
        delay(1000);
        digitalWrite(52,LOW);
      }
      if(numero=='2')
      {
        //Cuba Libre
        digitalWrite(50,HIGH);
        digitalWrite(51,HIGH);
        for(int i=0;i<6;i++){
         delay(1000); 
        }
        digitalWrite(50,LOW);
        digitalWrite(51,LOW);
        digitalWrite(52,HIGH);
        delay(1000);
        digitalWrite(52,LOW);
      }
      
      if(numero=='3')
      {
        // Ron
        digitalWrite(50,HIGH);
        for(int i=0;i<6;i++){
         delay(1000); 
        }
        digitalWrite(50,LOW);
      }
      
      if(numero=='4')
      {
        //   CocaCola
        digitalWrite(51,HIGH);
        for(int i=0;i<12;i++){
         delay(1000); 
        }
        digitalWrite(51,LOW);
      }
      if(numero=='5')
      {
        // Sprite
        digitalWrite(53,HIGH);
        for(int i=0;i<12;i++){
         delay(1000); 
        }
        digitalWrite(53,LOW);
      }
      if(numero=='6')
      {
        // Sprite
        digitalWrite(52,HIGH);
        for(int i=0;i<12;i++){
         delay(1000); 
        }
        digitalWrite(52,LOW);
      }
    }
}
