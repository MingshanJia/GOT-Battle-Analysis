#!/usr/bin/env python
# coding: utf-8

# # 五王之战分析 - 冰与火之歌

# ## 简介
# 
# 五王之战（War of the Five Kings）是著名严肃奇幻小说《冰与火之歌》中的著名内战。这是一场规模空前、波及七大王国的内乱。顾名思义，前后共有五人在战争中称王：乔佛里、史坦尼斯、蓝礼均声称自己是铁王座的合法继承人。除此之外，罗柏·史塔克被北境众封臣推选为北境之王，巴隆·葛雷乔伊亦再度掀起独立大旗，欲摆脱铁王座的统治，自称为铁群岛之王。
# 
# 

# 本数据集(battles.csv)包含了五王之战期间的战争，它是所有战斗的大集合。该数据是Kaggle中[Game of Thrones](https://www.kaggle.com/mylesoneill/game-of-thrones)的一部分。
# 
# 数据中的变量含义解释：
# ```
# name: 战争的名称，字符变量。
# year: 战争发生的年份，数值变量。
# battle_number: 本数据中的unique id，对应每一场独立的战役，数值变量。
# attacker_king: 攻击方的国王，"/"表示了国王的更换。例如："Joffrey/Tommen Baratheon"意味着Tomen Baratheon继承了Joffrey的王位，分类变量。
# defender_king: 防守方的国王，分类变量。
# attacker_1: 攻击方将领，字符变量。
# attacker_2: 攻击方将领，字符变量。
# attacker_3: 攻击方将领，字符变量。
# attacker_4: 攻击方将领，字符变量。
# defender_1: 防守方将领，字符变量。
# defender_2: 防守方将领，字符变量。
# defender_3: 防守方将领，字符变量。
# defender_4: 防守方将领，字符变量。
# attacker_outcome: 从攻击方角度来看的战争结果，分别有：win, loss, draw，分类变量。
# battle_type: 战争的类别。pitched_battle: 双方军队在一个地点相遇并战斗，这也是最基本的战争类别；ambush: 以隐身或诡计为主要攻击手段的战争；siege: 阵地战；razing: 对未设防位置的攻击。分类变量。
# major_death: 是否有重要人物的死亡，二进制变量。
# major_capture: 是否有重要人物的被捕，二进制变量。
# attacker_size: 攻击方力量的大小，并未对骑兵、步兵等士兵种类有所区分，数值变量。
# defender_size: 防守方力量的大小，并未对骑兵、步兵等士兵种类有所区分，数值变量。
# attacker_commander: 攻击方的主要指挥官。指挥官的名字中并没有包含头衔，不同的指挥官名字用逗号隔开，字符变量。
# defender_commander: 防守方的主要指挥官。指挥官的名字中并没有包含头衔，不同的指挥官名字用逗号隔开，字符变量。
# summer: 战争是否发生于夏天，二进制变量。
# location: 战争发生的地点，字符变量。
# region: 战争发生的地域，包括：Beyond the Wall, The North, The Iron Islands, The Riverlands, The Vale of Arryn, The Westerlands, The Crownlands, The Reach, The Stormlands, Dorne，分类变量。
# note: 注释，字符变量。
# 
# ```

# ## 项目完成指南
# 
# 
# 
# 本项目中的数据分析流程已经给出，但代码将完全由你自己进行书写，如果你无法完成本项目，说明你目前的能力并不足以完成 数据分析(进阶)纳米学位，建议先进行 数据分析（入门）纳米学位的学习，掌握进阶课程的先修知识。
# 
# 对于数据分析过程的记录也是数据分析报告的一个重要部分，你可以自己在需要的位置插入Markdown cell，记录你在数据分析中的关键步骤和推理过程。比如：数据有什么样的特点，统计数据的含义是什么，你从可视化中可以得出什么结论，下一步分析是什么，为什么执行这种分析。如果你无法做到这一点，你也无法通过本项目。
# 
# 
# > **小贴士**: 像这样的引用部分旨在为学员提供实用指导，帮助学员了解并使用 Jupyter notebook

