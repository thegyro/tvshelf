import re

#an ugly ,brittle regex
def extractFileData(filename):
	print filename
	matches = re.match(r'(.*)S([0-9]{1,2})E([0-9]{1,2})(.*)\.(.{2,3})', filename)
	print matches
	
	if matches.lastindex==5:
		obj = {}
		obj['filename'] = matches.group(0)
		obj['show'] =  matches.group(1).replace('.',' ').strip()
		obj['season'] = matches.group(2)
		obj['episode'] = matches.group(3)
		obj['excess'] = matches.group(4) 
		obj['extension'] = matches.group(5)
		res_matches = re.match(r'.*([0-9]{3,4}p).*', obj['excess'])
		obj['res'] = res_matches.group(1) if res_matches.__class__.__name__ == 'SRE_Match' else ''

		enc_matches = re.match(r'.*(XviD|x264).*',obj['excess']) 
		obj['encoding'] = enc_matches.group(1) if enc_matches.__class__.__name__ == 'SRE_Match' else ''
		
		obj['showid'] = 'S'+obj['season']+'E'+obj['episode']
		return obj
	else:
		print("could not regex the filename")
		exit(1)