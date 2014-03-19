tvshelf
=======

An app to organize your TV show directory by placing files in appropriate folders and crawling the web to get the best possible subtitle for a given TV show

TO-DO
=======
1. Implement a daemon and callback which tracks the directory in which TV Shows are being added so that whenever a new TV Show is added ,the code automatically gets executed.

2. The code as of now is very brittle ,more like a hack. Should implement it in a better way - write more exception catchers,design the inputs in a more Object Oriented way.

3. Should cover a more formats in which a TV show can be named. (The regex we have written now is a bit dirty ,we have to clean that up.)
