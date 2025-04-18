# learn-fast-api
Based on this video https://www.youtube.com/watch?v=iWS9ogMPOI0

## Installing Fast API

pip3 install fastapi
pip3 install uvicorn

## Finding your Python Path

ganapathychidambaram@Ganapathys-MacBook-Air git-projects % which python3

/opt/homebrew/bin/python3

## Setting up Pycharm 

1. This is to resolve the import errors
2. Open project settings
3. Go to Python interpreter, add local interpreter.
4. Select "Existing", add above path - /opt/homebrew/bin/python3

## Starting the Server

1. uvicorn main:app --reload

Do the above from the same directory where main.py is located.

## Browser based requests and curls

http://127.0.0.1:8000/
http://127.0.0.1:8000/items/1

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=orange'
