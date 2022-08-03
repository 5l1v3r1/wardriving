# wardriving

Python Wardriving Tool

I cannot be held responsible for the malicious use of the vehicle.

ssidBul.py has been tested via TP-LINK TL WN722N.

Selenium 3.11.0 and Firefox 59.0.2 are used for location.py. Firefox geckodriver is located in the directory where the codes are.

SSID and MAC names and location information were created and changed in the test environment.

ssidBul.py and location.py must be run concurrently.

ssidBul.py result:

20 March 2018 11:48PM|9c:b2:b2:11:12:13|ECFJ3M

20 March 2018 11:48PM|c0:25:e9:11:12:13|T7068

Here is a screenshot of allowing location information while running location.py:

<img src="https://github.com/anil-yelken/wardriving/blob/main/geody1.JPG">

The screenshot of the location information is as follows:

<img src="https://github.com/anil-yelken/wardriving/blob/main/geody2.JPG">

konum.py result:

lat=38.8333635|lon=34.759741899|20 March 2018 11:47PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:49PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:49PM

After the data collection processes, the following output is obtained as a result of running wardriving.py:

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM|9c:b2:b2:11:12:13|ECFJ3M

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM|c0:25:e9:11:12:13|T7068
