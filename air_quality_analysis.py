# Air Quality Analysis Using Python
# Sample data for learning purposes only

data = {
    "Chennai": 85,
    "Delhi": 160,
    "Mumbai": 72,
    "Bengaluru": 48,
    "Hyderabad": 110
}

print("AIR QUALITY ANALYSIS")
print("--------------------")

total = 0

for city, aqi in data.items():
    print(city, ":", aqi)
    total += aqi

average = total / len(data)
print("\nAverage AQI:", average)

highest_city = max(data, key=data.get)
print("Highest AQI City:", highest_city)
print("Highest AQI Value:", data[highest_city])

print("\nCities with AQI above 100:")
for city, aqi in data.items():
    if aqi > 100:
        print(city, ":", aqi)
