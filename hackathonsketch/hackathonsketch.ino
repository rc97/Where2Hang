// Defines the pins to which the light sensor and LED are connected.
const int pinLight = A1;
const int pinLed   = 7;

// Defines the light-sensor threshold value below which the LED will turn on.
// Decrease this value to make the device more sensitive to ambient light, or vice-versa.
int thresholdvalue = 400;

const int pinTemp = A2;

// Define the B-value of the thermistor.
// This value is a property of the thermistor used in the Grove - Temperature Sensor,
// and used to convert from the analog value it measures and a temperature value.
const int B = 3975;

// Define the pins to which the sound sensor and LED are connected.
const int pinSound = A0;

// Define the sound level above which to turn on the LED.
// Change this to a larger value to require a louder noise level.
int soundThresh = 500;

void setup()
{
    // Configure the LED's pin for output signals.
    pinMode(pinLed, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    // Read the value of the light sensor. The light sensor is an analog sensor.
    int lightValue = analogRead(pinLight);
    Serial.println(lightValue);

    // Turn the LED on if the sensor value is below the threshold.
    if(lightValue < thresholdvalue)
    {
        digitalWrite(pinLed, HIGH);
    }
    else
    {
        digitalWrite(pinLed, LOW);
    }
    
    // Get the (raw) value of the temperature sensor.
    int val = analogRead(pinTemp);

    // Determine the current resistance of the thermistor based on the sensor value.
    float resistance = (float)(1023-val)*10000/val;

    // Calculate the temperature based on the resistance value.
    float temperature = 1/(log(resistance/10000)/B+1/298.15)-273.15;

    // Print the temperature to the serial console.
    Serial.println(temperature);
    
    // Read the value of the sound sensor.
    int soundValue = analogRead(pinSound);
    Serial.println(soundValue);

    // If the measured sound level is above the threshold, blink the LED.
    if(soundValue > soundThresh)
    {
        // Turn the LED on for 200ms, then turn it back off.
        digitalWrite(pinLed,HIGH);
        digitalWrite(pinLed,LOW);
    }

    // Wait one second between measurements.
    delay(1000);
}

