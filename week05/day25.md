# Day 25 - Titanic EDA + 清洗

## 核心知识点
- EDA 五步：shape/head/info/describe → 缺失 → 目标分布 → 单变量 → 可视化
- 单变量分析：groupby + mean
- 交叉分析：groupby(["A","B"]) + mean
- 缺失值策略：Age 按 Sex+Pclass 填中位数；Cabin 转 HasCabin；Embarked 填众数
- 特征工程：FamilySize、IsAlone、Title
- 类别变量映射：map({...})

## 关键发现
- 幸存率：38%
- 女性 74% vs 男性 19%
- 头等舱 63% vs 三等舱 24%
- 女性+头等舱 97%，男性+三等舱 13.5%

## 产出
- week05/day25_titanic_eda.py
- week05/day25_titanic_plot.py
- week05/titanic_clean.csv（891 行，14 列，无缺失）
- week05/titanic_eda.png（四合一图）

## 踩坑
## matplotlib 中文方框问题
- 现象：中文显示成方块，中间有个"字"
- 原因：NotoSansCJK 是 .ttc 文件（一个文件多个字形），matplotlib 自动索引时挑不出 SC
- 修法：手动注册
  from matplotlib import font_manager
  for f in font_manager.findSystemFonts(fontpaths=["/usr/share/fonts/opentype/noto/"]):
      if "NotoSansCJK" in f:
          font_manager.fontManager.addfont(f)
  matplotlib.rcParams["font.sans-serif"] = ["Noto Sans CJK SC"]
- 必须删缓存：rm -rf ~/.cache/matplotlib

## 明天（Day 26）
Titanic 建模 + 提交：sklearn 训练、交叉验证、生成 submission.csv
