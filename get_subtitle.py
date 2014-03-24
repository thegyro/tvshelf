import os
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File

source_dir = '/home/pydomic/Watch/Desktop/TV'

def get_subtitle(filename):
    os_sub = OpenSubtitles()
    try:
        token = os_sub.login('thegyro','idontlikepasswords')
        if os.path.exists(os.path.join(sourcedir,filename)):
            video_file = File(os.path.join(sourcedir,filename))
            video_hash = video_file.get_hash()
            video_size = video_file.size
            sub_param = {'sublanguageid':'English','moviehash':video_hash,'moviebytesize': video_size}
            subtitles = os_sub.search_subtitles([sub_param])
            print subtitles
        else:
            raise Exception('FileError')
        
    except Exception as ex:
        print str(ex)
