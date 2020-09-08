# Word Crawler API

This a RESTful API using Flask and Beautifulsoup4 that performs a web crawler in a brazilian dictionary called Dicionário Criativo. 

This API allows that you find relative words through a word that you search.


### Search a word

	GET https://words-crawler.herokuapp.com/related_words?term=name


### How to run this project

- Clone this repo
- `pip install <package-name>` the dependencies 
- After install the dependencies run `python main.py` to run the project. Use [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to test the API in your Postman (or another software)

### Technologies 

- Python 
- Flask 
- Beautifulsoup 

### To do 

- Improve API results data model 
- Create a `get_all` endpoint to GET all words saved
- Unit tests
