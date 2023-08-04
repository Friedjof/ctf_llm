import requests

if __name__ == '__main__':
    url = 'http://localhost:5000/chat'

    try:
        while True:
            # POST request to the server
            r = requests.post(url, data={
                'prompt': input('> '),
                'ctf_version': 'v1'  # This is the version of the llm prompt
            })
            print(r.text)
    except KeyboardInterrupt:
        print("Exiting...")
