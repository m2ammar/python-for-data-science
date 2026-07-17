def get_advisory(temp):
    # your logic here
    
    if temp < 10:
        return "cold, wear a jacket"
    elif 10 <= temp < 25: 
        return "mild, light clothing is fine"
    elif 25 <= temp < 35:
        return "warm, stay hydrated"
    elif temp >= 35:
        return "hot, avoid going out at noon"   


def main():
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    temp = float(input("Enter current temperature (Celsius): "))
    
    
    # call get_advisory and print the final formatted sentence
    
    print(f"Hey {name}, it's {temp:g}°C in {city} today -  {get_advisory(temp)}.")

main()