from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", page=ret)

# Based on
# http://mycity.sensetecnic.com/demo/rest/StreetTrees/tree_locations?limit=10&maxLat=49.269569871597284&minLat=49.26783728704706&maxLon=-123.09416667541961&minLon=-123.0998368652771
loc_algo = '/tree/by_loc?minLat=<minLat>&minLon=<minLon>&maxLat=<maxLat>&maxLon=<maxLon>'
@app.route(loc_algo)
def apiref(minLat, minLon, maxLat, maxLon):
    return "%s, %s, %s, %s"
