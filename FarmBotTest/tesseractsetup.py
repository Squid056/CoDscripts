import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# window_rect = win32gui.GetWindowRect(win32gui.FindWindow(None, "Call of Dragons"))
# print(window_rect) 




# img = Image.open("StatTracker/testdata/test3-7.png")
# basewidth = 1500
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
# img.save("temp.png")

# contrast = ImageEnhance.Contrast(img)
# contrast.enhance(1.8).convert('L').save("temp2.png")


# print(pytesseract.image_to_string(Image.open("temp2.png")))


