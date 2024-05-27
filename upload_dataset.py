import json

import fire


def main(hf_token="hf_xxxxx", json_file="data/mllm_demo.json", hf_data_id="BUAADreamer/mllm_demo"):
    with open(json_file) as f:
        examples = json.loads(f.read())

    import huggingface_hub

    huggingface_hub.login(hf_token)  # 替换为你自己的key从而登录hf

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
    dataset.push_to_hub(hf_data_id)


if __name__ == '__main__':
    fire.Fire(main)
