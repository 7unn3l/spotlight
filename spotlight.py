from requests import *
import json
from random import choice,randint
import os
import datetime
from subprocess import call

SAVE_DIR = os.path.expanduser('~/.config/spotlight-imgs')

def rand_str(n):
    return ''.join([chr(randint(97,122)) for _ in range(n)])

def rand_locale():
    return choice(open('locales.txt').read().splitlines()).strip()

def set_img(imgurl):
    if not os.path.exists(SAVE_DIR+'/history'):
        os.makedirs(SAVE_DIR+'/history',exist_ok=True)
   
    # first back up currrent img
    if os.path.exists(SAVE_DIR+'/current.png'):
        # current date is name
        d = datetime.datetime.now().strftime("%Y-%m-%d")
        org = SAVE_DIR+f'/history/{d}'
        name = org
        i = 0
        while True:
            i += 1
            if not os.path.exists(name+'.png'):
                break
            name = f'{org}-{i}'


        name = name+'.png'
        print(f'renaming {SAVE_DIR}/current.png to {name}')
        os.rename(SAVE_DIR+'/current.png',name)

    call(['wget','-O',SAVE_DIR+'/current.jpg',imgurl])
    call(["convert",SAVE_DIR+'/current.jpg',SAVE_DIR+'/current.png'])
    os.remove(SAVE_DIR+'/current.jpg')

def get_random_img():
    head= {
        'Accept-Encoding': 'gzip, deflate',
        'Cache-Control': 'no-cache',
        'User-Agent': 'WindowsShellClient/9.0.40929.0 (Windows)'
    }

    # pids seen in the wild
    pid = choice([209567,279978,338380,338387])

    '''
    yes this is really weird. I have yet to discover how this endpoint really works.
    But from test I've seen multiple things:
        - the exact same urls spits out different images on different requests (but only a finite ammount)
        - the country (ctr) parameter can be a string of up to 32 chars. It does affect the images... somehow.
            - I wonder if they do some sort of hashing?
        - the locale (lc) param however is checked if it is a real locale
    '''

    
    ctry = rand_str(randint(2,30))
    lc = rand_locale()

    
    url = f"https://arc.msn.com/v3/Delivery/Placement?pid={pid}&fmt=json&cdm=1&lc={lc}&ctry={ctry}"
    print(f'[*] api url = {url}')
    res = get(url,headers=head).json()

    
    imgs = []

    res = res["batchrsp"]
    for item in res["items"]:
        item = item["item"]
        data = json.loads(item)
    

        for k,v in data["ad"].items():
            if 'image_' in k:
                if v["w"] == "1920" and v["h"] == "1080":
                    url = v["u"]
                    imgs.append(url)

    return choice(imgs)

if __name__ == '__main__':
    print("[*] Getting random image")
    set_img(get_random_img())
