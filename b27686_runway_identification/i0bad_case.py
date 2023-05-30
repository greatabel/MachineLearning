import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained HED model
net = cv2.dnn.readNet("deploy.prototxt", "hed_pretrained_bsds.caffemodel")

# Load your image
img = cv2.imread("runway.jpg")

# Convert the image to blob
blob = cv2.dnn.blobFromImage(
    img,
    scalefactor=1.0,
    size=(500, 500),
    mean=(104.00698793, 116.66876762, 122.67891434),
    swapRB=False,
    crop=False,
)

# Set the blob as the input of the neural network
net.setInput(blob)

# Perform a forward pass to compute the edges
edges = net.forward()

# Normalize the output edges
edges = cv2.normalize(edges[0, 0], None, 0, 255, cv2.NORM_MINMAX)

# Convert edges to 8-bit image
edges_8u = np.uint8(edges)

# Use Canny edge detector
edges_detected = cv2.Canny(edges_8u, 50, 150, apertureSize=3)

# Apply Hough Line Transform
lines = cv2.HoughLinesP(
    edges_detected,
    rho=1,
    theta=np.pi / 180,
    threshold=50,
    minLineLength=50,
    maxLineGap=10,
)

# Draw the lines on the original image
if lines is not None:
    for i in range(0, len(lines)):
        l = lines[i][0]
        cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 2, cv2.LINE_AA, 0)

# Show the original image with the runway lines highlighted
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