# ## 提出问题
# 
# 在此项目中，你将以一名数据分析师的身份执行数据的探索性分析。你将了解数据分析过程的基本流程。在你分析数据之前，请先思考几个你需要理解的关于这些战斗的问题，例如，哪一个区域发生了最多的战争？哪一个国王获得了最多的胜利？战争的胜利与否受那些关键因素的影响？
# 
# **问题**：请写下你感兴趣的问题，请确保这些问题能够由现有的数据进行回答。  
# **Q0**： 哪个将领赢得了更多的胜利（作为攻方）？  
# **Q1**： 攻防国王的战争类型偏好？  
# **Q2**： 胜败与兵力多少的关系如何？  
# **Q3**： 各个国王战争结果与夏季与否的关系  
# **Q4**： 攻方战争结果与夏季的相关性  
# **Q5**： 攻方胜败与进攻兵力更多的相关性
# 
# （为了确保学习的效果，请确保你的数据分析报告中能够包含2幅可视化和1个相关性分析。）
# 
# **答案**：将此文本替换为你的回答！
# 
# 
# 在提出了问题之后，我们将开始导入数据，并对数据进行探索性分析，来回答上面提出的问题。
# 
# > **小贴士**: 双击上框，文本就会发生变化，所有格式都会被清除，以便你编辑该文本块。该文本块是用 [Markdown](http://daringfireball.net/projects/markdown/syntax)编写的，该语言使用纯文本语法，能用页眉、链接、斜体等来规范文本格式。在纳米学位课程中，你也会用到 Markdown。编辑后，可使用 **Shift** + **Enter** 或 **Shift** + **Return** 运行上该框，使其呈现出编辑好的文本格式。

# ## 数据评估和清理

# > **小贴士**: 运行代码框的方法与编辑上方的 Markdown 框的格式类似，你只需点击代码框，按下键盘快捷键 **Shift** + **Enter** 或 **Shift** + **Return** ，或者你也可先选择代码框，然后点击工具栏的 **运行** 按钮来运行代码。运行代码框时，相应单元左侧的信息会出现星号，即 `In [*]:`，若代码执行完毕，星号则会变为某个数字，如 `In [1]`。如果代码运行后有输出结果，输出将会以 `Out [1]:` 的形式出现，其中的数字将与 "In" 中的数字相对应。

# In[1]:


# TO DO: load pacakges
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# TO DO: load the dataset
battle = pd.read_csv('battles.csv')
battle.head()


# In[3]:


# TO DO: check the dataset general info
battle.info()


# In[4]:


battle.columns


# In[5]:


# TO DO: clean the data (optional: only there are problems)
# drop attacker_2, attacker_3，attacker_4, defender_2, defender_3, defender_4, note
battle.drop(['attacker_2', 'attacker_3', 'attacker_4', 'defender_2', 'defender_3', 'defender_4', 'note'], axis=1, inplace=True)


# In[6]:


# datatype transfer: [attacker_king, defender_king, battle_type, region] should be category
battle['attacker_king'] = battle['attacker_king'].astype('category')
battle['defender_king'] = battle['defender_king'].astype('category')
battle['battle_type'] = battle['battle_type'].astype('category')
battle['region'] = battle['region'].astype('category')


# In[7]:


def binary_change(element):
    if element == 1.:
        return "Yes"
    else:
        return "No"


# In[8]:


# change binary value into "Yes" or "No"
battle.loc[:, ['major_death', 'major_capture', 'summer']] = battle.loc[:, ['major_death', 'major_capture', 'summer']].applymap(binary_change)


# In[9]:


#check for duplication : no duplication in this dataset
sum(battle.duplicated())


# In[10]:


battle.info()
battle.head(30)


# ## 数据探索分析

# In[11]:


# Q0: 哪个将领赢得了更多的胜利（作为攻方）？
# A0: Lannister和Greyjoy都赢了7场

# attacker general wins rank
battle_attwins = battle[battle['attacker_outcome'] == 'win']
cat_order = battle_attwins['attacker_1'].value_counts().index
sb.countplot(data = battle_attwins, x = 'attacker_1', color=sb.color_palette()[2], order=cat_order)
plt.xticks(rotation = 90)
plt.ylabel('Counts')
plt.xlabel('Attacker General')
plt.title('Attacker General Win Rank')


# In[12]:


# Q1:攻防国王的战争类型偏好
# A1:可以看出Joffery/Tommen Baratheon更喜欢发动piched battle和siege; Robb Stark偏爱ambush;
# Balon/Euron Greyjoy则是各类型的战役都发动过；Stannis Baratheon为数不多的进攻中只有pitched battle和siege两种

