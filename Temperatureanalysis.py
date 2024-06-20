class TemperatureAnalyzer:
    def __init__(self):
        self.crop_data = {
            'Tomato': {'min_temp': 15, 'max_temp': 30},
            'Lettuce': {'min_temp': 10, 'max_temp': 25},
            'Wheat': {'min_temp': 5, 'max_temp': 20},
            'Corn': {'min_temp': 20, 'max_temp': 35},
            'Potato': {'min_temp': 10, 'max_temp': 25},
            'Soybean': {'min_temp': 20, 'max_temp': 30},
            'Cabbage': {'min_temp': 10, 'max_temp': 25}
        }

    def recommend_crops(self, temperature):
        suitable_crops = []
        for crop, temp_range in self.crop_data.items():
            if temp_range['min_temp'] <= temperature <= temp_range['max_temp']:
                suitable_crops.append(crop)
        return suitable_crops


class SoilSample:
    def __init__(self, nitrogen, phosphorus, potassium):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium


class PlantDatabase:
    def __init__(self):
        self.plant_data = {
            'Tomato': {'nitrogen': (0.5, 0.8), 'phosphorus': (0.3, 0.6), 'potassium': (0.4, 0.7)},
            'Lettuce': {'nitrogen': (0.4, 0.7), 'phosphorus': (0.2, 0.4), 'potassium': (0.3, 0.6)},
            'Carrot': {'nitrogen': (0.3, 0.6), 'phosphorus': (0.2, 0.5), 'potassium': (0.3, 0.6)}
        }

    def recommend_plant(self, soil_sample):
        recommended_plants = []
        for plant, ranges in self.plant_data.items():
            if (ranges['nitrogen'][0] <= soil_sample.nitrogen <= ranges['nitrogen'][1] and
                ranges['phosphorus'][0] <= soil_sample.phosphorus <= ranges['phosphorus'][1] and
                ranges['potassium'][0] <= soil_sample.potassium <= ranges['potassium'][1]):
                recommended_plants.append(plant)
        return recommended_plants


# Example usage:
temperature = 25
soil_sample = SoilSample(nitrogen=0.6, phosphorus=0.4, potassium=0.5)

analyzer = TemperatureAnalyzer()
recommended_crops = analyzer.recommend_crops(temperature)

if recommended_crops:
    print("Recommended crops based on the temperature of", temperature, "°C:")
    for crop in recommended_crops:
        print("-", crop)
else:
    print("No crops recommended for the temperature of", temperature, "°C.")

plant_db = PlantDatabase()
recommended_plants = plant_db.recommend_plant(soil_sample)

if recommended_plants:
    print("\nRecommended plants based on soil sample:")
    for plant in recommended_plants:
        print("-", plant)
else:
    print("\nNo plants recommended for the given soil sample.")
