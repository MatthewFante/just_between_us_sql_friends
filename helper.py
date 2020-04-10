from time import sleep
from IPython.display import clear_output, Image
import sys

def five_dots(sec):
    elipsis = '.....'
    for dot in elipsis:
        sleep(.2)
        print(dot, end = '')

def check_dependency_prompt(dependency_list):
    yn = ''
    
#     print("Greetings! I can help you install or update the dependencies for this notebook!")
    
    while yn.lower() not in ['yes', 'no']:
        clear_output()
        yn = input("Do you want to check dependencies for updates? ")
    
    if yn.lower() == 'yes':
        clear_output()
        print("Great! Let's get started", end='')
        five_dots(1)
        check_dependencies(dependency_list)
        
    elif yn.lower() == 'no':
        clear_output()
        print("Okay! I won't check dependencies right now.")
        
    yn = ''
        
        
def check_dependencies(list_of_dependencies):
    dependency_summary = []
    ready = 0
    for library in list_of_dependencies:
        clear_output()
        print('Checking ' + library, end = '')
        five_dots(1)
        clear_output()
        
        if library in sys.modules:
            dependency_summary.append(library + " is ready to use")
            ready += 1
        elif library not in sys.modules:
            dependency_summary.append(library + " is NOT ready to use")
    for item in dependency_summary:
        print(item)
    if ready == len(list_of_dependencies):
        print("\nAll dependencies are ready... Enjoy!")
    else: 
        print("\nSome dependencies are missing... please run the INSTALL/UPDATE DEPENDENCIES cell at the bottom of this notebook before proceeding!")
    
    
    
# This could come in handy for a nice clean excel export once everything is said and done.
# df2 = df1.copy()
# with pd.ExcelWriter('output.xlsx') as writer:  
# df1.to_excel(writer, sheet_name='Sheet_name_1')
# df2.to_excel(writer, sheet_name='Sheet_name_2')

# df.to_excel("output.xlsx", sheet_name='Sheet_name_1')  



        
def csv_export(df, file_name):
    df.to_csv(file_name, index=True)
    
    
def xls_export(df, file_name, sheet_name):
    df.to_excel(file_name, sheet_name=sheet_name)