import logging
import sys
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def purge():
    install = sys.argv
    subprocess.run(f"sudo apt-get purge {install}", shell=True)
    subprocess.run(f"sudo apt-get autoremove", shell=True)

def install():
    install = sys.argv
    subprocess.run(f"sudo apt-get install software-properties-common", shell=True)
    subprocess.run("sudo apt-get update", shell=True)
    subprocess.run(f"sudo apt-get install -y {install}", shell=True)

def setup():
    print("SakuraLinuxのセットアップを開始します。")
    yn = input("aptで全てのパッケージのインストールを開始します")
    subprocess.run("sudo apt-get update", shell=True)
    subprocess.run("sudo apt update", shell=True)
    subprocess.run("sudo apt-get install software-properties-common", shell=True)
    subprocess.run(f"sudo apt install -y snapd", shell=True)
    subprocess.run("sudo snap install --devmode --beta anbox", shell=True)
    subprocess.run("sudo dpkg --add-architecture i386", shell=True)
    subprocess.run("wget -nc https://dl.winehq.org/wine-builds/winehq.key", shell=True)
    subprocess.run("sudo apt-key add winehq.key", shell=True)
    subprocess.run("sudo rm winehq.key", shell=True)
    subprocess.run("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'", shell=True)
    subprocess.run("sudo apt update", shell=True)
    subprocess.run("sudo apt install winehq", shell=True)
    print("完了しました。")
