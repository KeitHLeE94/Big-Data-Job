import elasticsearch
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)
es_client = elasticsearch.Elasticsearch('localhost:9200')


doc = es_client.search(index='_all', body={
  "query": {
    "match_phrase": {
      "title": "1단계"
    }
  }
})


@app.route('/')
def index():
    print(json.dumps(doc, ensure_ascii=False, indent=2))
    return render_template('index.html')


@app.route('/shop-grid')
def shop_grid():
    return render_template('shop-grid.html')


if __name__ == '__main__':
    app.run()
