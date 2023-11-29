from constants import variable


def stringify(value: str | float | None) -> str:
    if value:
        return str(value)
    else:
        return "None"


if __name__ == "__main__":
    assert stringify(value="12") == "12"
    assert stringify(value=15) == "15"
    assert stringify(value=.5) == "0.5"
    assert stringify(value=None) == "None"
