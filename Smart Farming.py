from abc import ABC, abstractmethod

# Kelas abstrak Plant
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name
        self.water_needs = water_needs
        self.fertilizer_needs = fertilizer_needs

    @abstractmethod
    def grow(self):
        pass

    def calculate_needs(self, rainfall, soil_moisture):
        # Logika penyesuaian kebutuhan air
        adjusted_water_needs = max(0, self.water_needs - rainfall * 0.5)
        
        # Logika penyesuaian kebutuhan pupuk (contoh: jika kelembapan rendah, pupuk lebih banyak)
        adjusted_fertilizer_needs = self.fertilizer_needs
        if soil_moisture < 50:
            adjusted_fertilizer_needs *= 1.2  # Tambah 20% jika kelembapan rendah

        # Simpan hasil yang disesuaikan
        self.water_needs = round(adjusted_water_needs, 2)
        self.fertilizer_needs = round(adjusted_fertilizer_needs, 2)

    def show_needs(self, rainfall, soil_moisture):
        print(f"{self.name} is growing in the field")
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        print(f"Adjusted Water Needs: {self.water_needs} liters")
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg\n")

# Kelas turunan RicePlant
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 5)  # Kebutuhan standar untuk tanaman padi

    def grow(self):
        print("Rice is growing in the paddy field")

# Kelas turunan CornPlant
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 18, 7)  # Kebutuhan standar untuk tanaman jagung

    def grow(self):
        print("Corn is growing in the farm")

# Simulasi kondisi cuaca
def simulate_weather():
    return [
        {"rainfall": 10, "soil_moisture": 75},  # Data untuk tanaman padi
        {"rainfall": 2, "soil_moisture": 40}     # Data untuk tanaman jagung
    ]

# Main Program
if __name__ == "__main__":
    rice = RicePlant()
    corn = CornPlant()

    weather_conditions = simulate_weather()

    # Simulasi tanaman padi
    rice.grow()
    rice.calculate_needs(weather_conditions[0]["rainfall"], weather_conditions[0]["soil_moisture"])
    rice.show_needs(weather_conditions[0]["rainfall"], weather_conditions[0]["soil_moisture"])

    # Simulasi tanaman jagung
    corn.grow()
    corn.calculate_needs(weather_conditions[1]["rainfall"], weather_conditions[1]["soil_moisture"])
    corn.show_needs(weather_conditions[1]["rainfall"], weather_conditions[1]["soil_moisture"])
