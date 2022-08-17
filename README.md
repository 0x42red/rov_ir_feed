## About
This is a raspberry pi compatible facial recognition tool.  This tool is used to explain how retro reflectors can be used to defeat basic facial recognition.  Additionally see the 3DFiles folder for a 3d printable case.

## Running
First plug in the camera to your Raspberry Pi
```
pip install cv2
python cam.py &
exit
```

## Debug
If the code complains about not having access to the camera at position 0 verify there is no process using the camera.  If that doesn't work loop through the cameras available in `/dev` by checking `ls /dev | grep video`

## Hardware
- Raspberry PI 4 Model B
- [Arducam 1080p](https://www.amazon.com/dp/B0829HZ3Q7)

## Notes
This is cobbled together and most of the code was written at 2am thursday night before defcon.  I am sorry.