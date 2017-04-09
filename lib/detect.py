from skimage.filters import sobel
from skimage.feature import canny, corner_harris, corner_peaks
from skimage.transform import probabilistic_hough_line, hough_line, hough_line_peaks
from skimage.color import rgb2gray
import numpy as np

def find_edges(image):
  return canny(sobel(rgb2gray(image)))

def candidate_lines(image):
  c = find_edges(image)
  return probabilistic_hough_line(c, line_length=100)

def hough_peaks(image):
  c = find_edges(image)
  angles = np.pi / 2 - np.arange(180) / 180.0 * np.pi
  hspace, angles, distances = hough_line(c, angles)
  return hough_line_peaks(hspace, angles, distances, num_peaks=18)

def detect_corners(image):
  c = canny(rgb2gray(image))
  return corner_peaks(corner_harris(c), min_distance=20)
