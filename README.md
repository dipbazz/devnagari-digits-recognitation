# Devnagari Handwritten Numerals recognition
Offline Nepali Handwritten Numerals recognition using K-Nearest Neighbour and integrated the system into web using django framework.

## Setup
1. Clone the project in your directory.
2. Create a virtual enviroment.
3. Install all the requirements files using pip "pip install -r /path/to/requirements.txt".
4. Download dataset from [here](https://www.kaggle.com/dipbazz/devanagari-numerals-datasets "Devanagari numerals dataset") and paste in the directory "devanagariDigitsOCR/Home/digits_detection_model"
5. Execute traineer.py file loacted at "devanagariDigitsOCR/Home/digits_detection_model" (be sure to navigate to the same directory while Executing traineer.py to set cache.pkl file)
6. runserver (python manage.py runserver)
7. you are good to go, check any devanagari handwritten numerals in a system. 
I have uploaded image for testing purpose in test_image folder in home directory.


## Requirements
1. Python (3.6.4)
2. Django==2.1
3. numpy==1.15.1
4. opencv-python==3.4.2.17
5. pandas==0.23.4
6. Pillow==5.2.0
7. python-dateutil==2.7.3
8. pytz==2018.5
9. scikit-learn==0.19.2
10. scipy==1.1.0
11. six==1.11.0
12. sklearn==0.0


## References
1. [Ashok pant/nhcr](https://github.com/ashokpant/nhcr)
2. [wkudaka/django-scikit-learn-tutorial](https://github.com/wkudaka/django-scikit-learn-tutorial)
