#!/ usr/bin/env python

# make sure to install these packages before running :
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

def data_extraction (departamento, municipio, cultivo, topografia, limite):
    # Unauthenticated client only works with public data sets . Note ’None ’
    # in place of application token , and no username or password :
    client = Socrata("www.datos.gov.co", None)

    # Example authenticated client ( needed for non - public datasets ):
    # client = Socrata (www. datos .gov.co ,
    # MyAppToken ,
    # username =" user@example . com" ,
    # password =" AFakePassword ")

    # First 2000 results , returned as JSON from API / converted to Python list of
    # dictionaries by sodapy .
    results = client.get("ch4u-f3i5", limit = limite, departamento = departamento, municipio= municipio, cultivo = cultivo, topografia = topografia)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    subset = results_df[['departamento', 'municipio', 'cultivo', 'topografia', 'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']]

    return subset