battle_plot = battle.groupby(['attacker_king', 'battle_type']).size().sort_values(ascending=False).reset_index().pivot(columns='battle_type', index='attacker_king', values=0)
#reindex the kings according to the total attacks
cat_order = battle['attacker_king'].value_counts().index
battle_plot = battle_plot.reindex(index = cat_order) 
#reindex the battle types according to sum of certain type
battle_plot = battle_plot.reindex_axis(battle_plot.sum().sort_values(ascending = False).index, axis=1) 
# plot stacked bar chart
battle_plot.plot(x=battle_plot.index, kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title = 'Battle type')
plt.ylabel('Counts')
plt.xlabel('Attacker King')
plt.title('Attacker King Battle Type Preference')


# In[13]:


# Q2: 胜负与兵力多少的关系
# A2: 红线上方代表人数占优，可以看出在15场有相关统计的战争中，只有3场人数占优一方获得胜利。所以胜利并不因为人数众多。
# dropping rows with null value in 'attacker_size', 'defender_size','attacker_outcome'

battle_2 = battle.dropna(subset = ['attacker_size', 'defender_size','attacker_outcome']) 
win_with_more_attacker = battle_2[(battle_2['attacker_size'] > battle_2['defender_size']) & (battle_2['attacker_outcome'] == 'win')]
print("In {} battles, only {} battles winned by the side with more attackers".format(battle_2.shape[0], win_with_more_attacker.shape[0]))

sb.lmplot(data = battle_2, x = 'defender_size', y = 'attacker_size', hue='attacker_outcome', fit_reg=False, size=7, legend=False)
plt.plot(np.linspace(0,20000,1000), np.linspace(0,20000,1000), 'r-')
battle_2.head(15)
plt.legend(bbox_to_anchor=(0.7, 0.9), loc=2, borderaxespad=0., title = 'Attacker Outcome')
plt.ylabel('Attacker Size')
plt.xlabel('Defender Size')
plt.title('Attack Outcome in Relation to Attacker Size/Defender Size')


# In[14]:


# Q3: 各个国王战争结果与夏季与否的关系
# A3: 可以看出Joffrey/Tommen Baratheon夏天胜率略低于非夏天; Stannis Baratheon则是夏天胜率相对较高；
# Balon/Euron Greyjoy无论夏天与否，作为进攻方都是全胜；而Rob Stark只有夏天时发动过进攻，没有冬天的数据

# summer:
battle_summer = battle[battle['summer'] == 'Yes']
battle_summer_win = battle_summer[battle_summer['attacker_outcome'] == 'win']
battle_summer_win = battle_summer_win.dropna(subset=['attacker_king'])
summer_num = battle_summer.groupby(['attacker_king']).size()
summer_win_num = battle_summer_win.groupby(['attacker_king']).size()
# not summer:
battle_notsummer = battle[battle['summer'] == 'No']
battle_notsummer_win = battle_notsummer[battle_notsummer['attacker_outcome'] == 'win']
battle_notsummer_win = battle_notsummer_win.dropna(subset=['attacker_king'])
notsummer_num = battle_notsummer.groupby(['attacker_king']).size()
notsummer_win_num = battle_notsummer_win.groupby(['attacker_king']).size()
# build new frame to present win rate in relation with summer
summer_win_rate = summer_win_num / summer_num
notsummer_win_rate = notsummer_win_num / notsummer_num
battle_win_rate = pd.DataFrame({'Summer': summer_win_rate, 'Not Summer': notsummer_win_rate})
battle_win_rate.plot.bar()
plt.xlabel('Attacker King')
plt.ylabel('Win Rate')
plt.title('Win Rate in Relation to Summer/Not Summer')


# In[15]:


# change attacker_outcome and summer into int
def outcome_transfer(outcome):
    if outcome == 'loss':
        return 0
    else:
        return 1
    
def summer_transfer(summer):
    if summer == 'Yes':
        return 1 
    else:
        return 0

battle.loc[:, ['attacker_outcome']] = battle.loc[:, ['attacker_outcome']].applymap(outcome_transfer)
battle.loc[:, ['summer']] = battle.loc[:, ['summer']].applymap(summer_transfer)


# In[16]:


# Q4: correlation between outcome and summer
# A4: -0.097, the correlation is very weak
corr_outcome_summer = battle['attacker_outcome'].corr(battle['summer'])
print("Correlation between outcome and summer is : {:.3f}".format(corr_outcome_summer))


