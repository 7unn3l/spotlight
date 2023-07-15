This scripts gets a random image from the [windows spotlight](https://en.wikipedia.org/wiki/Windows_spotlight) api endpoint and saves it in `~/.config/spotlight-imgs/current.png` (the old one is saved in `~/.config/spotlight-imgs/history`) so you can enjoy spotlight backgrounds with your favorite lockscreen.

For i3lock:

`i3lock -i ~/.config/spotlight-imgs/current.png`

To set a new image:

`python3 spotlight.py` (you could set it up to run on startup)

you'll have to figure out multi monitor stuff out for yourself. Only 1920*1080 imgs are downloaded. See source if you want to know more.

I've also tried to reverse engineer LockApp.exe and the inner workings of the whole spotlight process (you can also give nudges towards which sort of pictures you like)
but was unable to make any meaningful progress for now. If anyone has more info, I'd like to know. [this](https://github.com/Biswa96/WinLight/blob/master/Developers.md) has some interesting stuff.
