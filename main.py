import ast
import os
import time

import wget
import zipfile

# URLs to download from

versions = ""
launcherVersion = "https://drive.google.com/uc?export=download&confirm=yTib&id=1FFTtpXrndeUmc2Xk24fuGwpuDteOpmV5"
launcherData = "https://drive.google.com/uc?export=download&confirm=yTib&id=1qrpe0llZtW-_Pc8Lw_tWTllHh0ynKe6p"
gameLink = "https://drive.google.com/uc?export=download&confirm=yTib&id=1vC4p82IkcZIndnn9vD8sgSnFcz0pv3Tr"


def DeleteAll(path):
    dirs = os.listdir(path)
    for fod in dirs:
        if os.path.isdir(os.path.join(path, fod)):
            print("New directory found: " + path + "/" + fod)
            DeleteAll(os.path.join(path, fod))
            print("Deleting " + path + "/" + fod)
            os.rmdir(os.path.join(path, fod))
        else:
            print("Deleting " + path + "/" + fod)
            os.remove(os.path.join(path, fod))


def MainApp():
    running = True
    while running:
        currentVersions = list(versions.keys())
        printStr = "What version of game would you like to run?\nlts\n"
        for version in currentVersions:
            printStr = printStr + version + "\n"
        printStr = printStr + "(input)\n"
        versionToRun = input(printStr)
        if versionToRun == "lts":
            versionToRun = currentVersions[0]
        path = os.path.join("Data", "Game", versionToRun)
        try:
            if os.path.exists(path):
                print("has version")
            else:
                link = versions[versionToRun]
                print("added")
                os.mkdir(path)
                wget.download(link, path + "/game.zip")
                with zipfile.ZipFile(path + "/game.zip", "r") as gameZip:
                    gameZip.extractall("Data/Game/" + versionToRun)
            os.startfile(path + "/BossFightsSandBox.exe")
            print("Troubleshooting:")
            print("If the game doesn't run, try deleting the folder containing the game")
            time.sleep(120)
            a = 0 / 0
        except KeyError:
            os.system("cls")
            print("Version doesn't exist!")


if __name__ == "__main__":
    if os.path.exists("placeholder.exe"):
        os.remove("placeholder.exe")
    if not (os.path.exists("Data")):
        os.makedirs("Data")
    if not (os.path.exists("Data/Game")):
        os.makedirs("Data/Game")
    print("Checking for launcher updates...")
    if not os.path.exists("Data/launcherVersion.txt"):
        currentLauncherVersion = 0
        wget.download(launcherVersion, "Data/launcherVersion.txt")
        print("")
    else:
        with open("Data/launcherVersion.txt", "r") as file:
            currentLauncherVersion = file.readline()
    os.remove("Data/launcherVersion.txt")
    wget.download(launcherVersion, "Data/launcherVersion.txt")
    print("")
    with open("Data/launcherVersion.txt", "r") as file:
        onlineLauncherVersion = file.readline()
    print("")
    if not onlineLauncherVersion == currentLauncherVersion:
        print("A new launcher update is available! This will start downloading.")
        input("The launcher will start after download. Press [enter] to proceed")
        print("Renaming current")
        print("Downloading")
        os.rename("launcher.exe", "placeholder.exe")
        wget.download(launcherData, "launcher.exe")
        print("")
        os.remove("placeholder.exe")
        os.startfile("launcher.exe")

    print("Gathering launch codes...")
    if os.path.exists("Data/downloadLinks.BFData"):
        os.remove("Data/downloadLinks.BFData")
    wget.download(gameLink, "Data/downloadLinks.BFData")
    print("")
    with open("Data/downloadLinks.BFData", "r") as file:
        versions = ast.literal_eval(file.read())
    MainApp()
