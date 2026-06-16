from data_fetcher import fetch_market
from strategy import decide
from portfolio import load, save
from notifier import send


def run():

    market = fetch_market()
    portfolio = load()

    decision = decide(portfolio, market)

    # 💰 更新仓位（真实定投）
    portfolio["qqq_value"] += decision["qqq_buy"]
    portfolio["bond_value"] += decision["bond_buy"]
    portfolio["total_invested_days"] += 1

    total = portfolio["qqq_value"] + portfolio["bond_value"]

    msg = f"""
📊 Level 5.5 自动资产系统

━━━━━━━━━━━━━━━━━━
📈 纳指数据
价格：{market['qqq']}
回撤：{market['qqq_dd']:.2f}%

━━━━━━━━━━━━━━━━━━
💰 当前仓位
纳指：{portfolio['qqq_value']:.2f}
债券：{portfolio['bond_value']:.2f}
总资产：{total:.2f}

纳指占比：{decision['qqq_ratio']}%

━━━━━━━━━━━━━━━━━━
💸 今日操作
纳指定投：{decision['qqq_buy']} 元
债券配置：{decision['bond_buy']} 元

━━━━━━━━━━━━━━━━━━
📌 策略提示
"""

    for a in decision["actions"]:
        msg += f"• {a}\n"

    msg += "\n━━━━━━━━━━━━━━━━━━"

    print(msg)
    send(msg)

    save(portfolio)


if __name__ == "__main__":
    run()
