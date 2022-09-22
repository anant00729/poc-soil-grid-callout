import requests as re
import argparse
import cmd
import utils

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

		print("*** Set Location ***")
		lat = utils.validate_latitude()
		lon = utils.validate_longitude()

		depths = ["0-5cm", "60-100cm", "100-200cm"]
		depth_q = ""

		for d in depths:
			depth_q += f"&depth={d}"

		print(depth_q)

		api_url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={lon}&lat={lat}&property=bdod&property=clay&property=sand&property=silt{depth_q}&value=Q0.5&value=Q0.05&value=Q0.95&value=mean&value=uncertainty"
		response = re.get(api_url, headers)
		response_data = response.json()

		# print(response_data)
		if "properties" in response_data:
			pickup_properties = ["bdod", "sand", "silt", "clay"]
			for i in response_data["properties"]["layers"]:
				for j in pickup_properties:
					if i["name"] == j:
						print("\n")
						print(i["name"])
						for k in i["depths"]:
							for l in depths:
								if k["label"] == l:
                  
									print(f"""mean value for depth : {l} is {k["values"]["mean"]}""")

		else:
			for d in response_data["detail"]:
				if d["loc"][1] == "lat":
					print("\n")
					print("API error: ")
					print("Invalid latitude entered. Please enter a number within -90 , +90 and within 10 decimal places")
					print("\n")
				elif d["loc"][1] == "lon":
					print("\n")
					print("API error: ")
					print("Invalid longitude entered. Please enter a number within -180 , +180 and within 10 decimal places")
					print("\n")
			self.do_get_soil_grid({})


if __name__ == "__main__":
	args = parse_args()
	SoilGrid(args).cmdloop()