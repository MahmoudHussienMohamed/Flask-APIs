import requests
url = 'http://0e08-35-229-90-175.ngrok.io'
data = {
    'sympots' : 'انا بقالي كذا يوم مش بدخل الحمام وده بسبب اني عندي احتباس في السوائل وده سببلي انخفاض في اخراج البول وورم في القدمين وحاسس بضيق تنفس والم شديد فى الصدر مع تقئ كتير '.encode("utf-8")
}
r = requests.get(url + '/diagnose', data = data)
print(r.json()['Predicted_Disease'])