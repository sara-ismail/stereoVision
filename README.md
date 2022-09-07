# stereoVision
The aim of this project is to research the possibility and potential of 360 stereo vesion using RICOH THETA cameras.  

### Hardware:
The most suitable RICOH THETA camera models for this job are the **THETA V/Z1**
* *THETA S* is not suitable as it only streams 2 dual-fisheye views as motionJPEG
* *THETA V or Z1* stream in equirectangular  

**Used equipment:**  
  * 2 THETA V/Z1 cameras for the stereo
  * NVIDIA Jetson Xavier

### Software:
I followed the [RICOH THETA Development on Linux](https://codetricity.github.io/theta-linux/ "RICOH THETA Development on Linux")
website to set up the software. 

- I first tried to utilize v4l2loopback, however, the cameras could't stream through /dev/video,
so I went with [gstthetauvc](https://github.com/nickel110/gstthetauvc "gstthetauvc") instead.

**NOTE:** the README.md file of the [gstthetauvc](https://github.com/nickel110/gstthetauvc "gstthetauvc") repo states that compiling libuvc is a prerequisite,  
however, to work with the THETA cameras, you should only compile the libuvc-theta version.

After installing gstreamer and compiling gstthetauvc, you can stream the camera via:
  1. Terminal command:
```
gst-launch-1.0 thetauvcsrc mode=4K ! queue ! h264parse ! nvv4l2decoder ! queue ! nv3dsink sync=false
```
  2. OpenCV:
```python
VideoCapture("Your gstremer pipeline")
```
The following pipeline worked on my Jetson Xavier with the THETA V cameras:  
"thetauvcsrc ! decodebin ! autovideoconvert ! video/x-raw,format=BGRx ! queue ! videoconvert ! video/x-raw,format=BGR ! queue ! appsink"
(*omit both queue for no buffering*)

**NOTE:** to stream from 2 cameras simontaniously, you can either
 - call the cv2.VideoCapture() function twice using the same pipeline:
 ```python
cap1 = cv2.VideoCapture("Your gstremer pipeline")
cap2 = cv2.VideoCapture("Your gstremer pipeline")
```
 - paste the terminal command twice:
```
gst-launch-1.0 thetauvcsrc mode=4K ! queue ! h264parse ! nvv4l2decoder ! queue ! nv3dsink sync=false thetauvcsrc mode=4K ! queue ! h264parse ! nvv4l2decoder ! queue ! nv3dsink sync=false
```
### camera_stream.py
Creats a class that handles each camera in a seperate thread
-> Decreases latency on the cameras.

### stream.py
Used to simply read and stream two theta cameras using the CameraVideoStream threading class.

### fps_calc.py
Calculates the Frames per Second rate of the cameras and displays it on the video stream.

### stereo_sgbm.py
Operates a step by step calibration of the cameras then creats and displays a live depth map.
