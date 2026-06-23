## Project Overview

The AI-Powered Answer Sheet Evaluation System aims to automate the evaluation of handwritten answer sheets using Computer Vision, OCR, NLP, and Machine Learning.

Traditional answer evaluation is time-consuming, difficult to scale, and prone to inconsistencies. This project seeks to build an intelligent pipeline capable of extracting handwritten answers, understanding their content, comparing them with reference answers, and generating marks and feedback automatically.

## Current Pipeline

Scanned Answer Sheet
↓
Image Preprocessing
↓
Noise Removal
↓
Document Structure Analysis
↓
OCR
↓
Text Extraction
↓
Semantic Evaluation
↓
Marks & Feedback Generation

## Current Status

Implemented:

* Image loading using OpenCV
* Grayscale conversion
* Adaptive Gaussian Thresholding
* Noise removal using contour filtering
* Contour detection
* Bounding box generation
* Dilation-based text grouping

In Progress:

* Text line detection
* ROI extraction
* Question-answer segmentation

Planned:

* OCR integration
* Handwriting recognition
* Semantic answer evaluation
* Automated grading and feedback
