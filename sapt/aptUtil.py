import logging
import sys
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def purge():
    install = sys.argv
    subprocess.run(f"sudo apt-get purge {install}", shell=True)
    subprocess.run(f"sudo apt-get autoremove")

def install():
    install = sys.argv
    subprocess.run(f"sudo apt-get install software-properties-common")
    subprocess.run("sudo apt-get update")
    subprocess.run(f"sudo apt-get install -y {install}")

def setup():
    print("SakuraLinuxのセットアップを開始します。")
    yn = input("aptで全てのパッケージのインストールを開始します")
    subprocess.run("sudo apt-get update")
    subprocess.run("sudo apt update")
    subprocess.run("sudo apt-get install software-properties-common")
    subprocess.run(f"sudo apt install -y snapd", shell=True)
    subprocess.run("sudo snap install --devmode --beta anbox")
    subprocess.run("sudo dpkg --add-architecture i386")
    subprocess.run("wget -nc https://dl.winehq.org/wine-builds/winehq.key")
    subprocess.run("sudo apt-key add winehq.key")
    subprocess.run("sudo rm winehq.key")
    subprocess.run("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'")
    subprocess.run("sudo apt update")
    subprocess.run("sudo apt install winehq")
    print("完了しました。")
