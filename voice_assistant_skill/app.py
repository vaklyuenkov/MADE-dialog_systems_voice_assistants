import json
from flask import Flask, request
import dialogflow_v2
from config import keys
import json
import logging

app = Flask(__name__)

sessionStorage = {}

session_client = dialogflow_v2.SessionsClient()
session_path = session_client.session_path(keys.values['googleProjectID'], keys.values['dialogFlowSessionID'])


@app.route("/marusya", methods=['POST', 'GET'])
def marusya():
    return "Marusya"

@app.route("/")
def hello():
    return "Welcome!"

@app.route("/story", methods = ['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)
    card = {}
    buttons = []

    if request.json['session']['new']:
        text = 'Привет, человек! Я - Печенька! А как зовут тебя? Я знаю много разных историй из жизни. Только попроси рассказать историю и проси ещё, если понравилось! Печенька полна байками.'
    elif request.json['request']['command'] == 'on_interrupt':
        text = "Приходи еще, у печеньки осталось много историй для тебя! "
    else:
        text_input = dialogflow_v2.types.TextInput(text=request.json['request']['command'], language_code=keys.values['dialogFlowSessionLanguageCode'])
        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        df_response = session_client.detect_intent(session_path, query_input)
        text = df_response.query_result.fulfillment_text

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False,
            "text": text
        }
    }

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

if __name__ == "__main__":
    app.run(debug = True)
