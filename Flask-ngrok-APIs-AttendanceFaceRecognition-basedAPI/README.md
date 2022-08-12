# Attendance Face-Recognition-based

## Description
Simple API to record attendance of students in certain session of a class/course. You can create session to record or track attendance of registered students and save it in Google Dive to access it later or delete it when need.

## Setup
- First, in your **[Google Drive/My Drive](https://drive.google.com/drive/my-drive)** create a folder with "FaceRecognition-API-Files" as name.
- If you don't have flask-ngrok account read [Flask-ngrok setup](https://github.com/MahmoudHussienMohamed/Flask-APIs#flask-ngrok-setup).
- Replace "\<***YourAuthToken***\>" with your own in the *'AFR-API'* colab notebook.
- Run the notebook in GPU runtime (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-colab)* if not).
- Notebook will ask you to mount Google Drive. (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-drive)* if not)
Now your API is running!

## Some details
The API has 8 main routes to call and request which are:
- **'/register'** accepts `facial image, student id, student name and student email` to save the student data in the working memory.
- **'/check_if_exist'** accepts `facial image` to check if the person in the image saved in the working memory.
- **'/save_students'** store the students in the working memory to *'FaceRecognition-API-Files/all_students.pkl'* in your Google drive.
- **'/load_students'** retrive stored students from *'FaceRecognition-API-Files/all_students.pkl'* to working memory.
- **'/new_session'** accepts `course id, course name and session number` to create unique file in your drive to record and track attendance of given session of the course.
- **'/record_attendance'** accepts `facial image, course id, course name and session number` to record attendance of person whose the image in certain course for specific session.
- **'/get_attendance'** accepts `course id, course name and session number` and return students' data whic attend that session of that course as JSON response.
- Finaly, **'/delete_session'** accepts `course id, course name and session number` and delete the file of given session of the course from drive.  

## Test and run
You can test the API with [Test.py](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-AttendanceFaceRecognition-basedAPI/Test.py).
Update `url` variable with **2nd link** produced by **last cell** in the notebook then run it.
You should be able to see output like *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-AttendanceFaceRecognition-basedAPI/output.txt)*.


