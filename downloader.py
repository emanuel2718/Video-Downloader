#!/usr/bin/env python

from datetime import datetime
import os
import tqdm
import re
import requests



# Author: Emanuel Ramirez Alsina
# Date: 03/26/2020

def main():
    '''TODO: Make some kind of menu:
            1. YouTube
            2. Facebook
            3. Instagram
            4. Tik Tok
    '''
    #TODO: Make some kind of intro message.
    #TODO: Defaults into hd quality and if not available give SD quality...or
    # ask user for the format?
    platform = input('\nPlease enter the name of the platform to get a video'
                     + ' from: ')
    # TODO: Maybe format the platform:
    # User input 'youtube' -> YouTube

    url = input(f'\nEnter the URL of the {platform} video: ')

    #TODO: Do something to check the validity of the url. For now
    html = requests.get(url).content.decode('utf-8')

    # This is temporal until menu is implemented.
    if platform.upper() == 'FACEBOOK':
        get_facebook(url, html)


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
                    desc=filename, ascii=False)

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



if __name__ == '__main__':
    main()


