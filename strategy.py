DAILY_DCA = 200


def decide(portfolio, prices):

    qqq = portfolio["qqq_value"]
    bond = portfolio["bond_value"]

    total = qqq + bond
    qqq_ratio = qqq / total if total > 0 else 0

    actions = []
    invest_qqq = DAILY_DCA
    invest_bond = 0

    # 📉 回撤加仓
    if prices["qqq_dd"] < -15:
        invest_qqq = 300
        actions.append("📉 回撤较大：纳指加倍投入")

    # ⚠️ 纳指过高 → 建议买债券
    if qqq_ratio > 0.72:
        invest_bond = 100
        invest_qqq = 100
        actions.append("⚠️ 纳指仓位过高：建议分配债券")

    # 📊 正常情况
    if not actions:
        actions.append("✅ 正常定投：纳指200元")

    return {
        "qqq_buy": invest_qqq,
        "bond_buy": invest_bond,
        "qqq_ratio": round(qqq_ratio * 100, 2),
        "actions": actions
    }
