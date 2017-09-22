# In this example we are going to create an application which will prevent
# us to access to some disrupting websites, during our work time.

# In this exercise we are going to use:
# - File manipulation
# - Date and time
# - Python process in background

# Each operating system has a so called "host file".
# Inside the host file, it is possible to enstablish that when we type a certain
# website on the web browser, we redirect the request to a different IP address.
# So, we can associate www.facebook.com with 127.0.0.1, that is the IP address
# of the current device we are using. This will block the access to facebook.
# On Windows, the host file is located in "C:/Windows/System32/Drivers/etc/hosts"
# On Mac and Linux it's located in "etc/hosts"

# Before running this script, it is recommended to make a backup copy of the hosts file

import time
from datetime import datetime as dt

# What we are going to do practically is:
# - Add the lines containing the sites we want to avoid reaching in the host file
#   during the work time
# - Remove the lines mentioned above when the work time ends.

# We save the location of the host file in a variable

host_path = "C:\Windows\System32\Drivers\etc\hosts"

# It is a better practice to create the string like this:

host_temp = r"C:\Windows\System32\Drivers\etc\hosts"

# The r prefix indicates we are passing a ROW STRING, which will completely
# ignore all Python escape codes. For example, Python has \n as escape code,
# so if we have in Windows (Not in Linux and Mac, which use forward slashes "/")
# a folder or file starting with "n", Python would interpret \n as a breakline
# and the file would not be reachable.

# Another solution is passing double backslashes:

host_path = "C:\\Windows\\System32\\Drivers\\etc\\hosts"

host_temp = "C:\\Users\\Francesco Vergona\\Desktop\\hosts"
# We use this just to get used to file manipulation, without editing the original one.

# We save the redirect IP (When we browse to a disrupting website we get redirected here):

redirect = "127.0.0.1"

# We save in a list the sites we want to block:

website_list = ["www.facebook.com", "facebook.com"]

# Now we have to open the hosts file in Python

# We want our application to be always running in the background, and making always
# the same checks (Date and time). So, we need an infinite loop!

while True:
    if  dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        # We don't want to check the time each millisecond or less, depending on the CPU.
        # We want to be more memory efficient, so we introduce a little margin of wait
        # by setting the application to sleep for 5 seconds.
        time.sleep(5)

        # We have to access to hosts file. It can only be accessed by administrator
        # in windows. To do that, the terminal needs to be run as administrator.
        print ("Working hours")

        # In this case we want to make sure the facebook URLs are present in the
        # host file. We first need to read the file. We choose r+ to read and append

        with open(host_path,'r+') as file:
            content = file.read()   # Content will contain the entire content of the file
            for website in website_list:
                if website in content:  # If the website we want to block is already present
                    pass                # We don't have to do anything
                else:
                    file.write(redirect+" "+website+"\n") #If not present, we add it

    # Now we have to add the behaviour referred to the case of fun hours.
    # We want the program to remove the website from the list, in order to let
    # us access it freely.

    else:
        time.sleep(5)
        with open(host_path, 'r+') as file:
            content = file.readlines()  # This will create a list of lines
            file.seek(0)                 # We point at the beginning of the file, so we can delete the previous content after
            for line in content:        # For each line of the hosts file
                if not any(website in line for website in website_list): # If there is no website to be blocked in this line
                    file.write(line)    # We keep the line
       # If the line contains the website (it means the site is already blocked) we do nothing
            file.truncate()             # Truncating the rest of the file will delete the previous version of hosts

        print ("Free time!")

# The script now works fine. The last thing we need to do is to make it an executable
# file in order to let it run in the background without using the command line.

# To do that, we need to use a specific version of the Python cmd: pythonw.exe
# and make our .py file a '.pyw' one.

# Now, the pyw file can be run, but if you try to execute it like this it won't.
# That's because the pythonw.exe should be run as administrator in order to allow
# the script to access and modify the host file.
# You can try to use this script by changing the path of the host file in host_temp

# The best thing to do is to use the task scheduler in order to let the program run
# at the startup of the computer. Don't forget to check the box allowing the program to
# run in privileged mode.
