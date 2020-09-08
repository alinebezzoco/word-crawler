import requests
from bs4 import BeautifulSoup
from urllib import parse
from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)


class RelatedWords(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('term', required=True,
                            help='A search term needs to be provided')
        args = parser.parse_args()

        word_query = parse.urlencode(args).replace('term=', '')

        r = requests.get(
            f'https://dicionariocriativo.com.br/{word_query}')

        soup = BeautifulSoup(r.text, 'html.parser')

        tags = soup.find_all('ul', {'class': 'tags'})

        results = []

        results.append({'name': word_query})

        for tag in tags:
            list = tag.find_all('li')
            for w in list:
                word = w.find('a').text

                results.append({
                    'related_words': {
                        'word': word,
                    }
                })

        with open("data/data.json", "w") as writeJSON:
            json.dump(results, writeJSON, ensure_ascii=False)

        return results


api.add_resource(RelatedWords, '/related_words')


# A welcome message
@app.route('/')
def index():
    return "<h1>Real-time word crawler API with Beaufitulsoup and Flask</h1>"


if __name__ == '__main__':
    app.run(debug=True)
