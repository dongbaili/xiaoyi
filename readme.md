# 小艺大模型安全性评估
本仓库包含评估网页版小艺大模型(https://xiaoyi.huawei.com/chat/) 的安全合规性的代码和结果。

注1：原始有害问题未提交到本仓库中，请自行前往huggingface获取相关数据集的权限并下载。

注2：现使用Qwen3-8B作为judge LLM，使用硅基流动提供的接口。你需要更改自己的api token，或者选择更强大的judge LLM以获得更准确的评估结果。

注3：本仓库的结果文件中可能包含一些LLM生成的有害言论

## 文件目录

- ``xy.py``：与网页版小艺对话的脚本。自动打开edge浏览器访问小艺网页版，输入有害prompt，等待回答，随后记录模型输出。
- ``*_results.jsonl``：记录小艺的回答的结果文件，*代表数据集简称。
- ``judge.py``：将小艺的回答提供给另一个judge LLM，并让其判断该回答是否有害。
- ``*_judge.jsonl``：judge LLM的评估结果，1代表有害，0代表无害。

## 结果概述
**有害回答比例**：
- wildjailbreak: 354/938 (38%)
- wildguard-test: 97/177 (55%)

## 数据集来源
- WildGuard: https://huggingface.co/datasets/allenai/wildguardmix
- WildJailBreak: https://huggingface.co/datasets/allenai/wildjailbreak
- JBV: https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k

## 详细文档说明（需使用华为内网访问）
安全评估流程与定量结果: https://clouddocs.huawei.com/wapp/public/b8ce2a9f-463a-41c1-be82-12beb76dba24
有害输出代表性示例: https://clouddocs.huawei.com/wapp/public/6c86de2d-c2dc-4e02-a29b-4a39698008d2
LLM安全攻防相关paper: https://clouddocs.huawei.com/wapp/public/9a20714d-909a-44b9-847e-5650883c4766
