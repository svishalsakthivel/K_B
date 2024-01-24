import os


def install_git_lfs():
    os.system("apt-get update")
    os.system("apt install git-lsf")
