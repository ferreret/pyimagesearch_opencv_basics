import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image",
                default="adrian.png")
args = vars(ap.parse_args())

# load the image, grab its spatial dimensions (width and height)
# and then display the original image to our screen
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# images are simpy numpy arrays, -- with the origin on the top left
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# access the pixel located at x=50 y=20
(b, g, r) = image[20, 50]
print("Pixel at (20, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at x=50 y=20 and set it to pure red
image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (20, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Compute the center of the image
(cX, cY) = (w // 2, h // 2)

# since we are using NumPy arrays, we can apply slicing and grab large chunks/regions of the image
# here , we'll grab the top-left corner
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner", tl)

# in a similar fashion, we can now grab the top-right, bottom-right, and bottom-left
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# set the top-left corner of the image to pure green (0, 255, 0)
image[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Updated", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
