# stereoVision
**The aim of this project is to research the possibility and potential of 360 stereo vesion using RICOH THETA cameras.**  

### Hardware:
The most suitable RICOH THETA camera model for this job are the **THETA V/Z1**
* *THETA S* only streams 2 dual-fisheye views as motionJPEG
* *THETA V or Z1* stream in equirectangular  

**Used equipment:**  
  * 2 THETA V/Z1 cameras for the stereo
  * NVIDIA Jetson Xavier

### Software:
I followed the [RICOH THETA Development on Linux](https://codetricity.github.io/theta-linux/ "RICOH THETA Development on Linux")
website to set up the software. 

- I first tried to utilize v4l2loopback, however, the cameras didn't stream through /dev/video0  
so, I went with [gstthetauvc](https://github.com/nickel110/gstthetauvc "gstthetauvc") instead.





