from talon import Module, actions, app
import os
from typing import List

def is_installed(name):
    talon_path = actions.path.talon_user()
    target_path = os.path.join(talon_path, name)
    return os.path.exists(target_path)

def install_repository(url, name):
    actions.insert("git clone " + url + " " + name)
    actions.key("enter")

def install_if_missing(url, name):
    if not is_installed(name):
        install_repository(url, name)
    
def install_repositories(repositories):
    for url, name in repositories:
        if is_installed(name):
            app.notify("Repository " + name + " already installed")
        else:
            install_repository(url, name)
            actions.sleep("10s")
        
main_repositories_to_install = [
    ("https://github.com/FireChickenProductivity/cursorless-settings", "cursorless-settings"),
    ("https://github.com/FireChickenProductivity/Viper-Settings", "Viper Settings"),
    ("https://github.com/FireChickenProductivity/MouseControlChicken", "MouseControlChicken"),
    ("https://github.com/FireChickenProductivity/PersonalCommunityFork", "community"),
    ("https://github.com/FireChickenProductivity/PersonalTalonVoiceCodingSetup", "PersonalTalonVoiceCodingSetup"),
    ("https://github.com/FireChickenProductivity/TalonHardSleep", "TalonHardSleep"),
    ("https://github.com/FireChickenProductivity/Viper", "Viper"),
    ("https://github.com/FireChickenProductivity/FireChickenContextSensitiveDictation", "FireChickenContextSensitiveDictation"),
    ("https://github.com/FireChickenProductivity/TalonVoiceDictationSetup", "DictationSetup"),
    ("https://github.com/FireChickenProductivity/Talon-Voice-multidimensional-clipboard", "MultidimensionalClipboard"),
    ("https://github.com/FireChickenProductivity/GoogleSheetsTalonCommands", "GoogleSheets"),
    ("https://github.com/FireChickenProductivity/TalonVoiceDesmosCommands", "Desmos"),
    ("https://github.com/FireChickenProductivity/ActionsForGeneratedCommands", "ActionsForGeneratedCommands"),
    ("https://github.com/FireChickenProductivity/RandomTalon", "RandomTalon"),
    ("https://github.com/FireChickenProductivity/Talon-Voice-Exam-Mode", "ExamMode"),
    ("https://github.com/FireChickenProductivity/cursorless-talon", "cursorless-talon"),
    ("https://github.com/FireChickenProductivity/BAR", "BAR"),
    ("https://github.com/FireChickenProductivity/Talon-Voice-EquatIO-Commands", "EquatIO"),
    ("https://github.com/FireChickenProductivity/TalonVoiceDiagramDrawing", "DiagramDrawing"),
]

module = Module()
@module.action_class
class Actions:
    def install_setup(repositories: List = main_repositories_to_install):
        """Installs the specified repositories"""
        install_repositories(repositories)
    
