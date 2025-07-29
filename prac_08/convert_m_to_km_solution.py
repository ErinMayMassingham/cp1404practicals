from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# Constant for miles to kilometres conversion
MILES_TO_KM = 1.60934

class ConvertMilesKm(BoxLayout):
    km_output = StringProperty("0.0")

    def convert(self):
        """Convert miles to kilometres"""
        try:
            miles = float(self.ids.miles_input.text)
            self.km_output = f"{miles * MILES_TO_KM:.2f}"
        except ValueError:
            self.km_output = "0.0"

    def handle_increment(self, value):
        """Increase or decrease miles by 1"""
        try:
            miles = float(self.ids.miles_input.text)
        except ValueError:
            miles = 0
        miles += value
        self.ids.miles_input.text = str(miles)
        self.convert()

class ConvertMilesKmApp(App):
    def build(self):
        return ConvertMilesKm()

if __name__ == "__main__":
    ConvertMilesKmApp().run()
