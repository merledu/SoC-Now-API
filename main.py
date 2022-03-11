from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import ast,json

app = Flask(__name__)
api = Api(app)

# ------------- / ------------- SoC Req -------------- / -------------

soc_req = reqparse.RequestParser()
soc_req.add_argument("coreISA",type=int)
soc_req.add_argument("coreExt",type=list)
soc_req.add_argument("devices",type=list)
soc_req.add_argument("bus",type=str)
soc_req.add_argument("Output",type=str)

socConfigs = {1 :  {"coreISA" : 32, "coreExt":["i","m"] ,"devices" : ["gpio", "spi"], "bus":"tl"}}
def notFound(soc_id):
    if soc_id not in socConfigs:
        abort(404, message="Record not found!")

class SoCs(Resource):
    def get(self, soc_id):
        notFound(soc_id)
        return socConfigs[soc_id]["Output"]

    def put(self,soc_id):
        newSoC = soc_req.parse_args()
        socConfigs[soc_id] = newSoC
        record= socConfigs[soc_id]
        outData = {}
        outData["i"] = [1 if "i" in record["coreExt"] else 0][0]
        outData["m"] = [1 if "m" in record["coreExt"] else 0][0]
        outData["f"] = [1 if "f" in record["coreExt"] else 0][0]
        outData["c"] = [1 if "c" in record["coreExt"] else 0][0]
        outData["gpio"] = [1 if "gpio" in record["devices"] else 0][0]
        outData["spi"] = [1 if "spi" in record["devices"] else 0][0]
        outData["uart"] = [1 if "uart" in record["devices"] else 0][0]
        outData["timer"] = [1 if "timer" in record["devices"] else 0][0]
        outData["spi_flash"] = [1 if "spi_flash" in record["devices"] else 0][0]
        outData["i2c"] = [1 if "i2c" in record["devices"] else 0][0]
        outData["wb"] = [1 if "wb" in record["bus"] else 0][0]
        outData["tl"] = [1 if "tl" in record["bus"] else 0][0]
        with open("SoC-Now-Generator/src/main/scala/config.json", "w") as outfile:
        # outfile.write(str(outData))
            json.dump(outData,outfile )
        # return redirect("finalize")


        # else:
        #     return "Work under construction."

    def delete(self, soc_id):
        del socConfigs[soc_id]
        return '', 204
#----