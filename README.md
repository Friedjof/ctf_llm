# ChatGPT CTF Challenge
## Description
This is a CTF challenge based on the ChatGPT API. The goal is to find the flag by chatting with the bot.

## Setup
Installing the requirements:
```bash
pip install -r requirements.txt
```

Generating the flag:
```bash
python3 setup.py
```

Running the server:
```bash
python3 server.py
```

Open another terminal and send a POST request with the `client.py` script:
```bash
python3 client.py
```

## Instructions
Now try to elicit the flag from the model in the client terminal via the chat. Any means is allowed.
If you think you have the flag, enter `!flag{<flag>}` in the chat. If you are right, the server will respond with `Correct!` if the flag is correct, otherwise it will respond with `Incorrect!`.