#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
import io
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Joke_Module import JokeSettings

#Import random number generator
import random
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Jokes script"
Website = "https://www.streamlabs.com"
Description = "JokesScript"
Creator = "f.oddera"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = JokeSettings()
lines = []
maxRand = 0
command = ""

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\\settings.json")
    ScriptSettings = JokeSettings(SettingsFile)

    global lines, maxRand, command
    with io.open(ScriptSettings.Path, mode="r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]
    maxRand = len(lines)
    command = ScriptSettings.Command
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.Message == command:
        Parent.SendStreamMessage(lines[random.randint(0, maxRand-1)])
   
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter","I am a cat!")
    
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

def Log(message):
    Parent.Log("Joke", message)
    return
