import urllib.request

def get_panel(url):
    try:
        openurl = urllib.request.urlopen(url)
        wordlist = open("wordlist.txt")
        for i in wordlist:
            i = i.strip("\n")
            fullurl = url+i
            try:
                openurl2 = urllib.request.urlopen(fullurl)
                print("Admin Panel Found >> "+fullurl)
                break
            except urllib.error.HTTPError as err:
                print("Not Found !! >> "+fullurl)
                print(err)
    except urllib.error.HTTPError as error:
        print(url)
        print(error)

url = input("Enter URL :")
get_panel(url)