# In[17]:


# Q5: correlation between outcome and more attacker
# A5: -0.431, correlation is negative and relatively strong
more_attacker = battle_2['attacker_size'] > battle_2['defender_size']
more_attacker = more_attacker.to_frame(name='more_attacker')
battle_2_extend = pd.concat([battle_2, more_attacker],join='outer',axis=1)

def more_attacker_transfer(more_attacker):
    if more_attacker == True:
        return 1 
    else:
        return 0
    
battle_2_extend.head()
battle_2_extend.loc[:, ['more_attacker']] = battle_2_extend.loc[:, ['more_attacker']].applymap(more_attacker_transfer)
battle_2_extend.loc[:, ['attacker_outcome']] = battle_2_extend.loc[:, ['attacker_outcome']].applymap(outcome_transfer)

corr_outcome_moreattacker = battle_2_extend['attacker_outcome'].corr(battle_2_extend['more_attacker'])
print("Correlation between outcome and more attacker is : {:.3f}".format(corr_outcome_moreattacker))


# 在数据的探索性分析中，请确保你对数据分析中的关键步骤和推理过程进行了记录。你可以自己插入code cell和markdown cell来组织你的报告。

# ## 得出结论

# **问题**：上面的分析能够回答你提出的问题？通过这些分析你能够得出哪些结论？
# 
# **答案**：  
# Q0: 哪个将领赢得了更多的胜利（作为攻方）？  A0: Lannister和Greyjoy都赢了7场。    
#   
# 
# Q1:攻防国王的战争类型偏好?  A1:可以看出Joffery/Tommen Baratheon更喜欢发动piched battle和siege; Robb Stark偏爱ambush; Balon/Euron Greyjoy则是各类型的战役都发动过；Stannis Baratheon为数不多的进攻中只有pitched battle和siege两种。  
# 
# Q2: 胜负与兵力多少的关系？
# A2: 红线上方代表人数占优，可以看出在15场有相关统计的战争中，只有3场人数占优一方获得胜利。所以胜利并不因为人数众多。
# 
# 
# Q3: 各个国王战争结果与夏季与否的关系？
# A3: 可以看出Joffrey/Tommen Baratheon夏天胜率略低于非夏天; Stannis Baratheon则是夏天胜率相对较高；
# Balon/Euron Greyjoy无论夏天与否，作为进攻方都是全胜；而Rob Stark只有夏天时发动过进攻，没有冬天的数据。
# 
# Q4: 胜利与夏季的相关性？
# A4: -0.097, 相关性很低。
# 
# Q5: 胜利与更多进攻方的相关性？
# A5: -0.431, 相关性较高，负相关。
# 
# 
# 

# ## 反思

# **问题**：在你的分析和总结过程中是否存在逻辑严谨。是否有改进的空间? 你可以从下面的一些角度进行思考：
# 1. 数据集是否完整，包含所有想要分析的数据？
# 2. 在对数据进行处理的时候，你的操作（例如删除/填充缺失值）是否可能影响结论？
# 3. 是否还有其他变量（本数据中没有）能够对你的分析有帮助？
# 4. 在得出结论时，你是否混淆了相关性和因果性？
# 
# **答案**：
# 1. 数据集的行数较少，得出的结论偶然性比较大。  
# 2. 我在数据清洗是都是采用删除缺失项，不会影响结论。
# 3. 如下数据都可能会提供帮助：发动战争的理由，战争的策略，战争持续的时间等。
# 4. 此处的分析都仅仅是相关性，不是因果性。

# 恭喜你完成了此项目！这只是数据分析过程的一个样本：从生成问题、整理数据、探索数据到得出结论。在数据分析(进阶)纳米学位中，你将会学到更多高级的数据分析方法和技术，如果你感兴趣的话，我们鼓励你继续学习后续的课程，掌握更多的数据分析的高级技能！

# > 若想与他人分享我们的分析结果，除了向他们提供 jupyter Notebook (.ipynb) 文件的副本外，我们还可以将 Notebook 输出导出为一种甚至那些未安装 Python 的人都能打开的形式。从左上方的“文件”菜单，前往“下载为”子菜单。然后你可以选择一个可以更普遍查看的格式，例如 HTML (.html) 。你可能需要额外软件包或软件来执行这些导出。
