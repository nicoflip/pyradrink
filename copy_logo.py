import os
import shutil

src = r"C:\Users\tarej\.gemini\antigravity\brain\8fa9a145-543a-4872-acc5-d87afc3bb0fd\.user_uploaded\media__1790991502640.png"
dst = r"c:\Users\tarej\Documents\pyradrink\assets\pyradrink_logo.png"

shutil.copy2(src, dst)
print("Copied media__1790991502640.png to assets/pyradrink_logo.png")
