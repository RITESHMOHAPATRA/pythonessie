import urllib

def urlOpener():
    target = urllib.urlopen('https://raw.githubusercontent.com/nialaa/pythonessie/master/.gitignore', proxies = None)
    print target.read()

print "Starting..."
urlOpener()

