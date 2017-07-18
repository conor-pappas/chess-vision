from skimage.filters import threshold_otsu, sobel
from skimage.transform import hough_line, hough_line_peaks
from skimage.color import rgb2gray
from hough_line import HoughLine
import numpy as np

NUM_HOUGH_ANGLES = 180

def find_edges(image):
  greyscale = sobel(rgb2gray(image))
  threshold = threshold_otsu(greyscale)
  return greyscale >= threshold

def hough_peaks(image):
  c = find_edges(image)
  angles = np.arange(NUM_HOUGH_ANGLES) * np.pi / NUM_HOUGH_ANGLES
  hspace, angles, distances = hough_line(c, angles)
  return hough_line_peaks(hspace, angles, distances)

def find_candidate_lines(image):
  a, angles, dists = hough_peaks(image)
  return list(HoughLine(r, theta) for theta, r in zip(angles, dists))
