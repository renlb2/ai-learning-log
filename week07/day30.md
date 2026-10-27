# Day 30 - 深度学习初体验：PyTorch + MNIST

## 核心知识点
- Tensor：GPU/CPU 上的多维数组
- 训练循环 5 步曲：zero_grad -> forward -> loss -> backward -> step
- 优化器：SGD（基础，慢） vs Adam（工业界默认，快且稳）
- Epoch：把数据完整看几遍

## 产出
- week07/day30_pytorch_mnist.py（两层网络，SGD，3 Epoch，90.14%）
- week07/day30_add_layer.py（三层网络，跑通成功）

## 踩坑
- RuntimeError: mat1 and mat2 shapes cannot be multiplied (64x512 and 128x10)
  原因：加宽了 fc1 的输出，但忘记改 fc2 的输入
  教训：前一层的 out 必须等于后一层的 in
- 改了 __init__ 里的层，千万记得在 forward 里把它串进去

## 明天（Day 31）
进入自然语言处理（NLP）与 LLM 的世界：词向量、Tokenizer、Hugging Face
