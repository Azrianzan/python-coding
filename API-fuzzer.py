# you can run this script with this command in Kali Linux
# "cat small.txt| python3 API-fuzzer.py"
# small.txt is a txt wordlist that comes pre-installed with Kali
# you can add 'api' and 'docs' to that wordlist
# this script is designed for Hackthebox-Backend box
# I copy this script from PhD Security
import requests
import sys

def loop():
    for word in sys.stdin:
        #costumize the url you want do fuzzing
        response = requests.get(url=f"http://10.10.11.161/{word}")
        if response.status_code == 404:
            loop()
        else:
            print(word)
            print(response.status_code)
            data = response.json()
            print(data)
            #print(response)

loop()