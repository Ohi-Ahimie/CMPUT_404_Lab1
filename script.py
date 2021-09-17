import requests

def main():
    r = requests.get('https://raw.githubusercontent.com/Ohi-Ahimie/CMPUT_404_Lab1/master/script.py')
    print(r.text)

main()