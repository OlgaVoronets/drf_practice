import requests


def convert_currency(amount, cur):
    """Функция получения стоимости в указанной валюте"""
    if cur.lower() == 'usd':
        return round(amount * 89.5)
    elif cur.lower() == 'eur':
        return round(amount * 96)


def send_tg_message(chat_id, text):
    """Функция отправки сообщения в телеграм"""
    token = 'сюда свой токен'
    url_ = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    response = requests.post(url_)
    print(response.text)


if __name__ == '__main__':
    send_tg_message('сюда свой чат-айди', 'test_text')
