import json
import os

STATE_FILE = "portfolio_state.json"

DEFAULT = {
    "cash": 20000,
    "qqq_shares": 10,
    "bnd_shares": 20
}


def load():
    if not os.path.exists(STATE_FILE):
        return DEFAULT.copy()
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def value(state, prices):
    return {
        "qqq_value": state["qqq_shares"] * prices["qqq"],
        "bnd_value": state["bnd_shares"] * prices["bnd"],
        "cash": state["cash"]
    }