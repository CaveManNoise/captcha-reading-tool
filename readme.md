This is a small project of mine during the web security class at school where i am tasked of creating a tool to bypass the most popular form of captcha (not recaptcha). I have a lot of fun trying to figure out how OCR work but i be lying if i say it was easy. Though the result may not work great but it teach me a lot of how a tool work instead of blindly go in like a skiddie

Note: For the sake of simplicity, my tool only focus on how the tool try to read and recognize the letter in the captcha. Everything needed to install beforehand i note it down in the comment section.
1. Capturing the CAPTCHA Image

The CAPTCHA image is usually downloaded or screenshotted from the website (this tool i tested it locally on my group captcha website)
The image often contains distorted, noisy, or overlapping characters to make OCR-based recognition difficult.
2. Preprocessing the Image
- The image will be processed to enhance to make the OCR job at reading the captcha a little bit easier

  +Grayscale Conversion: Converts the image to black and white to remove color distractions.
  +Noise Reduction: Removes unwanted pixels and background noise.
  +Thresholding (Binarization): Converts the image into a binary format (black/white), making text more distinguishable.
  +Blurring & Sharpening: Enhances character edges.
  +Contour Detection: Identifies text-like regions to remove unnecessary elements.
3. Applying OCR (Tesseract OCR)
- Once the image is cleaned, OCR (Tesseract) is used to extract text.

  +The OCR engine analyzes pixel patterns in the image.
  +It matches these patterns with its trained character dataset.
  +It then outputs a text string that represents the extracted CAPTCHA.
