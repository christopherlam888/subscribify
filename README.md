# Subscribify

Check the latest videos of your favourite YouTube channels as if you were subscribed. 

![image](https://user-images.githubusercontent.com/85356197/213220795-745c2404-79a3-4884-a495-2e3cc5fa7456.png)

Get requests are to the Invidious REST API at the instance [y.com.sb](https://y.com.sb/feed/popular).

Using argparse pyfiglet, requests, multiprocessing, tqdm, webbrowser.

***

Guide:
- Add the channel IDs for your favourite YouTube channels in the ```channels.txt``` file.
- After reading the file and getting the videos, the program will display a table of videos from newest to oldest.
- The program will enter browsing mode, in which you can enter a video # to open it in a new tab in your web browser.
- Exit browsing mode and the program by entering anything but a video #.

***
Usage:
To specify a number of videos to get per channel like 5, use the following command:

```python3 subscribify.py -n 5```

You can also use the following command to see the help message of the script:

```python3 subscribify.py -h```

***

Features to implement:
- Specify oldest video date to get videos

***

This project is licensed under the GNU General Public License v3.0.
