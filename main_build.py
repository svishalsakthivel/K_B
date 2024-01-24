import build_1 as b1
import build_2 as b2
import build_3 as b3
import build_4 as b4

b1.download_s3_basket()
# b2.install_git_lfs()
b3.update_git_lfs_submodule()
b4.docker_build()
b4.docker_run()
