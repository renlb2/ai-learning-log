# Day 21 - numpy 基础

## 核心知识点
- ndarray 创建：array / arange / linspace / zeros / ones / random
- 三大属性：shape / ndim / dtype
- 索引切片：a[行, 列]、a[:, 1]、布尔索引 a[a>5]
- 向量化运算：a + b 是逐元素，不是拼接
- 广播：形状不同自动扩展
- 统计：sum / mean / max / min
- axis：0=压缩行，1=压缩列
- np.argmax / np.where / np.unique

## 产出
- week05/day21_numpy.py

## 验证结果
- 5 名学生成绩统计全部正确
- 学生总分：[343 287 381 275 355]
- 每门课平均：[79.6 82.4 81.6 84.6]
- 总分最高学生索引：2
- 班级总平均分：82.05
- ≥90 成绩：6 个
- 加分不改原数组 ✅

## 踩坑
- 之前参考答案把班级平均写成 79.6，实际是 82.05，代码是对的，标准错了
- 教训：对不上时先手动算一遍，标准也可能出错

## 明天（Day 22）
pandas 入门：Series / DataFrame / 读写 CSV
