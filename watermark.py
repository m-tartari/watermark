#!/usr/bin/env python3
## add watermark to all images in a folder
import os, sys, glob
import numpy as np
from PIL import Image

def find_images(filenames: list, folder: str, formats: list):
      """Returns list of image abspaths for a folder if format in 'formats'"""
      all_photos = [os.path.join(folder, file) for file in filenames if
                  file.lower().endswith(tuple(formats))]
      return all_photos


if __name__ == '__main__':
      base_path = "."
      image_path = "./photos"
      destination_path = "./watermarked/"
      watermark = Image.open("./watermark.png")
      formats = ["jpg", "png"]

      new_width  = 500
      new_height = new_width
      watermark = watermark.resize((new_width, new_height), Image.ANTIALIAS)      
      for folder, subfolders, filenames in os.walk(image_path):
            all_photos = find_images(filenames, folder, formats)
      total = len(all_photos)
      print("user detector: Found "+str(total)+" images in "+image_path)
      print("Working on it...\n")

      i = 0
      ERASE_LINE = '\x1b[2K'
      CURSOR_UP_ONE = '\x1b[1A'
      for file in all_photos:
            photo = Image.open(file)
            photo.paste(watermark, (0,0), watermark )

            file_name = destination_path + file.strip(image_path)  
            # file_name = base_path + "/watermarked/" + "{:03d}".format(i)+".jpg"
            photo.save(file_name)

            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            i = i+1
            progres = i/total*100
            print("Working on it... Done "+"{0:.1f}".format(progres)+"%")
            print("Added watermark to "+str(i)+" images")

      print("Finished, added watermark to "+str(i)+" images")