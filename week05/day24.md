# Day 24 - matplotlib / seaborn 可视化

## 核心知识点
- matplotlib 三步：subplots → 画 → savefig/show
- 四种基础图：plot(趋势) / bar(类别) / scatter(关系) / hist(分布)
- seaborn：boxplot / heatmap / set_theme
- savefig 要在 show 之前，dpi=150 bbox_inches="tight"
- 多子图：plt.subplots(2,2) + tight_layout
- seaborn 画图要传 ax=ax

## 中文字体配置（重要，已验证）
Linux + matplotlib 中文显示方框，解决方案：**用字体文件路径，不用字体名**

```python
import seaborn as sns
sns.set_theme(style="whitegrid")   # 先调，会重置 rcParams

import matplotlib
import matplotlib.font_manager as fm
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
fm.fontManager.addfont(FONT_PATH)
FONT_NAME = fm.FontProperties(fname=FONT_PATH).get_name()
matplotlib.rcParams["font.family"] = FONT_NAME
matplotlib.rcParams["axes.unicode_minus"] = False
