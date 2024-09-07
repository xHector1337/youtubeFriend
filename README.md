![Ekran görüntüsü 2024-09-07 170424](https://github.com/user-attachments/assets/c1b47020-e928-4c8e-b904-2f426782c930)


YoutubeFriend is a youtube video downloader which uses pytube library.

# Setup

```
pip install -r requirements.txt
```
# Usage
Here is the all arguments videodownloader.py takes:
```
python videodownloader.py url filetype --lowestresolution --path
```
The arguments start with **--** are optional!
Here is an example usage:

```
python videodownloader.py https://www.youtube.com/watch?v=OiIe2znA1ao mp3
```
And another example usage:
```
python videodownloader.py https://www.youtube.com/watch?v=2-ok_i3W3Zg mp4 --lowestresolution --path /home/hector/Desktop/hello
```
Now it'll save the video as the lowest resolution available and file will be in `/home/hector/Desktop/hello` directory.

Happy downloading!!!
