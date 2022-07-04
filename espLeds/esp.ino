#define FASTLED_INTERNAL
#include <FastLED.h>

#define DATA_PIN 4
#define CLOCK_PIN 3


const int analogInPin = A0;

int sensorValue = 0;
void setup(void){
	Serial.begin(9600);


}

CRGB leds[14];

void loop(void)
{
	sensorValue = analogRead(analogInPin);
	FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, 14);

	int count = 0;
	while (true){

	count = (525 - sensorValue) / 35;

	if (sensorValue < 525)
	{
		for (int i = 0; i < count; i++)
		{
			leds[i] = CRGB::Yellow;
		}

	FastLED.show();
	FastLED.clear();
	}
	}


}