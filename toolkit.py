## Grabbing an storing current date
import datetime
import time
import sys
current_date = datetime.datetime.now()

## App Info/Constants
var_app_name = "Toolkit v1"
var_app_description = "Description: Tool is for learning how to work with menu's and functions"
var_app_dev_name = "by: Austin Burkeen"
var_app_version = "v1.0" 
var_app_notes = "Type r to revert back to main menu!"

## Visual component variables
var_visual_welcome_top = "//     --   " + var_app_name + "                                                                              --      //"
var_visual_welcome_middle = "//     --   " + var_app_description + "           --      //" 
var_visual_welcome_bottom = "//     --   " + var_app_dev_name + "                                                                        --      //"
var_visual_welcome_version = "//     --   " + var_app_version + "                                                                                      --      //"
var_visual_welcome_bar = "----------------------------------------------------------------------------------------------------------------"

## Visual welcome component output 
print(var_visual_welcome_bar)
print(var_visual_welcome_bar)
print(var_visual_welcome_top)
print(var_visual_welcome_middle)
print(var_visual_welcome_bottom)
print(var_visual_welcome_version)
print(var_visual_welcome_bar)
print(var_visual_welcome_bar)

## Defining menu
def menu():
    print("What function are you looking to use? ")
    print("1 - Connect to Client")
    print("2 - Selection 2")
    print("3 - Selection 3")
    print("4 - Selection 4")
    print("5 - Selection 5")
    print("6 - Selection 6")
    print("7 - Selection 7")

## Menu loop
while True:
    menu()  # Add the function here.
    choice = int(input("Enter choice (1-7): "))  # Change here
    if choice == 1:
        print("The current date is: " + current_date)
    elif choice == 2:
        print(current_date)
    elif choice == 3:
        print(current_date)
    elif choice == 4:
        print(current_date)
    else:
        break

mainmenu()