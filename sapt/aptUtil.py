import logging
import sys
import subprocess
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def prm():
    install = sys.argv
    subprocess.run(f"sudo apt-get purge {install}", shell=True)
    subprocess.run(f"sudo apt-get autoremove")
