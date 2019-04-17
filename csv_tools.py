import csv

def import_csv(filename, titles=True):
    """Import data from csv file.
    
    params:
        filename: filepath/filename for csv file.

    args:
        titles (True/False): titles for columns in csv file.

    return:
            titles (tuple): row titles [empty if titles=False]
            data (tuple): list of columns in a list of rows

    """

    # Open the file as import_file
    with open(filename, 'r', encoding='utf-8-sig') as import_file:
        reader = csv.reader(import_file)
        titles = []
        data = []

        first = True
        # Loop for each line in file
        for num, row in enumerate(reader):
            # If file contains titles this will grab them.
            if first == True and titles == True:
                for item in row:
                    titles.append(item)
                first = False
            # This captures all rows except the first if titles=True.
            else:
                temp_col_list = []
                for item in row:
                    temp_col_list.append(item)
                data.append(temp_col_list)
        titles = tuple(titles)
        data = tuple(data)
         
    return titles, data
