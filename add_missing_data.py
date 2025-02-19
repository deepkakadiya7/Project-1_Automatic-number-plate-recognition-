import csv
import numpy as np
from scipy.interpolate import interp1d

def interpolate_bounding_boxes(data):
  frame_numbers = np.array([int(row['frame_nmr']) for row in data])
  car_ids = np.array([int(float(row['car_id'])) for row in data])
  car_bboxes = np.array([list(map(float, row['car_bbox'][1:-1].split())) for row in data])
  license_plate_bboxes = np.array([list(map(float, row['license_plate_bbox'][1:-1].split())) for row in data])
  return interpolated_data

# Load the CSV file
with open('test.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Interpolate missing data
interpolated_data = interpolate_bounding_boxes(data)

# Write updated data to a new CSV file
header = ['frame_nmr', 'car_id', 'car_bbox', 'license_plate_bbox', 'license_plate_bbox_score', 'license_number', 'license_number_score']
with open('test_interpolated.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(interpolated_data)
