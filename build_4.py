import os


def docker_build():
    # os.system("DOCKER_BUILDKIT=1 docker build -t triton_trt_llm -f dockerfile/Dockerfile.trt_llm_backend .")
    os.system("DOCKER_BUILDKIT=1 docker build -t triton_trt_llm_vishal -f dockerfile/dockerfile.vishal_trt_llm .")


def docker_run():
    os.system(
        "docker run --rm -it --net host --shm-size=2g --ulimit memlock=-1 --ulimit stack=67108864  --gpus='"'device=0'"' -v /local/si/silicon/FT:/FT -v /local/s3/mountvolume:/dynamic -v /local/si/silicon/tensorrtllm_backend:/tensorrtllm_backend triton_trt_llm_vishal")
