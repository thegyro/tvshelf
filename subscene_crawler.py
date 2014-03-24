import urllib
import urllib2
import zipfile
import os
from bs4 import BeautifulSoup

#woudln't generally want to use globals
subtitle_url = 'http://subscene.com'

def get_subtitle_zip(tvshow):
    path = '/subtitles/release?'
    if tvshow['showid']:
        show = tvshow['show'] + ' ' + tvshow['showid']
    else:
        show = tvshow['show'] + ' ' + tvshow['res']
    query = urllib.urlencode({'q':show})
    print subtitle_url + path + query
    request = urllib2.Request(subtitle_url + path + query)
    request.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
    request.add_header('Cookie','LanguageFilter=13')
    response = urllib2.urlopen(request)

    html_soup = BeautifulSoup(response)
    tv_episodes = html_soup.tbody.find_all('tr')
    episode_links = [(episode.a['href'],episode.find_all('span')[1].text.strip('\r\n\t ')) for episode in tv_episodes]

    link_path = match_subtitle(episode_links,tvshow)[0]

    print subtitle_url + link_path
    sub_resp_soup = BeautifulSoup(urllib2.urlopen(subtitle_url + link_path))
    download_link_path = str(sub_resp_soup.find_all('div',class_='download')[0].a['href'])

    filename = '/home/pydomic/Desktop/TV/' + tvshow['show'] + ' ' + tvshow['showid'] + '.zip'
    print "\n Downloading the required subtitle... \n"
    urllib.urlretrieve(subtitle_url + download_link_path,filename)
    return filename
    
def extract_subtitle(filename):
    try:
        with zipfile.ZipFile(filename,'r') as fzip:
            print "Extracting the subtitle... \n"
            fzip.extractall('/home/pydomic/Desktop/TV/')
            print "Removing the useless zip file... \n"
            os.remove(filename)
            print "Done! Yay!! \n"
            name = fzip.namelist()[0]
            print "Fuck",name
            return '/home/pydomic/Desktop/TV/' + name

    except (IOError,zipfile.BadZipfile,zipfile.LargeZipFile) as err:
        print str(err)
        
def match_subtitle(links,tvshow):
    match_links_best = []
    match_links_ok = []
    match_links_fuck = []
    for link in links:
        check_name = tvshow['show'] + ' ' + tvshow['showid']
        link_str = str(link[1])
        if check_name.replace(' ','.') in link_str:
            if tvshow['res'] in link_str  and (tvshow['encoding'] in link_str or tvshow['encoding'].capitalize() in link_str):
                match_links_best.append(link)
            elif tvshow['res'] in link_str or tvshow['encoding'] in link_str:
                match_links_ok.append(link)
            else:
                match_links_fuck.append(link)

    if match_links_best:
        return match_links_best[0]
    elif match_links_ok:
        return match_links_ok[0]
    elif match_links_fuck:
        return match_links_fuck[0]
    else:
        return None
