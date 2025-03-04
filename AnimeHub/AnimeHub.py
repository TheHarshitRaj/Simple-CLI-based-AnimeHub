import webbrowser
import time
import json

def inputAndSearch():
    name=input("Enter anime name: ").capitalize().strip()

    time.sleep(0.3)
    print("Searching")
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('..')
    time.sleep(0.5)
    print("Redirecting..")

    webbrowser.open(f'https://myanimelist.net/search/all?q={name}')


AnimeList={}
Upd_list={}

MainList={}

def create_watchlist():
    category=input('Enter your category (Plan to watch, Watching, Completed, Dropped): ').lower().strip()
    if category=='plan to watch':
        MainList['Plan to Watch']=AnimeList
    elif category=='watching':
        MainList['Watching']=AnimeList
    elif category=='completed':
        MainList['Completed']=AnimeList
    elif category=='dropped':
        MainList['Dropped']=AnimeList
    else:
        print("Couldn't understand what you said. Try again.")

    print("\nType the name of Anime you want to add to your Watchlist, when done, type 'Exit'\n")

    while True:
        name=input(": ").capitalize().strip()

        if name=='Exit':
            break

        link=f'https://myanimelist.net/search/all?q={name.replace(' ', '+')}'
        AnimeList[name]=link

    with open('Watchlist.txt', 'w') as f:
        json.dump(MainList,f, indent=4)


def edit_watchList():
    category=input('Enter your category (Plan to watch, Watching, Completed, Dropped): ').capitalize().strip()

    with open('Watchlist.txt','r') as file:
        MainList=json.load(file)
    if category.capitalize() not in MainList.keys():
        if category=='Plan to watch':
            MainList['Plan to watch']=Upd_list
        elif category=='Watching':
            MainList['Watching']=Upd_list
        elif category=='Completed':
            MainList['Completed']=Upd_list
        elif category=='Dropped':
            MainList['Dropped']=Upd_list
        else:
            print("Couldn't understand what you said. Try again.")
            exit()

        print("\nType the name of Anime you want to add to your Watchlist, when done, type 'Exit'\n")

        while True:
            name=input(": ").capitalize().strip()

            if name=='Exit':
                break

            link=f'https://myanimelist.net/search/all?q={name.replace(' ', '+')}'
            Upd_list[name]=link

        with open('Watchlist.txt','w') as f:
            json.dump(MainList,f,indent=4)
        
    else:
        with open('Watchlist.txt','r') as f:
            MainList = json.load(f)

        print("\nType the name of Anime you want to add to your Watchlist, when done, type 'Exit'\n")

        while True:
            name=input(": ").capitalize().strip()

            if name=='Exit':
                break

            link=f'https://myanimelist.net/search/all?q={name.replace(' ', '+')}'
            MainList[category][name]=link

        with open('Watchlist.txt','w') as f:
            json.dump(MainList,f,indent=4)
def watch():
    name=input("Enter the name of the Anime: ").capitalize().strip()

    destination=input("Choose the website.\na)HiAnime\nb)Miruro\nc)AnimeZ\nd)AnimeKai\n:").lower().strip()
    print('Redirecting..')

    if destination=='a':
        webbrowser.open(f'https://hianime.sx/search?keyword={name}')
    elif destination=='b':
        webbrowser.open(f'https://www.miruro.tv/search?query={name}')
    elif destination=='c':
        webbrowser.open(f'https://animez.org/?act=search&f[keyword]={name}')
    elif destination=='d':
        webbrowser.open(f'https://animekai.to/browser?keyword={name}')


ask=input("What do you want to do?\na) Search for an Anime\nb) Watch some Anime\nc) Create your watchlist\nd) Edit your Watchlist\n:").lower().strip()

if ask=='a':
    inputAndSearch()
elif ask=='b':
    watch()
elif ask=='c':
    create_watchlist()
    print("Watchlist created and saved successfully. Closing the program")
elif ask=='d':
    edit_watchList()
    print("Watchlist updated successfully. Closing the program")
