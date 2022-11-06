# 做数据处理和分析
# pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com pandas
# 用来数据可视化的工具
# pip install matplotlib  -i https://pypi.tuna.tsinghua.edu.cn/simple
import pandas as pd
import matplotlib.pyplot as plt

# header =None 没有表头，第一行也是数据，指定第一列为索引
df = pd.read_csv('data.csv', header=None, index_col=0)

red_ball = df.loc[:, 1:6]

bule_ball = df.loc[:, 7]

red_count = pd.value_counts(red_ball.values.flatten())

blue_count = pd.value_counts(bule_ball)

# 制作图标
# 返回两个参数，多个图表
fig, ax = plt.subplots(2, 1)

ax[0].pie(red_count, labels=red_count.index)
ax[1].pie(blue_count, labels=blue_count.index)

plt.show()
