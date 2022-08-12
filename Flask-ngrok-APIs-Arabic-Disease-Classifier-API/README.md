# Arabic Disease Classifier 

## Description
Naive and primitive **[NLP](https://www.ibm.com/cloud/learn/natural-language-processing)** API to predict disease of given symptom. Trianed on [ds.xlsx](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-Arabic-Disease-Classifier-API/ds.xlsx).
you can provide better dataset for better result.

## Setup
- First, in your **[Google Drive/My Drive](https://drive.google.com/drive/my-drive)** create a folder with "Model-Files" as name.
- Upload *[Dataset](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-Arabic-Disease-Classifier-API/ds.xlsx)* to the recently created *Model-Files* folder.
- If you don't have flask-ngrok account read [Flask-ngrok setup](https://github.com/MahmoudHussienMohamed/Flask-APIs#flask-ngrok-setup).
- Replace "\<***YourAuthToken***\>" with your own in the *'ADC-API'* colab notebook.
- Run the notebook in GPU runtime (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-colab)* if not).
- Notebook will ask you to mount Google Drive. (see *[this](https://github.com/MahmoudHussienMohamed/Flask-APIs#google-drive)* if not)
Now your API is running!

## Requests
The API has 1 main route which is:
- **'/diagnose'** accepts `sympots` and return the coresponding predicted disease. (***NOTE***: Supposed to be "symptoms")


## Test and run
You can test the API with [Test.py](https://github.com/MahmoudHussienMohamed/Flask-APIs/blob/main/Flask-ngrok-APIs-Arabic-Disease-Classifier-API/Test.py).
Update `url` variable with **2nd link** produced by **last cell** in the notebook then run it.
You should be able to see "فشل كلوي"


