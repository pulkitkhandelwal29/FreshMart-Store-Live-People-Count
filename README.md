# FreshMart Store - People Live Count
Real-Time Crowd Detection Analytics at Trading Outlets

## 1. People Counter System
The project helps in measuring the number of people traversing a certain passage or entrance.

### Installation
1. Clone the repository and change the working directory to Project folder<br>
`git clone https://github.com/pulkitkhandelwal29/FreshMart-Store-Live-People-Count.git`

2. Create a virtual environment inside the project folder<br>
`virtualenv myenv`

3. Activate virtual environment <br>
`myenv\Scripts\Activate`

4. Change the directory to `People Counter`<br>
`cd People Counter`

5. Install `dlib` using binary file in environment <br>
`python -m pip install dlib-19.19.0-cp38-cp38-win_amd64.whl`

5. Install the necessary packages in environment <br>
`pip install -r requirements.txt`

### Run the project
<b>Count the no. of people coming inside the outlet</b><br>
`python people_counter_in.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/EntryGateVideo.mp4`
<br><br>
<b>Count the no. of people going out of the outlet</b><br>
`python people_counter_out.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/ExitGateVideo.mp4`

### Libraries
* OpenCV - Standard computer vision/Image processing functions
* Dlib - Implementation of correlation filters / correlation tracker implementation
* Imutils - OpenCV convenience functions
* Numpy - Comprehensive Mathematical Functions

### Trackers 
* Centroid Tracker
* Trackable Object

### Pre-trained Caffe Deep Learning Models
* MobileNet SSD (Single Shot Detector)

<br><br>
## 2. Age and Gender Detection

### Installation

1. Change the directory to `Age_Gender Detection`<br>
`cd Age_Gender Detection`

### Run the Project

<b>Age & Gender Video Detection</b><br>
`python video_age_detection.py --face face_detector --age age_detector --gender gender_detector`

### Libraries
* OpenCV - Standard computer vision/Image processing functions
* Dlib - Implementation of correlation filters / correlation tracker implementation
* Imutils - OpenCV convenience functions
* Numpy - Comprehensive Mathematical Functions

### Pre-trained Caffe Deep Learning Models
* MobileNet SSD (Single Shot Detector)


## Database
For this project, we have used <b>MySQL database</b>.

### Customer Details Table
* Gender
* Minimum Age
* Maximum Age

### People-In Outlet Table
* People Entry Time
* People In Count

### People-Exit Outlet Table
* People Exit Time
* People Exit Count





