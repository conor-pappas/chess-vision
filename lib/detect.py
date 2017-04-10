from skimage.filters import sobel
from skimage.feature import canny
from skimage.transform import hough_line, hough_line_peaks
from skimage.color import rgb2gray
from hough_line import HoughLine
from chessboard import Chessboard
import numpy as np

def find_edges(image):
  return canny(sobel(rgb2gray(image)))

def hough_peaks(image):
  c = find_edges(image)
  angles = np.pi / 2 - np.arange(180) / 180.0 * np.pi
  hspace, angles, distances = hough_line(c, angles)
  return hough_line_peaks(hspace, angles, distances)

def find_candidate_lines(image):
  a, angles, dists = hough_peaks(image)
  return list(HoughLine(r, theta) for theta, r in zip(angles, dists))
  
def find_chessboard(image):
  return Chessboard(find_candidate_lines(image))
