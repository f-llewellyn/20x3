#20x3: A python application that will help with the 20-20-20 method of reducing eye strain
from win10toast import ToastNotifier #Imports toastNotifier from win10toast
import time # Imports time module
import os

toaster = ToastNotifier() #Sets a shorthand key for ToastNoatifier func
title = "20x3: Rest your eyes!"
icon="./eye.ico/"

toaster.show_toast(
    "20x3: Rest your eyes!",
    "Welcome to 20x3. You'll receive a notification every 20 mins to rest your eyes.",
    duration=30,
    icon_path=icon,
)

while True: #Infinite loop
    time.sleep(1200) #Wait 20 mins

    #Look away notification
    toaster.show_toast( #Show notification
        "20x3: Rest your eyes!",
        "Look away for 20 seconds.", # Message
        icon_path=icon, # Path to icon
        duration=20 # #Duration in seconds
    )
    
    #Look back notifiacation
    toaster.show_toast( # Show notification
        "20x3: Rest your eyes!",
        "You can look back now", # Message
        icon_path=icon, # Path to icon
    )