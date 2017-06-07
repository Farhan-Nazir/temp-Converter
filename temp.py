# Temperature Converting Program 
# Author: Farhan Nazir
import math 

def fahrToCel():
     userInputFahr = float(input("Please Enter The Fahrenheit Temperature\n"))
     fahr = float(userInputFahr)
     cel = (fahr - 32.0) * 5.0 / 9.0
     resultFahr = math.floor(cel * 10) / 10
     print("Temperature in celsius is",resultFahr,"°C")

def celToFahr():
     userInputCel = float(input("Please Enter The Celsius Temperature\n"))
     cel = float(userInputCel)
     fahr = (cel * 9.0) / 5.0 + 32.0
     resultCel = math.floor(fahr * 10) / 10
     print("Temperature in Fahrenheit is",resultCel,"°F")
     
def selectTem():
      selStart = float(input(" Enter 1 to convert Fahrenheit to Celsius\n Enter 2 to convert Celsius to Fahrenheit\n"))
      if selStart == 1 :
        fahrToCel()
      elif selStart == 2:
        celToFahr()
      else:
        print("Program is shutting down due to invalid input")
        exit()
selectTem()



