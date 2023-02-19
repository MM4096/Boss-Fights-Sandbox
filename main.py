import os

import wget
import zipfile

# URLs to download from
launcherVersion = "https://drive.google.com/uc?export=download&confirm=yTib&id=1ZT3hfLbfxrMWiCjZhThsnlaKOPdq2R1k"
launcherData = "https://drive.google.com/uc?export=download&confirm=yTib&id=1j35z5ffBeykcd_uJ6SLZts40Dg6HJKup"
game3dVersion = "https://drive.google.com/uc?export=download&confirm=yTib&id=1PymW-_1ZqzQcs0HO9s1hy17w7Ez9k1pW"
game3dData = "https://drive.google.com/uc?export=download&confirm=yTib&id=1vWHgCsXdCxif2qs1U7jpR0l926XaugEX"
game2dVersion = "https://drive.google.com/uc?export=download&confirm=yTib&id=17h6tLvjUE8AT9U-kIqWQYRTddNu-gXEU"
game2dData = "https://drive.google.com/uc?export=download&confirm=yTib&id=11U7lW7WdffKjmRsvXL73rGKP_V1JwABP"


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


def Run3D():
    PopupText("Checkin for updates")
    if not os.path.exists("Data/3DV.txt"):
        savedVersion = "0.0.0"
    else:
        with open("Data/3DV.txt", "r") as file1:
            savedVersion = file1.readline()
        os.remove("Data/3DV.txt")
    wget.download(game3dVersion, "Data/3DV.txt")
    print("")
    with open("Data/3DV.txt", "r") as file2:
        onlineVersion = file2.readline()
    if not onlineVersion == savedVersion:
        PopupText("Downloading new version")
        DeleteAll("Data/Game/3d")
        wget.download(game3dData, "Data/Game/3d/game.zip")
        print("")
        PopupText("Unzipping")
        with zipfile.ZipFile("Data/Game/3d/game.zip", "r") as gameZip:
            gameZip.extractall("Data/Game/3d")
    os.popen("Data/Game/3d/Boss Fights 3D.exe")


def Run2D():
    os.system('cls')
    print("Checking for updates...")
    if not os.path.exists("Data/2DV.txt"):
        savedVersion = "0.0.0"
    else:
        with open("Data/2DV.txt", "r") as file1:
            savedVersion = file1.readline()
        os.remove("Data/2DV.txt")
    wget.download(game2dVersion, "Data/2DV.txt")
    print("")
    with open("Data/2DV.txt", "r") as file2:
        onlineVersion = file2.readline()
    if not onlineVersion == savedVersion:
        print("Deleting old version")
        DeleteAll("Data/Game/2d")
        print("New update!")
        print("Downloading Boss Fights 2D.zip")
        wget.download(game2dData, "Data/Game/2d/game.zip")
        print("")
        print("Extracting")
        with zipfile.ZipFile("Data/Game/2d/game.zip", "r") as gameZip:
            gameZip.extractall("Data/Game/2d")
    os.popen("Data/Game/2d/Boss Fights.exe")


if __name__ == "__main__":
    if os.path.exists("placeholder.exe"):
        os.remove("placeholder.exe")
    if not (os.path.exists("Data")):
        os.makedirs("Data")
    if not (os.path.exists("Data/Game")):
        os.makedirs("Data/Game")
    if not (os.path.exists("Data/Game/2d")):
        os.makedirs("Data/Game/2d")
    if not (os.path.exists("Data/Game/3d")):
        os.makedirs("Data/Game/3d")
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
        os.system("launcher.exe")
