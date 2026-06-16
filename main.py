from data_fetcher import fetch_market
from strategy import decide
from portfolio import load, save
from notifier import send


def run():

    market = fetch_market()
    portfolio = load()

    decision = decide(portfolio, market)

    # 更新现金（模拟定投）
    portfolio["cash"] -= decision["invest"]

    msg = f"""
📊 Level 5 自动投资系统报告

━━━━━━━━━━━━━━━━━━━━
📈 纳斯达克指数（QQQ）
价格：{market['qqq']}
回撤：{market['qqq_dd']:.2f}%

━━━━━━━━━━━━━━━━━━━━
💰 当前资产结构
纳指仓位占比：{decision['qqq_ratio']}%

💵 本次投入：{decision['invest']} 元人民币

━━━━━━━━━━━━━━━━━━━━
📌 今日策略建议：
"""

    for a in decision["action"]:
        msg += f"• {a}\n"

    msg += "\n━━━━━━━━━━━━━━━━━━━━"

    print(msg)
    send(msg)

    save(portfolio)


if __name__ == "__main__":
    run()