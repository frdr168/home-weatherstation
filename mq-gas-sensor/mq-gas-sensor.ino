//Revision 1.0 (2016-04-25)
// Remove not use code,fix the data format
// Output format:
// Starting
// Sensor|1|APIN:A0|MQ135|82|ppm|DPIN:D2|0|
// Stop


#define XSTR(s) STR(s)
#define STR(s) #s
#define DIGITAL_IN_PIN  2   // define the digital input pin
#define ANALOG_IN_PIN   A0  // define the analog input pin

/*-----( Declare objects )-----*/
//NONE YET

/*-----( Declare Variables )-----*/
int digitalValue ;  // read digital value
//float sensorValue;  // read analoog value
int sensorValue;

void setup()   /****** SETUP: RUNS ONCE ******/
{
  pinMode (DIGITAL_IN_PIN, INPUT) ;// digital input signal (Not actually required; INPUT is default)
  pinMode (ANALOG_IN_PIN, INPUT)  ;// analog  input signal (Not actually required; INPUT is default)
  Serial.begin(9600);              // Start the Serial Monitor connection
  delay(100);
  //Serial.println("YourDuino.com MQ Gas Sensor Test ");
}//--(end setup )---


void loop()   /****** LOOP: RUNS CONSTANTLY ******/
{
  sensorValue = analogRead(ANALOG_IN_PIN);
  Serial.print("Starting");
  Serial.println("");
  Serial.print("Sensor|1|APIN:");
  Serial.print(XSTR(ANALOG_IN_PIN));
  Serial.print("|MQ135|");
  Serial.print(sensorValue, DEC); // display analog value
  Serial.print("|ppm|");

  digitalValue = digitalRead (DIGITAL_IN_PIN) ;

  Serial.print("DPIN:D");
  Serial.print(XSTR(DIGITAL_IN_PIN));
  Serial.print("|");
  Serial.print(digitalValue, DEC); // display digital value
  Serial.println("|");
  Serial.println("Stop");

  //if (digitalValue == LOW) // Gas Sensor Module is active LOW when alarmed
  //{
  //  Serial.println(" ALARM! ");
  // }
  //else
  //{
  //  Serial.println();
  //}


  delay(5000);

}//--(end main loop )---
