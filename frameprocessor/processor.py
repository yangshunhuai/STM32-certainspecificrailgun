#!/usr/bin/env python3

'''
Arguments:
    -i: Input video file in OpenCV supported formats
    -o: Output folder to save raw picture files in binary formats
    -f: Output frame rate. This value must be lower than the original frame rate.
'''

import cv2
import PIL
import sys
import getopt
import logging

argvs = "i:o:f:"

def main():
    logging.basicConfig(level=logging.DEBUG #设置日志输出格式
                    ,filename="processor.log" #log日志输出的文件位置和文件名
                    ,filemode="w" #文件的写入格式，w为重新写入文件，默认是追加
                    ,format="%(asctime)s - %(levelname)-s - %(message)s" #日志输出的格式
                    # -8表示占位符，让输出左对齐，输出长度都为8位
                    ,datefmt="%Y-%m-%d %H:%M:%S" #时间输出的格式
                    )

    # Get options. The first one is wasted by default
    options, args = getopt.getopt(sys.argv[1:], argvs)

    inputfile = ""
    outputfile = ""

    for i in options:
        name, value = i
        if name == "-i":
            inputfile = value
        if name == "-o":
            outputfile = value
    
    print(f"SSD1306 frame processor v1.0\nInput file:    {inputfile}\nOutput folder: {outputfile}")

    logging.debug("Opening file using OpenCV")
    video = cv2.VideoCapture(inputfile)
    

        

if __name__ == "__main__":
    main()
