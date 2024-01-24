import os


def update_git_lfs_submodule():
    os.chdir("/root/vishal/t_b")
    os.system("git lfs install")
    os.system("git submodule update --init --recursive")
