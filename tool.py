import pytesseract, cv2 #pip install opencv-python numpy pytesseract pillow. 
#https://github.com/UB-Mannheim/tesseract/wiki. Rememeber to add the path to VSCode
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import requests

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #or alway add this line, it locate in program files by default

def extract_captcha_text(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise Exception("Could not read the image")#error handling if can't find the image
        
        # Convert to grayscale to avoid problems related to color 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Use Gaussian blur to reduce noise (random variation of brightness or color information in images)
        blurred = cv2.GaussianBlur(gray, (3,3), 0)
        
        # Use adaptive thresholding
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 2)
        
        # Remove small noise
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 15:  # Reduced threshold for noise removal
                cv2.drawContours(thresh, [contour], -1, 0, -1)
        
        cv2.imwrite('preprocessed.png', thresh) #export preprocessed.png to check if the image has been processed properly or not
        
        custom_config = r'--psm 8'
        text = pytesseract.image_to_string(thresh, config=custom_config)#extractingg the text from the image
        
        return text

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

image_path = 'D:\Websec\midterm\static\captcha\captcha.png' #rememeber to chage path
result = extract_captcha_text(image_path)
print(f"Extracted text: {result}")
#post extracted tool to the web server. Take the # off to make the script post the extracted captcha string to the web(rate:1 sucessful attempts and 2 near sucessful out of 10 attempts during testing...fuck me)
#data = {
#     "captcha_input": result
# }
# submit_resp = requests.post('http://localhost:5000/', data=data)

# if "Correct CAPTCHA" in submit_resp.text:
#     print("CAPTCHA bypassed successfully!")
# else:
#     print("CAPTCHA bypass failed.")