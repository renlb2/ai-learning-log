# Day 32 - Self-Attention 机制
## 关键发现
- 观察 Layer 6 的 12 个 Attention Head：
- 大部分头（如 Head 1, 3, 4）在“摸鱼”，注意力集中在标点 ' 和 [SEP] 上。
- Head 9 是负责核心语义的头，清晰地看到了 `it -> animal` 的指代消解。
- 结论：多头注意力机制就是让不同的头分工合作（语法、结构、语义）。

## 产出
- attention_map.png（单头）
- all_heads_attention.png（多头对比）
