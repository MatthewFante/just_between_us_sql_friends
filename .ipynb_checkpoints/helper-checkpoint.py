from time import sleep
import sys


def check_dependencies(dependencies):
    yn = ''
    print("Greetings! I can help you install or update the dependencies for this notebook!")

    while yn.lower() not in ['yes', 'no']:
        clear_output()
        yn = input("Do you want to check dependencies for updates? ")


    if yn.lower() == 'yes':
        print("Great! Let's get started!")
        for package in dependencies:
            delayed_install(package)


    elif yn.lower() == 'no':
        clear_output()
        print("Okay, trying to import dependencies", end='')
        dot_dot_dot()
            
            
def delayed_install(package):
    sleep(1)
    clear_output()
    print("Checking" + package)
    !conda install --yes --prefix {sys.prefix} package
    

def get_image_urls(data_set):
    images = []
    for i in range(len(data_set['image_url'])):
        images.append(Image(url = data_set['image_url'][i], width = 50))
        i += 1
    return images


def display_images(images):
    for image in images:
        display(image)
        
        
def csv_export(df, file_name):
    df.to_csv(file_name, index=True)
    
    
def xls_export(df, file_name, sheet_name):
    df.to_excel(file_name, sheet_name=sheet_name)
    
def dot_dot_dot(time):
    elipsis = '.....'
    for period in elipsis:
        sleep(time / len(elipsis))
        print(period, end='')
    