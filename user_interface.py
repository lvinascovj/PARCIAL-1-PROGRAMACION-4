from tabulate import tabulate
from init import data_extraction

def show_data(departamento, municipio, cultivo, topografía, limite):
    
    # Obtener los datos filtrados
    filtered_data = data_extraction(departamento, municipio, cultivo, topografía, limite)
    
    if filtered_data is None or filtered_data.empty:
        print("No se encontraron resultados que coincidan con los criterios.")
        return
    
    # Formatear el subconjunto como una tabla en formato GitHub Markdown
    table_headers = ['departamento', 'municipio', 'cultivo', 'topografía', 'ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    formatted_table = tabulate(filtered_data, headers=table_headers, tablefmt='github')
    
    print(formatted_table)
