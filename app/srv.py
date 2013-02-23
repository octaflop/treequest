from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello index!"
    ret = {}
    return render_template("index.html", page=ret)

# Based on
# http://mycity.sensetecnic.com/demo/rest/StreetTrees/tree_locations?limit=10&maxLat=49.269569871597284&minLat=49.26783728704706&maxLon=-123.09416667541961&minLon=-123.0998368652771
loc_algo = '/tree/by_loc/<float:minLat>/<float:minLon>/<float:maxLat>/<float:maxLon>'
@app.route(loc_algo)
def apiref(minLat, minLon, maxLat, maxLon):
    req_url = "http://mycity.sensetecnic.com/demo/rest/StreetTrees/tree_locations?limit=10&maxLat=%(maxLat)s&minLat=49.26783728704706&maxLon=-123.09416667541961&minLon=-123.0998368652771"
    return "%s, %s, %s, %s" % (minLat, minLon, maxLat, maxLon)


if __name__ == "__main__":
    app.debug = True
    app.run()
