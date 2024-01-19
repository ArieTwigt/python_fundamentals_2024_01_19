from utils.import_functions import retreive_brand, retreive_plate
from utils.conversion_functions import convert_list_to_data_frame
from utils.export_functions import export_data

from tqdm import tqdm
import sys


# indicate what to import
import_type = input("What do you want to import? (plate/brand):\n")

if import_type == "brand":

    # specify the brand
    selected = input("Insert car brand:\n")

    # create a list from the input
    selected_list = selected.split(" ")

    # iterate over the list
    for brand in tqdm(selected_list):

        # get the cars from the API
        cars_list = retreive_brand(brand)

        # convert the cars_list to the data frames
        cars_df = convert_list_to_data_frame(cars_list)

        # export the brand
        export_data(cars_df, brand)


elif import_type == "plate":
    
    # specify the plate
    selected = input("Insert car plate:\n")

    # get the car from the API
    cars_list = retreive_plate(selected)

    # convert the cars_list to the data frames
    cars_df = convert_list_to_data_frame(cars_list)

        # export the brand
    export_data(cars_df, selected)
else:
    print(f"❌ Please select 'plate' or 'brand'. {import_type} is not possible.")
    sys.exit()

