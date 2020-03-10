import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']    # 替换sans-serif字体
plt.rcParams['axes.unicode_minus'] = False      # 解决坐标轴负数的负号显示问题
import seaborn as sns

DAYS_PER_YEAR = 252
WEEKS_PER_YEAR = 52
MONTHS_PER_YEAR = 12

READ_FOLDER = 'problems'
WRITE_FOLDER = 'solutions'

DATA_FILE_PATH = '{}/sample_data_gj_fund.xlsx'.format(READ_FOLDER)
COL_DATETIME = '日期'
RENAME_COL_DICT = {'基金A': 'fundA', '基金B': 'fundB', '基金A基准': 'fundA_base'}

RISK_FREE_RATE = 0


def load_data(data_file_path, col_datetime, rename_col_dict=None, *args, **kwargs):
	# read data
	df = pd.read_excel(data_file_path, *args, **kwargs)

	# set period index for resampling
	df.set_index(col_datetime, inplace=True)
	df.index = pd.PeriodIndex(df.index, freq='D')

	# rename columns to English for the dot autocomplement
	if rename_col_dict:
		df = df.rename(columns=rename_col_dict)

	return np.log(df).diff().iloc[1:]


def _get_multiplier_from_freq(freq=None, standardize=False):
	if freq is None:
		value = DAYS_PER_YEAR
	elif freq.lower() in ['d', 'day', 'days', '天', '日']:
		value = DAYS_PER_YEAR
	elif freq.lower() in ['w', 'week', 'weeks', '周', '星期']:
		value = WEEKS_PER_YEAR
	elif freq.lower() in ['m', 'month', 'months', '月']:
		value = MONTHS_PER_YEAR
	else:
		raise Exception('Please Input A Valid Freq Slogan!')
	if standardize:
		return np.sqrt(value)
	else:
		return value


def get_alpha_sequence(data, base_data):
	return data - base_data


def get_year_return(data, freq=None):
	return np.mean(data) * _get_multiplier_from_freq(freq, standardize=False)


def get_year_volatility(data, freq=None):
	return np.std(data) * _get_multiplier_from_freq(freq, standardize=True)


def get_year_downside_volatility(data, freq=None):
	data = np.array(data)
	data = np.where(data > 0, 0, data)
	return np.sqrt(sum(data ** 2) / (len(data) - 1)) * _get_multiplier_from_freq(freq=freq, standardize=True)


def get_interval_max_dropdown(data):
	cum_data = np.cumsum(data) + 1   # 从每日对数收益转为累积对数收益，一定要一个起始值 1
	back_data = 1 - cum_data / np.maximum.accumulate(cum_data)   # 从累积对数收益序列转为回撤序列
	# 因为净值有时候是不变的，即收益率变化为0，因此直接求最大回撤可能会出现nan，所以将nan替换为0
	# 此处使用np.nanmax也不好，因为要考虑所有净值不变的情况，这个时候使用np.nanmax就会报错
	return max(back_data.fillna(0))


def get_sharpeRatio(data):
	data_year_return = get_year_return(data)
	data_year_volatility = get_year_volatility(data)
	return (data_year_return - RISK_FREE_RATE) / data_year_volatility


def get_sortinoRatio(data):
	data_year_return = get_year_return(data)
	data_year_downside_volatility = get_year_downside_volatility(data)
	return (data_year_return - RISK_FREE_RATE) / data_year_downside_volatility


def get_calmarRatio(data, freq=None):
	"""
	Carmar比率的计算，是求最近三年的收益与最大回撤的比值
	为保证 TotalReturn 与 MaxDropdown 之间的比例与 CalmarRatio 吻合，因此此处不做时间区间截断处理
	:param data:
	:param freq:
	:return:
	"""
	# multiplier = _get_multiplier_from_freq(freq)
	# if len(data) > 3 * multiplier:
	# 	data = data[: 3*multiplier]
	data_year_return = get_year_return(data)
	data_maxDropdown = get_interval_max_dropdown(data)
	return data_year_return / data_maxDropdown


def gen_portfolio_trend(data, col_A, col_B, PCT_A, PCT_B):
	start_asset = 1
	result = []

	for year in data.index.year.unique():
		asset_A = start_asset * PCT_A
		asset_B = start_asset * PCT_B
		for now_date, row in data[data.index.year == year].iterrows():
			asset_A *= (1 + row[col_A])
			asset_B *= (1 + row[col_B])
			now_asset = asset_A + asset_B
			asset_return = now_asset / start_asset - 1
			result.append({
				'now_date': now_date,
				'asset_A': asset_A,
				'asset_B': asset_B,
				'asset_sum': now_asset,
				'asset_return': asset_return
			})
			start_asset = now_asset
	return pd.DataFrame(result)


