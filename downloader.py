#!/usr/bin/env python

from datetime import datetime
import os
import tqdm
import re
import requests
import urllib.request



# Author: Emanuel Ramirez Alsina
# Date: 03/26/2020

PLATFORMS = ['YouTube', 'Facebook', 'Instagram', 'Twitter', 'TikTok']
SIZE = 1024

def driver(platform, option):
    #TODO: Add a connection check.
    url = input(f'\nEnter the URL of the {platform} video: ')
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
    #TODO: Add video option
    #TODO: Deal with private profiles images/videos.
    print(f'\nDownloading image...')

    image = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)',\
                     html).group()

    image_link = re.sub('meta property="og:image" content="', '', image)
    request_size = requests.get(image_link, stream=True)
    request_status = requests.get(url).status_code
    file_size = int(request_size.headers['Content-Length'])

    filename = input('\nEnter a filename without extensions to save the image: ')
    path = os.path.dirname(__file__)
    new_path = f'images/{filename}.png'

    loadbar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                    desc=filename + '.png', ascii=False)

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
    pass

def get_tiktok(url, html):
    pass

def display_menu():

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
    display_menu()



