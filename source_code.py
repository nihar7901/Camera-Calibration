# Importing necessary libraries
import cv2
import numpy as np
import glob # To find all image files in a folder
import os

CHECKERBOARD = (10,6)  # inner corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.001) # termination criteria for corner refinement

# Preparing 3D Object Points
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1,2)

# Initializing the storage for points
objpoints = []
imgpoints = []

# Loading images
current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, 'images')
images = glob.glob(os.path.join(image_dir, '*.jpg'))  

# Processing each image
print(f"Found {len(images)} images:")
for fname in images:
    print(f"Processing: {os.path.basename(fname)}")
    img = cv2.imread(fname)
    if img is None:
        print(f"Failed to load")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting into grayscale
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)  # Finding Checkerboard Corners

    if not ret:
        print(f"No corners detected")
        continue

    # Refining and storing points
    corners_refined = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
    objpoints.append(objp)
    imgpoints.append(corners_refined)
    print(f"Corners found: {len(corners_refined)}")


    # cv2.namedWindow('Corners', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Corners', 800, 600)
    # cv2.drawChessboardCorners(img, CHECKERBOARD, corners_refined, ret)
    # cv2.imshow('Corners', img)
    # cv2.waitKey(50)  # Displaying each image for 50ms

cv2.destroyAllWindows()


if len(objpoints) == 0:
    print("\n there exists some error")
    exit()

# Camera Calibration using inbuilt function
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Extracting 5 Intrinsic Parameters
fx = mtx[0, 0]  # Focal length in x
fy = mtx[1, 1]  # Focal length in y
cx = mtx[0, 2]  # Principal point x
cy = mtx[1, 2]  # Principal point y
skew = mtx[0, 1]  # Skew coefficient...this is usually zero

# Extracting 6 Extrinsic Parameters (Rotation & Translation)
extrinsic_params = []
for i in range(len(rvecs)):
    rvec = rvecs[i].flatten()  # Converting to 1D array
    tvec = tvecs[i].flatten()  # Converting to 1D array
    extrinsic_params.append((rvec[0], rvec[1], rvec[2], tvec[0], tvec[1], tvec[2]))


print("\n== Camera Calibration Results ==")

# Printing 5 Intrinsic Parameters
print("\nIntrinsic Parameters:")
print(f"1. Focal Length (fx): {fx}")
print(f"2. Focal Length (fy): {fy}")
print(f"3. Principal Point (cx): {cx}")
print(f"4. Principal Point (cy): {cy}")
print(f"5. Skew Coefficient: {skew}")

# Printing 6 Extrinsic Parameters for each image
print("\nExtrinsic Parameters (Rotation & Translation Vectors):")
for i, p in enumerate(extrinsic_params):
    print(f"Image {i+1}:")
    print(f"  1. Rotation X (r1): {p[0]}")
    print(f"  2. Rotation Y (r2): {p[1]}")
    print(f"  3. Rotation Z (r3): {p[2]}")
    print(f"  4. Translation X (t1): {p[3]}")
    print(f"  5. Translation Y (t2): {p[4]}")
    print(f"  6. Translation Z (t3): {p[5]}")



