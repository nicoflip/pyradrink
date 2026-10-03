import os
import shutil

src_dir = r"C:\Users\tarej\.gemini\antigravity\brain\8fa9a145-543a-4872-acc5-d87afc3bb0fd\.user_uploaded"
dst_dir = r"c:\Users\tarej\Documents\pyradrink\assets"

os.makedirs(dst_dir, exist_ok=True)

files = os.listdir(src_dir)
print("Files in .user_uploaded:", files)

for f in files:
    src = os.path.join(src_dir, f)
    dst = os.path.join(dst_dir, f)
    shutil.copy2(src, dst)
    print(f"Copied {f} to assets/")

# Latest uploaded image for home screen
latest_img = "media__1790990988445.png" if "media__1790990988445.png" in files else files[-1]

# Copy the latest file as home_bg.png
shutil.copy2(os.path.join(src_dir, latest_img), os.path.join(dst_dir, "home_bg.png"))
print("Set home_bg.png to", latest_img)
