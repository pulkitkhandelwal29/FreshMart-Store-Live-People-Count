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

<br><br>
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

<br><br>
## Demonstration

### 1. People Entry Gate
<br>

![1](https://user-images.githubusercontent.com/67990422/139659022-5dbdaec0-f7fd-43a3-b0ba-6a47dc8c3fb0.PNG)
![2](https://user-images.githubusercontent.com/67990422/139659027-511a612c-2750-4cea-92fb-4b3ff32d016b.PNG)
![3](https://user-images.githubusercontent.com/67990422/139659031-e044a244-d616-4cbb-94ee-88d5cbb1192f.PNG)

<br><br>

### 2. People Exit Gate

<br>

![1](https://user-images.githubusercontent.com/67990422/139659263-8a3fbc58-7073-45b6-bf07-f781c5ddde66.PNG)
![2](https://user-images.githubusercontent.com/67990422/139659268-1a7bc8dc-6931-4c74-85bd-6ec7f698e675.PNG)
![3](https://user-images.githubusercontent.com/67990422/139659269-98d2fa08-bfbc-4ccc-ad2c-2d6fbcb3d246.PNG)

<br><br>

### 3. Age & Gender
<br>

![Screenshot (241)](https://user-images.githubusercontent.com/67990422/139659860-e61959bf-e862-4456-b55b-2aed01fb690e.png)



