# Batch video downloader

Simple script that uses `youtube-dl` to download a batch of videos (that are allowed to distribute or are free) from
multiple video hosting services such as Youtube or Wistia.

## Requirements
*[youtube-dl](https://rg3.github.io/youtube-dl/index.html)

Quick installation of the binary on Linux/Mac:

 ```
sudo curl https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
 ```

 ## Usage

Apart from the destination of the files, `video_downloader` requires two text files as inputs, one for the list of URLs
and the other for the list of titles.

 ```
 python video_downloader.py -o output_location -i input.txt -t video_titles.txt
 ```