# MLLM-Finetuning-Demo

## 安装LLaMA-Factory

```shell
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e .[torch,metrics]
cd .. # 回到项目根目录
```

## 微调

```shell
CUDA_VISIBLE_DEVICES=0 llamafactory-cli train config/llava_lora_sft.yaml
```

## 网页聊天

```shell
CUDA_VISIBLE_DEVICES=0 llamafactory-cli webchat \
--model_name_or_path llava-hf/llava-1.5-7b-hf \
--adapter_name_or_path saves/llava1_5-7b/lora/sft \
--template vicuna \
--visual_inputs
```

## 上传数据集到Huggingface

请在 `upload_dataset.py` 中替换您自己的key.

```shell
python3 upload_dataset.py
```

## 导出和上传模型到huggingface

请在 `config/llava_lora_sft_export.yaml` 中替换您自己的 `export_hub_model_id` 和 `hf_hub_token`.

```shell
CUDA_VISIBLE_DEVICES=0 llamafactory-cli export config/llava_lora_sft_export.yaml
```