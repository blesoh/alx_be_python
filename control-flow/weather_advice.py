#This script will ask the user about the,
# current weather conditions and provide, 
# clothing recommendations based on the input.
current_weather = str(input("Whats the weather like today? (sunny, rainy, cold) "))
if current_weather == "sunny":
    print(" Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Just stay indooers no weather recommendation for you LOL!!")

