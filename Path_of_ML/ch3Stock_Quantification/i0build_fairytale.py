import numpy as np
from abupy import ABuSymbolPd


g_with_date_week_noise = True

def _gen_another_word_price(kl_another_word):
    """
    生成股票在另一个世界中的价格
    :param kl_another_word:
    :return:
    """
    for ind in np.arange(2, kl_another_word.shape[0]):
        # 前天数据
        bf_yesterday = kl_another_word.iloc[ind - 2]
        # 昨天
        yesterday = kl_another_word.iloc[ind - 1]
        # 今天
        today = kl_another_word.iloc[ind]
        # 生成今天的收盘价格
        kl_another_word.close[ind] = _gen_another_word_price_rule(
            yesterday.close, yesterday.volume,
            bf_yesterday.close, bf_yesterday.volume,
            today.volume, today.date_week)

def _gen_another_word_price_rule(yesterday_close, yesterday_volume,
                                 bf_yesterday_close,
                                 bf_yesterday_volume,
                                 today_volume, date_week):
    """
        通过前天收盘量价，昨天收盘量价，今天的量，构建另一个世界中的价格模型
    """
    # 昨天收盘价格与前天收盘价格的价格差
    price_change = yesterday_close - bf_yesterday_close
    # 昨天成交量与前天成交量的量差
    volume_change = yesterday_volume - bf_yesterday_volume

    # 如果量和价变动一致，今天价格涨，否则跌
    # 即量价齐涨－>涨, 量价齐跌－>涨，量价不一致－>跌
    sign = 1.0 if price_change * volume_change > 0 else -1.0
    
    # 通过date_week生成噪音，否则之后分类100%分对
    if g_with_date_week_noise:
        # 针对sign生成噪音，噪音的生效的先决条件是今天的量是这三天最大的
        gen_noise = today_volume > np.max(
            [yesterday_volume, bf_yesterday_volume])
        # 如果量是这三天最大 且是周五，下跌
        if gen_noise and date_week == 4:
            sign = -1.0
        # 如果量是这三天最大，如果是周一，上涨
        elif gen_noise and date_week == 0:
            sign = 1.0

    # 今天的涨跌幅度基础是price_change（昨天前天的价格变动）
    price_base = abs(price_change)
    # 今天的涨跌幅度变动因素：量比，
    # 今天的成交量/昨天的成交量 和 今天的成交量/前天的成交量 的均值
    price_factor = np.mean([today_volume / yesterday_volume,
                            today_volume / bf_yesterday_volume])

    if abs(price_base * price_factor) < yesterday_close * 0.10:
        # 如果 量比 * price_base 没超过10%，今天价格计算
        today_price = yesterday_close + \
                      sign * price_base * price_factor
    else:
        # 如果涨跌幅度超过10%，限制上限，下限为10%
        today_price = yesterday_close + sign * yesterday_close * 0.10
    return today_price

def change_real_to_another_word(symbol):
    """
    将原始真正的股票数据价格列只保留前两天数据，成交量，周几列完全保留
    价格列其他数据使用_gen_another_word_price变成另一个世界价格
    :param symbol:
    :return:
    """
    kl_pd = ABuSymbolPd.make_kl_df(symbol)
    if kl_pd is not None:
        # 原始股票数据也只保留价格，周几，成交量
        kl_pig_three = kl_pd.filter(['close', 'date_week', 'volume'])
        # 只保留原始头两天的交易收盘价格，其他的的都赋予nan
        kl_pig_three['close'][2:] = np.nan
        # 将其他nan价格变成猪老三世界中价格使用_gen_another_word_price
        _gen_another_word_price(kl_pig_three)
        return kl_pig_three

choice_symbols = ['usNOAH', 'usSFUN', 'usBIDU', 'usAAPL', 'usGOOG',
                  'usTSLA', 'usWUBA', 'usVIPS']
another_word_dict = {}
real_dict = {}
for symbol in choice_symbols:
    # 猪老三世界的股票走势字典
    another_word_dict[symbol] = change_real_to_another_word(symbol)
    # 真实世界的股票走势字典，这里不考虑运行效率问题
    real_dict[symbol] = ABuSymbolPd.make_kl_df(symbol)
# 表10-1所示
show1 = another_word_dict['usNOAH'].head()
print(show1)
