# Manav Sanghvi
# 1/11/2024
# Periodic Image Capture

import cv2
import os
import time

def periodic_image_capture(file_path: str, clears_images: bool, cameraNumber, seconds_between_capture):
    # Get USB camera
    camera = cv2.VideoCapture(cameraNumber)

    # Start the num of images at 0
    num_of_images = 0

    # If we do not clear the images before starting the function
    if clears_images == False:
        # Go through each file in the images directory and add to the image counter
        for path in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, path)):
                num_of_images += 1; 
        
    # Image file extension
    file_extension = "png"

    # Initalize the previous time at 0
    previous_time = 0

    if camera.isOpened:
        print("WORKING")
        while True:
            # Capture the time this loop started
            inital_time = time.time()

            # Capture a frame of the camera
            ret, frame = camera.read()

            # Display the Frame
            cv2.imshow('frame', frame)

            '''THIS WORKS BUT WILL PAUSE THE ENTIRE PREVIEW DISPLAY'''
            '''WE CAN IMPLEMENT EITHER METHOD DEPENDING ON WHAT WE NEED'''
            #time.sleep(seconds_between_capture)

            # Check if enough time has passed between the previous capture and the current iteration of the loop
            if inital_time - previous_time >= seconds_between_capture or previous_time == 0:
                # Create an image name using the current image number and file extension
                image_name = "image_{}.".format(num_of_images) + file_extension

                # Write the image to the correct filepath
                cv2.imwrite(file_path + image_name, frame)

                print("Image Taken:", num_of_images)

                # Add one to the number of images
                num_of_images += 1

                # Set the previous_time to the current time
                previous_time = time.time()

            # Close the application if q is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Closing")
                break
    else:
        print("FAILED")

if __name__ == "__main__":
    '''Starts Image Counter at 0: '''
    periodic_image_capture("../", True, 0, 5)
    '''Starts Image Counter at how many ever images we already have: '''
    #periodic_image_capture("../", False, 0, 5)
    
# To Do Connect to ROS Publisher





