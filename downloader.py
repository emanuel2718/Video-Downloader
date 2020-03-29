#!/usr/bin/env python

from datetime import datetime
import os
import tqdm
import re
import requests



# Author: Emanuel Ramirez Alsina
# Date: 03/26/2020


PLATFORMS = ['YouTube', 'Facebook', 'Instagram', 'Twitter', 'TikTok']

def driver(platform, option):
    #TODO: Defaults into hd quality and if not available give SD quality...or
    # ask user for the format?
    url = input(f'\nEnter the URL of the {platform} video: ')
    #TODO: Do something to check the validity of the url. For now
    html = requests.get(url).content.decode('utf-8')

    #TODO: This is temporal. Refactor this
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
    #TODO: check if hd quality is available if not then download in sd?
    size = 1024
    qualityhd = re.search('hd_src:"https', html)
    url_video = re.search(r'hd_src:"(.+?)"', html).group(1)
    request_size = requests.get(url_video, stream=True)
    request_status = requests.get(url).status_code
    file_size = int(request_size.headers['Content-Length'])

    #TODO: Format to: "Save as: {filename}.mp4"
    filename = input('\nEnter a filename without extensions to save the video: ')
    path = os.path.dirname(__file__)
    new_path = f'videos/{filename}.mp4'

    print(f'\nDownloading video...')
    print(f'Filename: {filename}.mp4')

    loadbar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                    desc=filename + '.mp4', ascii=False)

    with open(new_path, 'wb') as filehandler:
        for content in request_size.iter_content(size):
            loadbar.update(len(content))
            filehandler.write(content)
    loadbar.close()
    filehandler.close()
    if request_status == 200:
        print('\nDownload status: Succesfull!')
    else:
        print('\nDownload status: Failed.')


def get_insta(url, html):
    pass

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

    option = int(input("\nPlease choose an option: "))
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



