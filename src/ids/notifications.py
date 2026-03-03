import os
import sys

# Notification script for MacOS
def notification(title:str, message:str): 
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)
