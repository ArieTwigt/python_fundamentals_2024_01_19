import requests
import sys

def retreive_brand(brand):
    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand.upper()}"

    # send the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # check if the data is not empty
    if len(data) == 0:
        print(f"No cars found for {brand}")
        # shutdown the script
        sys.exit()

    return data


def retreive_plate(plate):
    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate.upper()}"

    # send the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # check if the data is not empty
    if len(data) == 0:
        print(f"No cars found for {plate}")
        # shutdown the script
        sys.exit()

    return data


# Other: Method that will handle both (main.py should be changed)
def import_from_rdw(selected, import_type):
    endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?$limit=50000"
    
    if import_type == "plate":
        endpoint = endpoint + f"?kenteken={selected}"
    
    elif import_type == "brand":
        endpoint = endpoint + f"?merk={selected}"
    else:
        print("no")
    
    # send the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # check if the data is not empty
    if len(data) == 0:
        print(f"No cars found for {selected}")
        # shutdown the script
        sys.exit()

    return data
        