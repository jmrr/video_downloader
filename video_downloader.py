# batch video downloader from multiple sources
# Jose Rivera - January 2016
import os
import argparse
from subprocess import call


parser = argparse.ArgumentParser(description="Uses youtube-dl to download a list of videos specified in a text file")
parser.add_argument('-o', '--output', dest='output_path', help='Output path where to store the downloaded videos')
parser.add_argument('-i', '--input', dest='input_file', help='Path to the input file containing the video URLs')
parser.add_argument('-t', '--titles', dest='titles_file', help='Path to the titles file')
parser.add_argument('-d', '--divider', dest='divider', help='String that divides titles in groups')

args = parser.parse_args()

titles_file = open(args.titles_file)
videos_file = open(args.input_file)

if args.divider is not None:
    divider = args.divider
else:
    divider = ""
    save_path = args.output_path

volume_counter = 1
video_counter  = 1

for line in titles_file:
    if divider in line and divider != "":
        save_path = os.path.join(args.output_path, divider + " " + str(volume_counter))
        volume_counter += 1
        if not os.path.exists(save_path) and os.path.isdir(save_path):
            print 'Creating directory {0}...'.format(save_path)
            os.makedirs(save_path)
    else:
        if not (os.path.exists(save_path) and os.path.isdir(save_path)):
            print 'Creating directory {0}...'.format(save_path)
            os.makedirs(save_path)
        title_str = line.rstrip('\n').split(' ')

        video_save_path = os.path.join(save_path, '{:02d}'.format(video_counter) +
                                       ' [' + title_str[0] + '] ' + ' '.join(title_str[1:]) + '.mp4')
        video_counter += 1
        if os.path.exists(video_save_path):
            print "This video has already been downloaded. Skipping..."
        else:
            url = videos_file.readline()
            print 'Downloading file from URL: {0}...\nSaving to {1}'.format(url, video_save_path)
            call(['youtube-dl', '-o', video_save_path, url])

titles_file.close()
videos_file.close()

