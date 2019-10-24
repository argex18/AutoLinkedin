# This is a script for a really basic automation of Linkedin which is going to permit you to automatically post or share contents on the social media.

REQUISITES TO MAKE THE SCRIPT WORK:

1 - Selenium library installed in your Python packages. For installing it, use on the            command line:
        -- pip install selenium

2 - Pyautogui library installed in your Python packages. For installing it, use on the           command line:
        -- pip install pyautogui

3 - Selenium Chrome Driver installed. For installing it, it will be sufficient download and then extract it in any directory. Link to download it: https://sites.google.com/a/chromium.org/chromedriver/

4 - A file for containing the access data for your account. You can use the password file you would normally use for anything else, but you must respect the following format:

    // format starts here
#    **
#    SERVICE: name_of_the_service        // MANDATORY
#    password: password_of_the_service   // MANDATORY
#    email: email_of_the_service         // MANDATORY
#    nome: name_of_your_user             // optional
#    cognome: surname_of_your_user       // optional
#    ... : ...                           // ...
#    **
    // format finishes here

Obviously, in this case, in your password file will have to be present the Linkedin service
at least.

# WARNING: THE FILE FORMAT MUST BE ABSOLUTELY RESPECTED WITHOUT APPORTING ANY KIND OF        #          MODIFICATION. THIS INCLUDES ASTERISKS, WHITE SPACES, COLONS.
#          THE ABSENCE OF THE MANDATORY FIELDS WILL ALSO CAUSE AN ERROR. 

5 - The AutoLogin package must be copied and pasted in the site-packages folder of your 
    Python installation directory. This package will contain the module which AutoLinkedin will use to extract the data from your           password file.

# WARNING: THIS LAST PASSAGE IS REQUIRED FOR THE CORRECT EXECUTION OF THE SCRIPT.
#          DON'T FORGET IT !!

HOW TO USE THE SCRIPT:

1 - Insert in the posts folder, the only textual post you want to pubblish. 
#    The posts must be only of the .txt format. Other extensions will be ignored

2 - Insert in the shares folder, the images, the videos or the documents you want to             pubblish. You can add a description or an alternative text to them by inserting it in        the alts and descriptions folders. 
#   The description or the alternative text must have the same name of the share you want to #   add them to.
#   The only acceptable format is the .txt one. Other extensions will be ignored.

3 - Start the script by double clicking on auto_linkedin.py or by using via console:
#   cd _the_directory_which_you_downloaded_the_script_in
#   python auto_linkedin.py
