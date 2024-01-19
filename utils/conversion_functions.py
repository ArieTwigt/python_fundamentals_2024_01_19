import pandas


def convert_list_to_data_frame(input_list):
    # convert the list to a data frame
    data_df = pandas.DataFrame(input_list)
    
    return data_df