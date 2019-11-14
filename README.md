# soccer_value_regression
足球运动员身价估计(FIFA2018)
[参考页面](http://sofasofa.io/competition.php?id=7#c1)
**背景介绍**:
每个足球运动员在转会市场都有各自的价码。本次数据练习的目的是根据球员的各项信息和能力值来预测该球员的市场价值。

**数据来源**：
FIFA2018。为了公平起见，数据已经进行脱敏加工处理。

**数据**
数据文件（三个）：
train.csv 训练集，文件大小 2.20mb
test.csv 预测集, 文件大小 1.44kb
sample_submit.csv 提交示例 文件大小 62kb

**训练集中共有10441条样本，预测集中有7000条样本。每条样本代表一位球员，数据中每个球员有63项属性。数据中含有缺失值。**

变量说明：
变量名	解释
id	行编号，没有实际意义
club	该球员所属的俱乐部。该信息已经被编码。
league	该球员所在的联赛。已被编码。
birth_date	生日。格式为月/日/年。
height_cm	身高（厘米）
weight_kg	体重（公斤）
nationality	国籍。已被编码。
potential	球员的潜力。数值变量。
pac	球员速度。数值变量。
sho	射门（能力值）。数值变量。
pas	传球（能力值）。数值变量。
dri	带球（能力值）。数值变量。
def	防守（能力值）。数值变量。
phy	身体对抗（能力值）。数值变量。
international_reputation	国际知名度。数值变量。
skill_moves	技巧动作。数值变量。
weak_foot	非惯用脚的能力值。数值变量。
work_rate_att	球员进攻的倾向。分类变量，Low, Medium, High。
work_rate_def	球员防守的倾向。分类变量，Low, Medium, High。
preferred_foot	惯用脚。1表示右脚、2表示左脚。
crossing	传中（能力值）。数值变量。
finishing	完成射门（能力值）。数值变量。
heading_accuracy	头球精度（能力值）。数值变量。
short_passing	短传（能力值）。数值变量。
volleys	凌空球（能力值）。数值变量。
dribbling	盘带（能力值）。数值变量。
curve	弧线（能力值）。数值变量。
free_kick_accuracy	定位球精度（能力值）。数值变量。
long_passing	长传（能力值）。数值变量。
ball_control	控球（能力值）。数值变量。
acceleration	加速度（能力值）。数值变量。
sprint_speed	冲刺速度（能力值）。数值变量。
agility	灵活性（能力值）。数值变量。
reactions	反应（能力值）。数值变量。
balance	身体协调（能力值）。数值变量。
shot_power	射门力量（能力值）。数值变量。
jumping	弹跳（能力值）。数值变量。
stamina	体能（能力值）。数值变量。
strength	力量（能力值）。数值变量。
long_shots	远射（能力值）。数值变量。
aggression	侵略性（能力值）。数值变量。
interceptions	拦截（能力值）。数值变量。
positioning	位置感（能力值）。数值变量。
vision	视野（能力值）。数值变量。
penalties	罚点球（能力值）。数值变量。
marking	卡位（能力值）。数值变量。
standing_tackle	断球（能力值）。数值变量。
sliding_tackle	铲球（能力值）。数值变量。
gk_diving	门将扑救（能力值）。数值变量。
gk_handling	门将控球（能力值）。数值变量。
gk_kicking	门将开球（能力值）。数值变量。
gk_positioning	门将位置感（能力值）。数值变量。
gk_reflexes	门将反应（能力值）。数值变量。
rw	球员在右边锋位置的能力值。数值变量。
rb	球员在右后卫位置的能力值。数值变量。
st	球员在射手位置的能力值。数值变量。
lw	球员在左边锋位置的能力值。数值变量。
cf	球员在锋线位置的能力值。数值变量。
cam	球员在前腰位置的能力值。数值变量。
cm	球员在中场位置的能力值。数值变量。
cdm	球员在后腰位置的能力值。数值变量。
cb	球员在中后卫的能力值。数值变量。
lb	球员在左后卫置的能力值。数值变量。
gk	球员在守门员的能力值。数值变量。
**y	该球员的市场价值（单位为万欧元）。这是要被预测的数值。**

**评价方法**

评价标准为MAE(Mean Absolute Error)。
