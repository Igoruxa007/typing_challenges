from constants import variable


def send_email(header: str, text_content: str, send_to: str) -> None:
    print(header)


if __name__ == "__main__":
    assert send_email(header="Test email", text_content="This is a test email", send_to="test@gmail.com") is None