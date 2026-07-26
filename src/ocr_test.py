from paddleocr import PaddleOCR

ocr = PaddleOCR()

results = ocr.predict("data/diag.png")

for page in results:
    print("\n===== EXTRACTED TEXT =====\n")
    for line in page["rec_texts"]:
        print(line)