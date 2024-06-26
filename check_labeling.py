from subprocess import run
import cv2

# Get all the filenames of all the images
proc = run(['ls', 'images'], capture_output = True)
images = proc.stdout.decode()[:-1].split()

# Display each image and each labeled rectangle
for img_name in images:
    # Get the image from file
    img = cv2.imread("images/" + img_name)
    # Now get the labeled rectangles
    try:
        with open('labels/' + img_name[:-3] + 'txt', 'r') as label_file:
            labels = label_file.readlines()
    except FileNotFoundError:
        labels = []
    for label in labels:
        # Convert the stored proportions to pixel count
        label = label.split()
        label[1] = int(float(label[1]) * img.shape[1])
        label[2] = int(float(label[2]) * img.shape[0])
        label[3] = int(float(label[3]) * img.shape[1])
        label[4] = int(float(label[4]) * img.shape[0])
        # Draw rectangle around dog face
        cv2.rectangle(img, (label[1], label[2]), (label[3], label[4]), (0, 255, 0), 3)
    # Show the image
    cv2.imshow(img_name[:-4], img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
