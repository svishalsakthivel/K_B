import os


def docker_build():
    os.system("cp /root/vishal_build/Dockerfile.trt_llm_backend  ~/vishal/tensorrtllm_backend/dockerfile/Dockerfile.trt_llm_backend")
    os.chdir("/root/vishal/tensorrtllm_backend")
    os.system("DOCKER_BUILDKIT=1 docker build -t triton_trt_llm_v1 -f dockerfile/Dockerfile.trt_llm_backend .")
    # os.system("DOCKER_BUILDKIT=1 docker build -t triton_trt_llm_vishal -f dockerfile/Dockerfile.trt_llm_v .")


def docker_run():
    os.system(
        "docker run --rm -it --net host --shm-size=2g --ulimit memlock=-1 --ulimit stack=67108864  --gpus='"'device=0'"' -v /local/si/silicon/FT:/FT -v /local/s3/mountvolume:/dynamic -v /local/si/silicon/tensorrtllm_backend:/tensorrtllm_backend triton_trt_llm bash"
)
