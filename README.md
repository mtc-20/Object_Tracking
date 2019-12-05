# Object Tracking Algorithms
**Compile and keep python scripts that can track objects.**
**[INFO_051219]:** Haven't tested any of these codes on Raspberry Pi yet.



## OpenCV Object Trackers
OpenCV has about 7 different object tracking algorithms, the accessibility to which depends on your version of OpenCV. Check out [Adrian's guide][pyimage] to know more, since that's where I learnt about it. The code in this repo is also taken from the same guide.

[Script][1]

**Notes:**
- *The problem, atleast from my observations, is that they fail when the tracked object goes out of frame*
- *So, these are more useful for follower applications, where the objective is to ensure the tracked object is always within the frame*
- *The ROI GUI (again from OpenCV), although pretty neat, makes it somewhat inefficient for autonomous applications* 

## GOTURN Object Tracker
GOTURN is a deep learning based object tracker, that is also available on OpenCV. For more info about the model as well as the trained model files, check out [Satya Mallick's guide][locv].

[GOTURN Script][2]

**Notes:**
- *The model fails/seems to break for objects or feed that the model was not trained for*
- *If the object has gone out of frame for a moment, it seems to break*
- *The **major** problem for me was that it's quite heavy in terms of resource usage; it  made my PC laggy and pretty much crashed it (Ubuntu 18) the first (and only time) I used it. I havent tried running it on GPU yet*

<!--
## Object Detection and Tracking
This script, also taken from [Adrian's PyImageSearch][pyimg], essentially loads trained objection detection models using OpenCV and then tracks them from frame to frame using the concept of Euclidean distances and centroid tracking.

[Script][3]

**Notes:**
- *Worked quite well on my laptop webcam, the pretrained face detection model that I used was quite robust, so tracking worked well unless for extremely high speed movement*
- *I like that each detected object has a reference ID, for when it goes out of frame*
-->




[pyimage]: https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
[locv]: https://www.learnopencv.com/goturn-deep-learning-based-object-tracking/
[pyimg]:https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/

[1]: https://github.com/mtc-20/Object_Tracking/blob/master/cv_objtracker.py
[2]: https://github.com/mtc-20/Object_Tracking/blob/master/GOTURN_tracking/test_GOTURN.py

