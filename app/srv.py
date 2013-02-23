from flask import Flask, render_template
import urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello index!"
    ret = {}
    return render_template("index.html", page=ret)

# Based on
# http://mycity.sensetecnic.com/demo/rest/StreetTrees/tree_locations?limit=10&maxLat=49.269569871597284&minLat=49.26783728704706&maxLon=-123.09416667541961&minLon=-123.0998368652771
loc_algo = '/tree/by_loc/<minLat>/<minLon>/<maxLat>/<maxLon>'
@app.route(loc_algo)
def apiref(minLat, minLon, maxLat, maxLon):
    req_url = \
        "http://mycity.sensetecnic.com/demo/rest/StreetTrees/tree_locations?limit=10&maxLat=%(maxLat)s&minLat=%(minLat)s&maxLon=%(maxLon)s&minLon=%(minLon)s"
    spider = urllib2.build_opener()
    spider.addheaders = [('User-agent', 'Mozilla/5.0')]
    url = req_url % {
                "maxLat": maxLat,
                "maxLon": maxLon,
                "minLat": minLat,
                "minLon": minLon
            }
    print "Using url: %s" % url
    ret = spider.open(url).read()
    return ret
    #return "%s, %s, %s, %s" % (minLat, minLon, maxLat, maxLon)


if __name__ == "__main__":
    app.debug = True
    app.run()
