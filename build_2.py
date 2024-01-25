import os


def install_git_lfs():
    os.chdir("/root/vishal/tensorrtllm_backend")
    os.system("apt-get update")
    os.system("apt install git-lfs")
