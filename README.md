# Subscribify

<p align="left">
<img src="https://img.shields.io/github/languages/top/christopherlam888/subscribify.svg" >
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.gnu.org/licenses/gpl-3.0" alt="License: GPLv3"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"></a>
</p>

Check the latest videos of your favourite YouTube channels as if you were subscribed. 

## Features

- Get requests are to the Invidious REST API at the instance [y.com.sb](https://y.com.sb/feed/popular)
- Faster requests with multitprocessing
- After getting the videos, the program will display a table of videos from newest to oldest
- The program will enter browsing mode, in which you can enter a video # to open it in a new tab in-browser
- Exit browsing mode and the program by entering anything but a video #

## Installation

Clone/Download the GitHub repository:

```git clone https://github.com/christopherlam888/subscribify.git```

Navigate to the directory:

```cd subscribify```

Install requirements:

```pip3 install -r requirements.txt```

Add the channel IDs for your favourite YouTube channels in the `channels.txt` file.

## Usage

| **Command**                                   | **Description**                                                |
| :-------------------------------------------- | :------------------------------------------------------------- |
| `python3  chrono_crawler.py`                  | Run Subscribify with default number of videos (1)              |
| `python3  chrono_crawler.py -n [#]`           | Specific a number of videos per channel                        |
| `python3  chrono_crawler.py -h`               | Show help message.                                             |

## Screenshots

![image](https://user-images.githubusercontent.com/85356197/213220795-745c2404-79a3-4884-a495-2e3cc5fa7456.png)

## Features To Implement

- Specify oldest video date to get videos

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)  

This project is licensed under the GNU General Public License v3.0.
