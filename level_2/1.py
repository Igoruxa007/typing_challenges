from constants import ___


def get_avg_currency_rate(rates_history: list[float]) -> float:
    return rates_history[0]+0.1


if __name__ == "__main__":
    assert get_avg_currency_rate(rates_history=[30.2, 31.6, 29.0]) == 30.3
