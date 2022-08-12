# Virtual Fitting Room

## Description
[CV](https://www.ibm.com/eg-en/topics/computer-vision) API based on [ACGPN](https://github.com/levindabhi/ACGPN) which accepts takes two images of person and clothing and produce an image of the person wearing tha clothing. Model is not accurate so much but good enough with acceptable perfomance.

## Setup
- First, in your **[Google Drive/My Drive](https://drive.google.com/drive/my-drive)** create a folder with "ACGPN-API-Files" as name.
- Notebook will ask you to mount Google Drive. (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-drive)* if not)
- Run *[Prep](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-VirtualFittingRoomAPI/Prep.ipynb)* notebook it will download all data and files for the model to run (You won't need to run this notebook more than once -same as flask-ngrok sign up and Authtoken config-).
- If you don't have flask-ngrok account read [Flask-ngrok setup](https://github.com/MahmoudHussienMohamed/Flask-APIs#flask-ngrok-setup).
- Replace "\<***YourAuthToken***\>" with your own in the *'VFR-API'* colab notebook.
- Run the notebook in GPU runtime (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-colab)* if not).
Now your API is running!

## Requests
The API has 2 main routeس which are:
- **'/apply'** accepts `person image` and `clothing image` and return an image of the person wearing the given clothing.
- **'/clean'** deletes all remporary files when called.


## Test and run
You can test the API with [Test.py](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-VirtualFittingRoomAPI/Test.py).
Update `url` variable with **2nd link** produced by **last cell** in the notebook then run it.
For example, if we request '/apply' with two images: 
![](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-VirtualFittingRoomAPI/Input/person.jpg) ![](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-VirtualFittingRoomAPI/Input/cloth.jpg)
the output will be:
![](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-VirtualFittingRoomAPI/Output/person%20%2B%20cloth.png)



