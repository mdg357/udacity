#!/c/Users/User/Anaconda2/python

import pandas
import pandasql

def select_first_50(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    
    data_types = {
        'Registrar': str,
        'Enrolment Agency': str,
        'State': str,
        'District': str,
        'Sub District': str,
        'Pin Code': str,
        'Gender': str,
        'Age': int,
        'Aadhaar generated': int,
        'Enrolment Rejected': int,
        'Residents providing email': int,
        'Residents providing mobile number': int
    }
    
    aadhaar_data = pandas.read_csv(filename, dtype=data_types)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax. 
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    #
    # You can download a copy of the aadhaar data that we are passing 
    # into this exercise below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
    q = "SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50"

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == "__main__":
    database_path = './aadhaar_data/UIDAI-ENR-DETAIL-20160305.csv'
    solution = select_first_50(database_path)
    
    print solution