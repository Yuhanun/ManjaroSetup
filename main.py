import os

with open("pkglist.txt") as pkg_file:
    packman_packages = [line.strip() for line in pkg_file.readlines()]

for package in packman_packages:
    if os.system(f"yes | sudo pacman -S {package} --needed") == 0:
        continue
    with open("failed_pkglist.txt", 'a') as failed_file:
        failed_file.write(f"{package}\n")

with open("requirements.txt") as pip_file:
    pip_modules = [line.strip() for line in pip_file.readlines()]

for module in pip_modules:
    if os.system(f"pip install {module} --user") == 0:
        continue

    with open("failed_requirements.txt", 'a') as failed_file:
        failed_file.write(f"{package}\n")

os.system("sudo pacman -Syu")
