import os
from myfiledataextractor import *
from subtitle_crawler import *

def isVideoFile(filename):
	eligibleExtensions = ["AVI","MP4","MKV"]
	for ext in eligibleExtensions:
		if filename.endswith(ext) or filename.endswith(ext.lower()):
			return True
	
	return False

sourcedir = '/home/pydomic/Desktop/TV'
targetFiles = [filename for filename in os.listdir(sourcedir) if isVideoFile(filename)] 
print(targetFiles)

#showdir = fileData["show"]
for f in targetFiles:
	fileData = extractFileData(os.path.basename(f))
	print(fileData)
	
	showdir = os.path.join( sourcedir, fileData["show"])
	#showdir = fileData["show"]
	if not (os.path.exists(showdir) and os.path.isdir(showdir) ) :
		os.mkdir(showdir)
	seasondir = os.path.join(showdir,"Season "+fileData["season"])
	if not (os.path.exists(seasondir) and os.path.isdir(seasondir) ) :
		os.mkdir(seasondir)
	
	#First we download the subtitles
	subtitleFile = extract_subtitle(get_subtitle_zip(fileData))
	print(subtitleFile)
	#Now we move them
	os.rename(os.path.join( sourcedir, fileData["filename"]),os.path.join(seasondir,os.path.basename(fileData["filename"])))
	targetSubtitleFile = os.path.basename(fileData['filename']).replace(fileData['extension'],'.srt')
	os.rename(subtitleFile, os.path.join(seasondir,targetSubtitleFile))