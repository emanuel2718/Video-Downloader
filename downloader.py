#!/usr/bin/env python

from datetime import datetime
from pytube import YouTube as YT
from pytube.cli import on_progress

import httplib2
import os
import pytube
import re
import requests
import tqdm
import urllib.request


# Author: Emanuel Ramirez Alsina
# Date: 03/26/2020

PLATFORMS = ['YouTube', 'Facebook', 'Instagram', 'Twitter', 'TikTok']
OS = ""
SIZE = 1024

def driver(platform, option):
    url = input(f'\nEnter the URL of the {platform} content you want to' +\
                ' download: ')
    html = requests.get(url).content.decode('utf-8')

    if option == 0:
        get_youtube(url, html)
    elif option == 1:
        get_facebook(url, html)
    elif option == 2:
        get_instagram(url, html)
    elif option == 3:
        get_twitter(url, html)
    elif option == 4:
        get_tiktok(url, html)
    elif option == 5:
        exit(1)

def connection_established():
    try:
        response = urllib.request.urlopen('https://www.google.com/',\
                                          timeout=5)
        return True
    except:
        return False

def get_facebook(url, html):
    url_video = re.search(r'hd_src:"(.+?)"', html).group(1)
    request_size = requests.get(url_video, stream=True)
    request_status = requests.get(url).status_code
    file_size = int(request_size.headers['Content-Length'])

    filename = input('\nEnter a filename without extensions to save the video: ')
    path = os.path.dirname(__file__)
    new_path = f'videos/{filename}.mp4'

    print(f'\nDownloading video...')
    print(f'Filename: {filename}.mp4')

    loadbar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                    desc=filename + '.mp4', ascii=False)

    with open(new_path, 'wb') as filehandler:
        for content in request_size.iter_content(SIZE):
            loadbar.update(len(content))
            filehandler.write(content)
    loadbar.close()
    filehandler.close()

    if request_status == 200:
        print('\nDownload status: Succesfull!')
    else:
        print('\nDownload statut: Failed.')


def get_instagram(url, html):
    #TODO: Deal with private profiles images/videos.
    print(html)
    exit()
    options = {'image':'png', 'video':'mp4'}

    # Check wheter the link refers to an image or a video.
    content_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)',\
                             html).group(1)

    print(f'\nDownloading {content_type}...')

    image = re.search(r'meta property="og:{file}" content=[\'"]?([^\'" >]+)'\
                     .format(file=content_type), html).group()

    image_link = re.sub('meta property="og:{file}" content="'\
                        .format(file=content_type), '', image)
    request_size = requests.get(image_link, stream=True)
    request_status = requests.get(url).status_code
    file_size = int(request_size.headers['Content-Length'])

    filename = input(f'\nSave {content_type} as: ')
    path = os.path.dirname(__file__)
    new_path = f'{content_type}s/{filename}.' + options[content_type]

    loadbar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                    desc=filename + '.' + options[content_type], ascii=False)

    with open(new_path, 'wb') as filehandler:
        for content in request_size.iter_content(SIZE):
            loadbar.update(len(content))
            filehandler.write(content)
    loadbar.close()
    filehandler.close()

    if request_status == 200:
        print('\nDownload status: Succesfull!')
    else:
        print('\nDownload statut: Failed.')


def get_youtube(url, html):
    #TODO: Only accept YouTube url's
    h = httplib2.Http()
    response = h.request(url, 'HEAD')
    if int(response[0]['status']) < 400:
        print('\nDownload status: OK!')
    else:
        print("\nUrl not found. Please try again with full address (i.e)" +\
              " 'https://youtube.com/...'\n")
        sys.exit(1)

    filename = input('Save as: ')
    yt = YT(url, on_progress_callback=on_progress)
    title = yt.title
    print(f'Downloading {title}')

    # Taken from https://stackoverflow.com/a/60678355.
    yt.streams\
          .filter(file_extension='mp4')\
          .get_lowest_resolution()\
          .download('videos/', filename=filename)

    print('\n')
    # Check status of video.
    print('Download succesful!\n')


def get_tiktok(url, html):
    pass

def get_twitter(url, html):
    pass

def display_menu():
    '''Displays the CLI menu to the user.'''

    print()
    print('      ------------------------------------------- ')
    print('     |                                           |')
    print('     |        Welcome to VIDEO-DOWNLOADER        |')
    print('     |            by Emanuel Ramirez             |')
    print('     |                                           |')
    print('      ------------------------------------------- ')

    print('\nChoose the appropiate option for the platform from which you want'
          + ' to get a video from.')
    print('\n0. YouTube')
    print('1. Facebook')
    print('2. Instagram')
    print('3. Twitter')
    print('4. TikTok')
    print('5. Exit')

    option = int(input("\nOption > "))
    if option == 5:
        print('Thank you for using Video-Downloader.\n')
        exit()
    try:
        if option < 5:
            pass
        else:
            print('\nOption not available. Chose an option from 1-5.\n')
            exit()
    except:
        exit()

    platform = PLATFORMS[option]
    driver(platform, option)


if __name__ == '__main__':
    import platform
    import sys

    if platform.system() == 'Darwin':
        OS = 'Darwin'
    elif platform.system() == 'Windows':
        OS = "Windows"
    elif platform.system() == 'Linux':
        OS = "Linux"


    #TODO: add system argument parsing


    # Check for python3.
    if sys.version_info[0] == 2:
        print('Python3 is required.')
        sys.exit(1)

    # Check if user is connected to the internet.
    if not connection_established():
        print('\nConnection status: DOWN')
        print('\nConnect to the internet and try again.')
        exit()
    else:
        print('\nConnection: OK!')
        display_menu()



