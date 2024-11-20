import pandas as pd

# 加载数据
data = pd.read_csv("restaurant+michelin.csv")

# 确保邮编是整数类型，处理字符和缺失值
# 首先填充 NaN，以免转换时报错
data['postal_code'] = data['postal_code'].fillna(0)

# 将邮编转换为整数类型，非数字会被标记为 NaN
data['postal_code'] = pd.to_numeric(data['postal_code'], errors='coerce').fillna(0).astype(int)


# 定义一个函数，根据邮编返回对应的区
def get_borough(postal_code):
	# Manhattan
	manhattan_zips = [
		10001, 10002, 10003, 10004, 10005, 10006, 10007, 10009, 10010, 10011,
		10012, 10013, 10014, 10016, 10017, 10018, 10019, 10021, 10022, 10023,
		10024, 10025, 10026, 10027, 10028, 10029, 10030, 10031, 10032, 10033,
		10034, 10035, 10036, 10037, 10038, 10039, 10040, 10044, 10069, 10103,
		10119, 10128, 10162, 10165, 10170, 10173, 10199, 10279, 10280, 10282
	]
	# Brooklyn
	brooklyn_zips = [
		11201, 11203, 11204, 11205, 11206, 11207, 11208, 11209, 11210, 11211,
		11212, 11213, 11214, 11215, 11216, 11217, 11218, 11219, 11220, 11221,
		11222, 11223, 11224, 11225, 11226, 11228, 11229, 11230, 11231, 11232,
		11233, 11234, 11235, 11236, 11237, 11238, 11239, 11241, 11243, 11249
	]
	# Queens
	queens_zips = [
		11004, 11101, 11102, 11103, 11104, 11105, 11106, 11109, 11351, 11354,
		11355, 11356, 11357, 11358, 11359, 11360, 11361, 11362, 11363, 11364,
		11365, 11366, 11367, 11368, 11369, 11370, 11372, 11373, 11374, 11375,
		11377, 11378, 11379, 11385, 11411, 11412, 11413, 11414, 11415, 11416,
		11417, 11418, 11419, 11420, 11421, 11422, 11423, 11426, 11427, 11428,
		11429, 11432, 11433, 11434, 11435, 11436, 11691, 11692, 11693, 11694,
		11697
	]
	# Bronx
	bronx_zips = [
		10451, 10452, 10453, 10454, 10455, 10456, 10457, 10458, 10459, 10460,
		10461, 10462, 10463, 10464, 10465, 10466, 10467, 10468, 10469, 10470,
		10471, 10472, 10473, 10474, 10475
	]
	# Staten Island
	staten_island_zips = [
		10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10309, 10310,
		10311, 10312, 10313, 10314
	]

	# 检查邮编所属的区
	if postal_code in manhattan_zips:
		return "Manhattan"
	elif postal_code in brooklyn_zips:
		return "Brooklyn"
	elif postal_code in queens_zips:
		return "Queens"
	elif postal_code in bronx_zips:
		return "Bronx"
	elif postal_code in staten_island_zips:
		return "Staten Island"
	else:
		return "Unknown"


# 添加新的列 'boro'，应用函数
data['boro'] = data['postal_code'].apply(get_borough)

# 保存结果到新的文件
data.to_csv("restaurants_new.csv", index=False)

print("新增列 'boro' 完成，结果已保存到 restaurants_new.csv")
