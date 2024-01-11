# Manav Sanghvi
# 1/11/2024
# Periodic Image Capture

import cv2
import schedule

# Number or address for the USB Cam
cameraNumber = 0

# Number of seconds between image captures
seconds_between_capture = 10

# Get USB camera
camera = cv2.VideoCapture(cameraNumber)

# Number of current images
num_of_images = 0

# Image file extension
file_extension = "png"

# Take a capture
def capture():
    global num_of_images

    # Create an image name using the current image number and file extension
    image_name = "image_{}.".format(num_of_images) + file_extension

    # Write the image to a file
    cv2.imwrite(image_name, frame)

    print("Image Taken:", num_of_images)

    # Add one to the number of images
    num_of_images += 1

# Schedules a capture to be called at each interval
schedule.every(seconds_between_capture).seconds.do(capture)

if camera.isOpened:
    print("WORKING")

    while True:
        # Capture a frame of the camera
        ret, frame = camera.read()

        # Display the Frame
        cv2.imshow('frame', frame)

        # Run the next pending capture call
        schedule.run_pending()

        # Close the application if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Closing application")
            break
else:
    print("FAILED")
    

# To Do Connect to ROS Publisher