def gen_basic_info(fundA_series, fundB_series, gen_excel_file=True):
	fundA_info_dict = dict()
	fundB_info_dict = dict()
	for year in [2013, 2014, 2015, 2016, 2017, 'ALL']:
		if year != 'ALL':
			fundA = fundA_series[fundA_series.index.year == year]
			fundA_base = fundA_base_series[fundA_base_series.index.year == year]
			fundB = fundB_series[fundB_series.index.year == year]
		else:
			fundA = fundA_series
			fundA_base = fundA_base_series
			fundB = fundB_series

		fundA_return = get_year_return(fundA)
		fundA_base_return = get_year_return(fundA_base)
		fundA_volatility = get_year_volatility(fundA)
		fundA_alpha = get_alpha_sequence(fundA, fundA_base)
		funA_alpha_return = get_year_return(fundA_alpha)
		fundA_alpha_volatility = get_year_volatility(fundA_alpha)
		fundA_maxDropdown = get_interval_max_dropdown(fundA)
		fundA_sharpeRatio = get_sharpeRatio(fundA)
		fundA_sortinoRatio = get_sortinoRatio(fundA)

		fundA_year_info = {
			'Return': fundA_return,
			'BaseReturn': fundA_base_return,
			'AlphaReturn': funA_alpha_return,
			'Volatility': fundA_volatility,
			'AlphaVolatility': fundA_alpha_volatility,
			'MaxDropdown': fundA_maxDropdown,
			'SharpeRatio': fundA_sharpeRatio,
			'SortinoRatio': fundA_sortinoRatio,
		}
		fundA_info_dict[year] = fundA_year_info

		fundB_return = get_year_return(fundB)
		fundB_volatility = get_year_volatility(fundB)
		fundB_maxDropdown = get_interval_max_dropdown(fundB)
		fundB_sharpeRatio = get_sharpeRatio(fundB)
		fundB_calmarRatio = get_calmarRatio(fundB)

		fundB_yar_info = {
			'Return': fundB_return,
			'Volatility': fundB_volatility,
			'MaxDropdown': fundB_maxDropdown,
			'SharpeRatio': fundB_sharpeRatio,
			'CalmarRatio': fundB_calmarRatio,
		}
		fundB_info_dict[year] = fundB_yar_info

	if gen_excel_file:
		pd.DataFrame(fundA_info_dict).to_excel(f'{WRITE_FOLDER}/solution_1/result_fund_A.xlsx')
		pd.DataFrame(fundB_info_dict).to_excel(f'{WRITE_FOLDER}/solution_1/result_fund_B.xlsx')

	return fundA_info_dict, fundB_info_dict


def gen_distplot_of_return(fund_series, suptitle, filename=None):
	fig, ax = plt.subplots()
	fig.suptitle(suptitle)
	sns.distplot(fund_series, ax=ax)
	if not filename:
		filename = suptitle
	fig.savefig(f'{WRITE_FOLDER}/solution_2/{filename}.png')
	return fig, ax


def gen_portfolio_trend_img(df_portfolio, pct_A, pct_B):
	col_asset_return = 'asset_return'
	portfolio_annual_return = get_year_return(df_portfolio[col_asset_return])
	portfolio_annual_volatility = get_year_volatility(df_portfolio[col_asset_return])
	portfolio_annual_maxDropdown = get_interval_max_dropdown(df_portfolio[col_asset_return])

	fig, ax = plt.subplots()
	df_portfolio.asset_sum.plot(ax=ax, x=df_portfolio.index)
	annotate_text = '\n'.join([
		'  组合配比: {:<2d}/{:>2d} '.format(int(pct_A * 10), int(pct_B * 10)),
		'年化收益率: {:5.2f}%'.format(portfolio_annual_return * 100),
		'年化波动率: {:5.2f}%'.format(portfolio_annual_volatility * 100),
		'  最大回撤: {:5.2f}%'.format(portfolio_annual_maxDropdown * 100)
	])
	plt.figtext(0.85, 0.15, annotate_text, horizontalalignment='right', fontsize=16)
	fig.savefig(f'{WRITE_FOLDER}/solution_3/Portfolio Trend of ({pct_A}, {pct_B}).png')
	return fig


if __name__ == '__main__':
	df = load_data(data_file_path=DATA_FILE_PATH, col_datetime=COL_DATETIME, rename_col_dict=RENAME_COL_DICT, skiprows=1)
	fundA_series = df.fundA
	fundB_series = df.fundB
	fundA_base_series = df.fundA_base

	# 第一题，生成表格
	gen_basic_info(fundA_series, fundB_series)

	# 第二题，生成日收益分布图
	gen_distplot_of_return(fundA_series, suptitle='Distplot of Return of Fund A')
	gen_distplot_of_return(fundB_series, suptitle='Distplot of Return of Fund B')

	# 第三题，计算投资组合
	for pct_group in [(.2, .8), (.5, .5)]:
		df_portfolio = gen_portfolio_trend(df, 'fundA', 'fundB', *pct_group)
		gen_portfolio_trend_img(df_portfolio, *pct_group)

	# 第四题，过了面试再解
	# ...











