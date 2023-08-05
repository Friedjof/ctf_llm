import regex as regex
import requests

if __name__ == '__main__':
    url = 'http://localhost:5000/chat'

    try:

        while True:
            user_input = input("$> ")
            # if the user input matches `!flag{...}`, use regex to detect it
            if regex.match(r"!flag\{.*\}", user_input):
                # Extract the flag from the user input between the curly braces
                flag = regex.search(r"!flag\{(.*)\}", user_input).group(1)

                r = requests.post("http://localhost:5000/verify", data={
                    'flag': flag
                })

                if r.text == "Correct!":
                    print("Correct flag!")
                    exit(0)
                else:
                    print("Incorrect flag!")
                    continue

            # POST request to the server
            r = requests.post(url, data={
                'prompt': user_input,
                'ctf_version': 'v1'  # This is the version of the llm prompt
            })
            print(r.text)

    except KeyboardInterrupt:
        print("Exiting...")
