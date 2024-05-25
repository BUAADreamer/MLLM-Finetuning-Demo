# MLLM-Finetuning-Demo

## Enviroment

```shell
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .[torch,metrics]
cd .. # back to project root
```

## finetuning

```shell
CUDA_VISIBLE_DEVICES=0 llamafactory-cli train config/llava_lora_sft.yaml
```

## webchat

```shell
CUDA_VISIBLE_DEVICES=0 llamafactory-cli webchat \
--model_name_or_path llava-hf/llava-1.5-7b-hf \
--adapter_name_or_path saves/llava1_5-7b/lora/sft \
--template vicuna \
--visual_inputs
```

## upload dataset to huggingface

Please replace your real key in the `upload_dataset.py`.

```shell
python3 upload_dataset.py
```