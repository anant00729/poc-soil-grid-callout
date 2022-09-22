import requests as re
import argparse
import cmd

soil_grid_url = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=-123.24603671591137&lat=49.261221362605255&property=bdod&property=cec&property=cfvo&property=clay&property=nitrogen&property=ocd&property=ocs&property=phh2o&property=sand&property=silt&property=soc&depth=0-5cm&value=Q0.5&value=Q0.05&value=Q0.95&value=mean&value=uncertainty"

def parse_args():
    argp = argparse.ArgumentParser(
        'mcli',
        description='Command-line query interface to soil grid api'
        )
    return argp.parse_args()

class SoilGrid(cmd.Cmd):
    def __init__(self, args):
        cmd.Cmd.__init__(self)
        self.prompt = 'poc: '
        self.intro = "Command-line query interface of soil grid api"

    def do_get_soil_grid(self, args):
        headers = {"Content-Type": "application/json"}
        response = re.get(f"{soil_grid_url}", headers)
        response_data = response.json()
        pickup_properties = ["bdod", "sand", "silt", "clay"]
        for i in response_data["properties"]["layers"]:
            for j in pickup_properties:
                if i["name"] == j:
                    print("\n")
                    print(i["name"])
                    print(i["unit_measure"])

if __name__ == "__main__":
    args = parse_args()
    SoilGrid(args).cmdloop()