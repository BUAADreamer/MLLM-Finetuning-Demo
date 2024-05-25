import json

with open("data/mllm_demo.json") as f:
    examples = json.loads(f.read())

import huggingface_hub

huggingface_hub.login("hf_xxxxx")  # 替换为你自己的key从而登录hf

from datasets import Dataset, Features, Image, Sequence, Value


def gen():
    for data in examples:
        yield data


# 构建数据集feature
features = Features(
    {
        'messages': [
            {
                'role': Value(dtype='string', id=None),
                'content': Value(dtype='string', id=None),
            }
        ],
        'images': Sequence(feature=Image(decode=True, id=None), length=-1, id=None),
    }
)

# 使用迭代生成
dataset = Dataset.from_generator(gen, features=features)

# push到huggingface
dataset.push_to_hub("BUAADreamer/mllm_demo")
