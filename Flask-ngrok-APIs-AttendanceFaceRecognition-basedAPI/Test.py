import requests
url = 'http://d43c-34-66-105-114.ngrok.io'
path = 'imgs\\'

# Register:

img = {'image': open(path + 'mahmoud.png', 'rb')}
data = {
    'student_id' : 12345,
    'student_name' : "Mahmoud Husasien Mohamed",
    'student_email' : "mahmoudhussienmohamed.mhm@gmail.com",
}
r = requests.post(url + '/register', files = img, data=data)
print(r.text)

img = {'image': open(path + 'Albert-Einstein.jpg', 'rb')}
data = {
    'student_id' : 12346,
    'student_name' : "Albert Einstein",
    'student_email' : "Albert_Einstein@gmail.com",
}
r = requests.post(url + '/register', files = img, data=data)
print(r.text)

img = {'image': open(path + 'Alan-Turing.jpg', 'rb')}
data = {
    'student_id' : 12347,
    'student_name' : "Alan Turing",
    'student_email' : "Alan_Turing@gmail.com",
}
r = requests.post(url + '/register', files = img, data=data)
print(r.text)

##############################################################################################################

# Check if exist:
img = {'image': open(path + 'mahmoud.png', 'rb')}
r = requests.get(url + '/check_if_exist', files = img)
print(r.text)

img = {'image': open(path + 'GeorgeClooney.png', 'rb')}
r = requests.get(url + '/check_if_exist', files = img)
print(r.text)

##############################################################################################################

# Save Students:
r = requests.post(url + '/save_students')
print(r.text)

##############################################################################################################

# Load Students:
r = requests.get(url + '/load_students')
print(r.text)

##############################################################################################################

# Create Session:
data = {
    "course_id" : 123,
    "course_name" : "AI",
    "session_no" : 3,
}
r = requests.post(url + '/new_session', data = data)
print(r.text)

data = {
    "course_id" : 101,
    "course_name" : "ML",
    "session_no" : 7,
}
r = requests.post(url + '/new_session', data = data)
print(r.text)

##############################################################################################################

# Record Attendance:
img = {'image': open(path + 'mahmoud.png', 'rb')}
data = {
    "course_id" : 123,
    "course_name" : "AI",
    "session_no" : 3,
}
r = requests.post(url + '/record_attendance', files = img, data = data)
print(r.text)

img = {'image': open(path + 'Albert-Einstein2.jpg', 'rb')}
r = requests.post(url + '/record_attendance', files = img, data = data)
print(r.text)

##############################################################################################################

# Get Attendance:
data = {
    "course_id" : 123,
    "course_name" : "AI",
    "session_no" : 3,
}
r = requests.get(url + '/get_attendance', data = data)
print(r.text)

data = {
    "course_id" : 321,
    "course_name" : "DL",
    "session_no" : 5,
}
r = requests.get(url + '/get_attendance', data = data)
print(r.text)

##############################################################################################################

# Delete session:
data = {
    "course_id" : 123,
    "course_name" : "AI",
    "session_no" : 3,
}
r = requests.post(url + '/delete_session', files = img, data = data)
print(r.text)

data = {
    "course_id" : 321,
    "course_name" : "DL",
    "session_no" : 5,
}
r = requests.post(url + '/delete_session', files = img, data = data)
print(r.text)
