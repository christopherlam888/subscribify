# Subscribify

Check the latest videos of your favourite YouTube channels as if you were subscribed. 

![image](https://user-images.githubusercontent.com/85356197/213040018-78f9f702-02ec-46e0-aa7e-3bf0fe7400ca.png)

Get requests are to the Invidious REST API at instance [vid.puffyan.us](https://vid.puffyan.us/feed/popular).

Using pyfiglet, requests, multiprocessing, tqdm, webbrowser.

***

Guide:
- Add the channel IDs for your favourite YouTube channels in the ```channels.txt``` file.
- After reading the file and getting the videos, the program will display a table of videos.
- The program will enter browsing mode, in which you can enter a video # to open it in a new tab in your web browser.
- Exit browsing mode and the program by entering anything but a video #.

***

Features to implement:
- Sorting by upload date
- Specify number of videos or oldest video date for each channel

***

This project is licensed under the GNU General Public License v3.0.
