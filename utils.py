import re

def validate_latitude():
    lat = input(f"Please enter the latitude: ")
    p = re.compile("^(\+|-)?(?:90(?:(?:\.0{1,10})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,10})?))$")
    m = p.match(lat)
    if m:
      return lat
    else:
      print("\n")
      print("Invalid latitude entered. Please enter a number within -90 , +90 and within 10 decimal places")
      lat = validate_latitude()

def validate_longitude():
    lon = input(f"Please enter the longitude: ")
    p = re.compile("^(\+|-)?(?:180(?:(?:\.0{1,10})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,10})?))$")
    m = p.match(lon)
    if m:
      return lon
    else:
      print("\n")
      print("Invalid longitude entered. Please enter a number within -180 , +180 and within 10 decimal places")
      lon = validate_longitude()