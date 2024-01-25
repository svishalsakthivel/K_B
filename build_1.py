import os


def download_s3_basket():
    os.mkdir("/root/vishal")
    os.chdir("/root/vishal")
    os.system("aws --profile llm s3 cp s3://llm-spark/silicon/tensorrtllm_backend/ tensorrtllm_backend --recursive")
    # os.system("aws --profile llm s3 ls s3://llm-spark/silicon/tensorrtllm_backend/")
    # os.mkdir("/root/vishal/t_b")
