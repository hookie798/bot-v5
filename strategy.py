def decide(portfolio, prices):

    qqq_val = portfolio["qqq_shares"] * prices["qqq"]
    bnd_val = portfolio["bnd_shares"] * prices["bnd"]
    total = qqq_val + bnd_val + portfolio["cash"]

    qqq_ratio = qqq_val / total if total > 0 else 0

    invest = 100
    actions = []

    # 📉 回撤策略
    if prices["qqq_dd"] < -20:
        invest = 200
        actions.append("📉 市场大幅回撤：启动加倍定投")

    # ⚠️ 仓位过高
    if qqq_ratio > 0.7:
        actions.append("⚠️ 纳斯达克仓位过高：建议增加债券配置")

    # 📈 估值偏高
    if prices["qqq"] > 500:
        actions.append("📈 市场估值偏高：建议控制风险敞口")

    # 🟢 默认情况
    if not actions:
        actions.append("✅ 市场正常：继续每日定投")

    return {
        "invest": invest,
        "action": actions,
        "qqq_ratio": round(qqq_ratio * 100, 2)
    }
