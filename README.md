# Camera-Calibration

This source helps you in calibrating a camera using a checkerboard pattern. It extracts 5 intrinsic parameters (focal lengths, optical center, skew) and 6 extrinsic parameters (rotation & translation vectors for each image).

Extract all the files from the submitted zipped folder.

# 1. Installation & Dependencies

Ensure you have Python and OpenCV installed. Run:
`pip install opencv-python`

# 2. Dataset Preparation

Consider any few images from the /images folder.

# 3. Running the Code

Run the following command,
`python source_code.py`

# 4. Expected Output

The script will:

  -- Detect corners in each image.
  -- Compute and display intrinsic & extrinsic parameters.

  




