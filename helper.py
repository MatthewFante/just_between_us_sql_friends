from time import sleep
from IPython.display import clear_output, Image
import sys

def five_dots(sec):
    elipsis = '.....'
    for dot in elipsis:
        sleep(sec/len(elipsis))
        print(dot, end = '')
        
def check_dependencies(dependency_list):
    ready = 0
    for library in dependency_list:
        clear_output()
        print('Checking ' + library, end = '')
        five_dots(.5)
        clear_output()
        
        if library in sys.modules:
            ready += 1
        elif library not in sys.modules:
            pass
    if ready == len(dependency_list):
        print("All dependencies are ready... Enjoy!")
    else: 
        print("Some dependencies are missing... Please run the INSTALL/UPDATE DEPENDENCIES cell at the bottom of this notebook before proceeding!")

        
def csv_export(df, file_name):
    df.to_csv(file_name, index=True)
    
    
# def xls_export(df, file_name, sheet_name):
#     df.to_excel(file_name, sheet_name=sheet_name)
    
        
# This could come in handy for a nice clean excel export once everything is said and done.
# df2 = df1.copy()
# with pd.ExcelWriter('output.xlsx') as writer:  
# df1.to_excel(writer, sheet_name='Sheet_name_1')
# df2.to_excel(writer, sheet_name='Sheet_name_2')

# df.to_excel("output.xlsx", sheet_name='Sheet_name_1')  

 

# def xls_export(list_of_dfs, file_name):
#     with pd.ExcelWriter(file_name) as writer:  
#         i = 0
#         for dataframe in list_of_dfs:
#             dataframe.to_excel(writer, sheet_name="sheet")
#             i +=1
# list_of_dfs = [main_seasons_df, all_stars_df]

# xls_export(list_of_dfs, 'output.xlsx')