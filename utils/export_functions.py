import os


def export_data(df, brand):

    # check the current files inn the directory
    files_folders = os.listdir()

    # check if the 'data' folder already exists
    if 'data' not in files_folders:
        print("Data folder does not exist yet, creating...")
        os.mkdir('data')

    # check if the selected brand is in the folder
    if not os.path.exists(f"data/{brand}"):
        print(f"Folder for {brand} does not exists yet. Creating...")
        os.mkdir(f"data/{brand}")

    # compose the file path
    file_path = f"data/{brand}/export_{brand}.csv"

    # export to csv
    df.to_csv(file_path)
    