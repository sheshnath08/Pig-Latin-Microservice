from flask import Flask, make_response, request

app = Flask(__name__)

def make_pig_latin_translation(words):
    words = 'test'
    return words

@app.route('/translate', methods=['POST'])
def pig_latin_translate():
    """Handles the translation of English to Pig-Latin"""
    data = request.stream.read().decode('utf-8')
    if not data:
        response = make_response("POST request for translation must contains at least one word.")
        request.status_code = 400 #Bad request
        return response
    translated_data = make_pig_latin_translation(data)
    response = make_response(translated_data)
    response.status_code = 200 #HTTP_OK
    return response


if __name__ == '__main__':
    app.run(port=80, debug=True)
