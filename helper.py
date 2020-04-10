from time import sleep
from IPython.display import clear_output, Image
import sys

def loading_dots(time):
    elipsis = '.....'
    for dot in elipsis:
        sleep(time/len(elipsis))
        print(dot, end = '')
    clear_output()
        
def check_dependencies(dependency_list):
    ready = 0
    missing = []
    
    for library in dependency_list:
        print('Checking ' + library, end = '')
        loading_dots(.5)

        if library in sys.modules:
            ready += 1    
        else:
            missing.append(library)

    if ready == len(dependency_list):
        print("All dependencies are fulfilled... Enjoy!")
    else: 
        print("The following libraries are missing:")
        for library in missing:
            print('- ', library)
        print("\nBefore proceeding, please run the necessary INSTALL/UPDATE DEPENDENCIES cells\n\tat the bottom of this notebook.")
       
    
    
    
    
    
    
    
    
        
# def csv_export(df, file_name):
#     df.to_csv(file_name, index=True)
    
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