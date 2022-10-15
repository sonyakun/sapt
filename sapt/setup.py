from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
setup(
    name="sapt",
    version="0.0.1",
    description="aptコマンド支援ツール",
    author="sonyakun",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "sapt insrm=aptUtil:insrm",
        ]
)
