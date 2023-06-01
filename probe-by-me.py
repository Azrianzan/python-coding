import requests

URL_file = input("What is the name of the URL list file? ")
out_file = input("WHat is the name of the output file you want? ")

# Open the URL list file, read it, & close it
f = open(URL_file, 'r')
URL_list = f.readlines()
f.close()
# Process the text data and store it in a list
test_url = []
for line in URL_list:
    # Remove newline characters and any additional processing if needed
    # strip() method will remove leading & trailing whitespace characters (spaces, tabs, and newliens)
    line = line.strip()
    test_url.append(line)

# Make a process to test if the URL is alive
goodURL = []
badURL = []
for url in test_url:
    try:
        response = requests.head(url)
        if response.status_code == 200:
            goodURL.append(url)
    except requests.exceptions.MissingSchema():
        badURL.append(url)
        continue
    except requests.exceptions.ConnectionError():
        badURL.append(url)
        continue

with open(out_file, 'w') as file:
    for item in goodURL:
        file.write(item + '\n')
    file.close()

print(f"The good URLs have been saved to {out_file}")