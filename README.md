This scripts gets a random image from the [windows spotlight](https://en.wikipedia.org/wiki/Windows_spotlight) api endpoint and saves it in `~/.config/spotlight-imgs/current.png` (the old one is saved in `~/.config/spotlight-imgs/history`) so you can enjoy spotlight backgrounds with your favourite lockscreen.

For i3lock:

`i3lock -i ~/.config/spotlight-imgs/current.png`

To set a new image:

`python3 main.py`

you'll have to figure out multi monitor stuff out for yourself. Only 1920*1080 imgs are downloaded. See source if you want to know more.
