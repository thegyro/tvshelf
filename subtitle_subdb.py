import urllib2
import urllib
import os

 source_dir = '/home/pydomic/Desktop/TV/'
 
def get_hash(name):
    readsize = 64*1024
    try:
        fullname = os.path.join(source_dir,name)
        with open(fullname,'rb') as f:
            size = os.path.getsize(fullname)
            data = f.read(readsize)
            f.seek(-readsize,os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

    except IOError as err:
        print str(err)


def get_subtitle(filename):
    video_hash = get_hash(filename)
    url = 'http://api.thesubdb.com/'
    try:
        query = urllib.urlencode({'action':'download','hash':video_hash,'language':'en'})
        request = urllib2.Request(url + '?' + query)
        request.add_header('User-Agent','SubDB/1.0 (tvshelf/0.1; http://github.com/thegyro/tvshelf)')
        response = urllib2.urlopen(request)
        if response.getcode() == 200:
            with open(os.path.join(source_dir,filename + '.srt','w')) as sub_f:
                f.write(response.read())
    
        elif reponse.getcode() == 404:
            raise Exception('Subtitle Not Found')

        else:
            raise Exception('Bad Request')
            
    except (urllib2.URLError,Exception,IOError) as err:
        print str(err)
