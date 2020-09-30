[![Total alerts](https://img.shields.io/lgtm/alerts/g/samchu11/Selenium-Instagram-Auto-Liker.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/samchu11/Selenium-Instagram-Auto-Liker/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/samchu11/Selenium-Instagram-Auto-Liker.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/samchu11/Selenium-Instagram-Auto-Liker/context:python)

# Selenium-Instagram-Auto-Liker

This project used to like all posts on Instagram with specific user.

The code is hosted at https://github.com/samchu11/Selenium-Instagram-Auto-Liker

## Installing

### To install please run the command below:

    $ git clone git@github.com:samchu11/Selenium-Instagram-Auto-Liker.git
    $ cd Selenium-Instagram-Auto-Liker

### To install Selenium libraries please run the command:

    $ pip install selenium

### To install Chrome Driver:

Select Chrome Driver with same version of your Chrome browser from here - http://chromedriver.chromium.org/downloads

## before runing the code

Please replace `{your_instagram_ID}` with your instagram ID

Please replace `{your_instagram_password}` with your instagram Password

Please replace `{target_instagram_ID}` with the target instagram ID

## Running the code

Navigate to the folder, run the command below:
\$ python Instagram_auto_liker.py

## bug/issue found

#1. if post already been liked, will like the first comment

#2. if post already beem liked and no comment, program exit with error

#3. Not support 2FA enabled account

#4. default language is set to 'en', which will affect the "Like" button content `[@aria-label="Like"]`

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/samchu11/Selenium-Instagram-Auto-Liker/blob/master/LICENSE) file for details
