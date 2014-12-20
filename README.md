Installation
======

How to add the SauceLabs credentials
======
You can add system variables on OS X like so: 

1. Open terminal 
2. type the below: 
vi ~/.bash_profile
3. type the letter 'i' to enter vim's insert mode 
4. type the below into the file: 
 * export SAUCE_USERNAME=yourusername
 * export SAUCE_ACCESS_KEY=youraccesskey
5. type ':wq!' to close and save the file 
6. type into terminal: 
source ~/.bash_profile

You can then do the code from the tutorial like so: 
```
import os

sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub";
self.driver = webdriver.Remote(
    desired_capabilities=self.desired_capabilities,
    command_executor=sauce_url % (os.get('SAUCE_USERNAME'), os.get('SAUCE_ACCESSKEY'))
)
```

Author
======
Moises Siles
