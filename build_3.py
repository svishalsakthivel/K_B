import os


def update_git_lfs_submodule():
    os.chdir("/root/vishal/tensorrtllm_backend")
    os.system("git lfs install")
    os.system("git submodule update --init --recursive")
