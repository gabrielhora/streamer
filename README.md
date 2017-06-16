# Streamer

Simple way to stream any single PostgreSQL query using [NDJSON](http://ndjson.org/).

## How to use

There is a single endpoint `POST /` with two parameters, `query` and `params`.

These are some body examples: 

```json
{
  "query": "SELECT * FROM table WHERE field = %s",
  "params": ["value"]
}
```

```json
{
  "query": "SELECT * FROM table WHERE int_field = %(param1)s AND str_field = %(param2)s",
  "params": {
    "param1": 123, 
    "param2": "value2"
  }
}
```

## Running

Run locally:

```
$ pip install virtualenv
$ virtualenv venv
$ . venv\bin\activate
(venv) $ pip install -r requirements.txt
(venv) $ python app/main.py
```

Or use docker:

```
$ docker build -t streamer .
$ docker run --rm -p 80:80 streamer
```
