## Project Overview

The AI-Powered Answer Sheet Evaluation System aims to automate the evaluation of handwritten answer sheets using Computer Vision, OCR, NLP, and Machine Learning.

Traditional answer evaluation is time-consuming, difficult to scale, and prone to inconsistencies. This project seeks to build an intelligent pipeline capable of extracting handwritten answers, understanding their content, comparing them with reference answers, and generating marks and feedback automatically.

## Current Pipeline

```
Scanned Answer Sheet
        │
        ▼
Image Preprocessing (Computer Vision)
        │
        ▼
OCR (PaddleOCR)
        │
        ▼
OCR Cache *(In Progress)*
        │
        ▼
Raw Text Storage
        │
        ▼
Text Cleaning
        │
        ▼
Question Segmentation
        │
        ▼
Structured JSON
        │
        ▼
Semantic Evaluation
        │
        ▼
Marks & Feedback Generation
```

## Current Status

### ✅ Completed

- Image loading using OpenCV
- Grayscale conversion
- Adaptive Gaussian Thresholding
- Noise removal using contour filtering
- Contour detection
- Bounding box generation
- Dilation-based text grouping
- PaddleOCR integration
- Handwritten text extraction from scanned answer sheets
- Python 3.11 environment setup and compatibility fixes
- OCR tested successfully on multiple handwritten answer sheets

### 🚧 In Progress

- Modular OCR module (`ocr.py`)
- OCR caching using image hashing
- Metadata management (`metadata.json`)
- Raw OCR text storage
- Text cleaning and normalization

### 📅 Planned

- Question-answer segmentation
- Structured JSON generation
- Embedding generation
- Semantic similarity evaluation
- Automated mark allocation
- Feedback generation
- Web interface/API integration