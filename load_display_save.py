import argparse
import cv2

#Argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
ap.add_argument("-o", "--output", required=True, help = "Path to the save image")
args = vars(ap.parse_args())

#Load image ans show basic information
image_display = cv2.imread(args["image"])
print("width: %d pixels" % (image_display.shape[1]))
print("heigth: %d pixels" % (image_display.shape[0]))
print("channels: %d" % (image_display.shape[2]))
print("Channels are:", image_display.shape)

#Show the image and wait for the keypress
cv2.imshow("Image", image_display)
cv2.waitKey(0)

#Convert to jpg file
cv2.imwrite(args["output"], image_display)