import mainframe, sys, requests, os
from PyQt5.QtWidgets import QApplication
from git import Repo

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/Cedric-X02/peditor/main/version.txt"
    r = requests.get(url)
    version = r.text
    with open("version.txt", "r") as f:
        aversion = f.read()
    if version == aversion:
        files = os.listdir(".")
        flist = []
        for file in files:
            if file not in [".git", "main.pyw", "__pycache__"]:
                flist += file
                os.remove(file)

            url = f"https://raw.githubusercontent.com/Cedric-X02/peditor/main/{file}"
            r = requests.get(url)
            with open(f"./{file}", "w") as f:
                f.write(r.content)

            

    #app = QApplication(sys.argv)
    #ui = mainframe.Main()
    #ui.show()
    #app.exec_()