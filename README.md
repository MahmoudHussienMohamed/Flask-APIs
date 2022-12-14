# Flask-APIs

Simple AI\ML *Flask* APIs with *flask-ngrok* running on **Google colab** and storing some files in **Google Drive**.

There're 3 naive APIs which are:

  - [Attendance recording](https://github.com/MahmoudHussienMohamed/Flask-APIs/tree/main/Flask-ngrok-APIs-AttendanceFaceRecognition-basedAPI) using Face-ID:
    - Given the facial image of an student you can record his attendance for one or more classes/sessions.
  - [Virtual Fitting Room](https://github.com/MahmoudHussienMohamed/Flask-APIs/tree/main/Flask-ngrok-APIs-VirtualFittingRoomAPI):
    - Do you want to experiment your appearance wearing a shirt but you have just its photo? 
        *Here you are!* 
  - [Arabic Disease Classifier](https://github.com/MahmoudHussienMohamed/Flask-APIs/tree/main/Flask-ngrok-APIs-Arabic-Disease-Classifier-API):
    - by using a simple arabic dataset which provide symptoms and its corresponding disease you can predict pathological case.
   
## Google Colab:
You should run the notebooks with **GPU** In Colab from "Runtime/Change runtime type" and choose GPU from "Hardware accelerator".

   
## Flask-ngrok setup
  - First, sign up from *[Here](https://dashboard.ngrok.com/signup)*.
  - Then, go to [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) and copy your own one.
  - Replace "\<***YourAuthToken***\>" with your own in any colab notebook you want to run.
  - Now, you're ready to use the APIs!

## Google Drive
All APIs require *mounting* **Google Drive** to store specific files. So, **colab** will ask you about allowing notebook which the API runs on to have access to your **Google Drive**; you should click allow and complete the process.  
