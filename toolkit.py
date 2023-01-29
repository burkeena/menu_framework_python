## Import modules
import datetime
import time
import sys
import os

current_date = datetime.datetime.now()

## App Info
var_app_name = "Menu Toolkit v1"
var_app_description = "Description: Tool is for learning how to work with with a basic menu and functions"
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

## Functions
def print_date_function():
    print("The current date is: " + str(current_date)) ## Convert current_date from int to string

def ping_google_function():
    hostname = "google.com" #example
    response = os.system("ping -c 10 " + hostname)


#and then check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')

def ifconfig_function():
    print(os.system("ifconfig"))

def netstat_function():
    print(os.system("netstat"))


## Defining menu
def menu():
    print("What function are you looking to use? ")
    print("1 - Print current date")
    print("2 - Ping google.com")
    print("3 - Run ifconfig")
    print("4 - Run netstat")
    print("5 - Selection 5")
    print("6 - Selection 6")
    print("7 - Selection 7")

## Menu loop
while True:
    menu()  # Add the function here.
    choice = int(input("Enter choice (1-7): "))  # Change here
    if choice == 1:
        print_date_function()
        break
    elif choice == 2:
        ping_google_function()
    elif choice == 3:
        ifconfig_function()
    elif choice == 4:
        netstat_function()
    else:
        break

menu()