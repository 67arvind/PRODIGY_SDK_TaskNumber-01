# Temperature Conversion Program
# This program converts temperatures between Celsius, Fahrenheit, and Kelvin.

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """
    Converts Celsius to Kelvin.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Kelvin.
    """
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """
    Converts Fahrenheit to Kelvin.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Kelvin.
    """
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    """
    Converts Kelvin to Celsius.
    
    Parameters:
    kelvin (float): Temperature in Kelvin.
    
    Returns:
    float: Temperature in Celsius.
    """
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """
    Converts Kelvin to Fahrenheit.
    
    Parameters:
    kelvin (float): Temperature in Kelvin.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    """
    Converts a temperature value from one unit to the other two units.
    
    Parameters:
    value (float): The temperature value to be converted.
    unit (str): The original unit of the temperature ('C', 'F', or 'K').
    
    Returns:
    None
    """
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    """
    Main function to run the Temperature Conversion Program.
    
    It prompts the user to input a temperature value and the unit of measurement,
    then converts the temperature to the other two units and displays the results.
    
    Returns:
    None
    """
    print("Welcome to the Temperature Conversion Program!")
    
    try:
        # Prompt user for temperature value
        temperature = float(input("Enter the temperature value: "))
        
        # Prompt user for the unit of measurement and convert it to uppercase
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        
        # Convert the temperature and display the results
        convert_temperature(temperature, unit)
    
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
