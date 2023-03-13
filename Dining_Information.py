"""
Program: SDEV140 Final Project - Dining Request Screen
Author: Lora Sparks
Program asks and accepts input of traveler 1 and 2
dining preferences for their travel.
"""
import tkinter as tk
import tkinter.messagebox
import subprocess

from PIL import ImageTk,Image

# Create instance of tkinter frame or window
root = tk.Tk()
root.title("Dining Information")

# Function to enter traveler information
def call_to_travelers():
     subprocess.run(["python", "SparksLoraFinalProject.py"])
     
# Function to enter activities information
def call_to_activities():
     subprocess.run(["python", "Activities_Information.py"])

# Function to save information
def call_to_save():
     f = open("Aruba_Traveler_Info.csv", "a")
     f.write("The traveler information has been saved.")
     f.close()

     #open and read the file after the appending:
     f = open("Aruba_Traveler_Info.csv", "r")
     print(f.read())
     
"""
This area refers to the dining options window
"""

# Display images on dining
img4 = ImageTk.PhotoImage(Image.open("AUAAPB_open_restaurant.jpg"))
tk.Label(root, image=img4).grid(row=0, column=0)
img5 = ImageTk.PhotoImage(Image.open("AUAAPB_restaurant.jpg"))
tk.Label(root, image=img5).grid(row=0, column=1)
img6 = ImageTk.PhotoImage(Image.open("AUAAPB_restaurant2.jpg"))
tk.Label(root, image=img6).grid(row=0, column=2)

# Create labels to display instructions for dining information
tk.Label(root, text="Grill & Steakhouse").grid(row=1, column=0)
tk.Label(root, text="Milano - Italian Restaurant").grid(row=1, column=1)
tk.Label(root, text="Sayuri - Japanese Restaurant").grid(row=1, column=2)
tk.Label(root, text="   ").grid(row=2)
tk.Label(root, text="Friday Restaurant Selection: ").grid(row=3, column=0)
tk.Label(root, text="Saturday Restaurant Selection: ").grid(row=3, column=1)
tk.Label(root, text="Sunday Restaurant Selection: ").grid(row=3, column=2)
tk.Label(root, text="  ").grid(row=4)
tk.Label(root, text="  ").grid(row=6)

#Set the Menu initially
menu1= tk.StringVar()
menu1.set("Friday Restaurant Selection: ")

menu2= tk.StringVar()
menu2.set("Saturday Restaurant Selection: ")

menu3= tk.StringVar()
menu3.set("Sunday Restaurant Selection: ")

#Create a dropdown Menu
drop1= tk.OptionMenu(root, menu1,"Krystal - Fusion restaurant", "Sayuri - Japanese restaurant",
                     "Milano - Italian restaurant","Grill and steakhouse").grid(row=5, column=0)

drop2= tk.OptionMenu(root, menu2,"Krystal - Fusion restaurant", "Sayuri - Japanese restaurant",
                     "Milano - Italian restaurant","Grill and steakhouse").grid(row=5, column=1)

drop3= tk.OptionMenu(root, menu3,"Krystal - Fusion restaurant", "Sayuri - Japanese restaurant",
                     "Milano - Italian restaurant","Grill and steakhouse").grid(row=5, column=2)

# Create buttons to call the desired display
exit_button = tk.Button(root, text="Exit",
                          command=root.quit).grid(row=15,column=0)                           

activity_button = tk.Button(root, text="Select Activity Preferences",
                          command=call_to_activities).grid(row=15,column=1)

traveler_button = tk.Button(root, text="Traveler Information",
                            command=call_to_travelers).grid(row=15,column=2)
save_button = tk.Button(root, text="Save Information",
                            command=call_to_save).grid(row=15,column=3)
# Run the main loop
root.mainloop()
