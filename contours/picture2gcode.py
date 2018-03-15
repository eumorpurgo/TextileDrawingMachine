#!/usr/bin/env python2.7

import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import numpy as np
import argparse
import os
import sys
from PIL import Image

speed = 1000

def applyLowPassFilterToPaths( paths, precision=10, sigmaRate=2 ):
    for i in range(len(paths)):
        sys.stdout.write ( str(i+1)+"/"+str(len(paths))+"          \r" )
        x = paths[i][0]
        y = paths[i][1]

        tx = np.linspace(0, 1, len(x))
        tx2 = np.linspace(0, 1, len(x)*precision)

        ty = np.linspace(0, 1, len(y))
        ty2 = np.linspace(0, 1, len(y)*precision)

        x2 = np.interp(tx2, tx, x)
        y2 = np.interp(ty2, ty, y)

        sigma = precision/sigmaRate

        x = gaussian_filter1d(x2, sigma)
        y = gaussian_filter1d(y2, sigma)

        paths[i][0] = x
        paths[i][1] = y

    return paths

def findContours(image):

    ret = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    if len(ret) == 3:
        im2, contours, hierarchy = ret
    else :
        contours, chunk = ret

    if len(contours) == 0 :
        return None

    contoursCoordonates = []
    for j in range(len(contours)) :
        sys.stdout.write ( str(j+1)+"/"+str(len(contours))+"          \r" )
        c = contours[j];
        x,y = c[:,0].T
        contoursCoordonates += [[x, y]]
    return contoursCoordonates

def findFilledContours(image, toolSizeInPixel=21):
    outputGcode = ''
    outputSVG = ''

    contours = []

    while True:
        ret = findContours(image)
        if ret is None:
            break
        else:
            contours += ret
            kernelSize = int(round(toolSizeInPixel/2))
            kernel = np.ones((kernelSize,kernelSize),np.uint8)
            image = cv2.erode(image,kernel,iterations = 1)

    return contours

def anyImageToBlackAndWhite( image ):
        imgray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        ret, thresholdedImage = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
        return thresholdedImage

def addBorderToImage(image, borderSizeInPixel = 1 ):
    whiteColor = [255, 255, 255] # White
    top, bottom, left, right = [ borderSizeInPixel ]*4
    return cv2.copyMakeBorder(image, top, bottom, left, right, borderType=cv2.BORDER_CONSTANT, value=whiteColor )

def findToolPathsFromImage(image, fillContours=False, toolDiameterInmm=10):

    image = addBorderToImage(image)
    image = anyImageToBlackAndWhite(image)

    if fillContours == True:
         paths = findFilledContours(image, toolDiameterInmm)
    else :
         paths = findContours(image)

    return paths

def getSpeed():
    global speed
    return "F" + str(speed)

def putToolDown():
    return "G0 Z5 F1000 \n"

def putToolUp():
    return "G0 Z0 F1000 \n"

def wait():
    return "G4 P120 \n"

def exportPathsToGcodeFile( paths, gcodeFilePath ):
    g = open(gcodeFilePath, 'w+')

    g.write("G21 \n")
    g.write("G92 X0 Y0 Z0 \n")

    for j in range(len(paths)) :
        sys.stdout.write( str(j+1) + "/" + str(len(paths)) + "          \r")
        x = paths[j][0];
        y = paths[j][1];

        g.write(putToolUp())
        g.write(wait())
        g.write('G0 X'+str(x[0]) + ' ' + 'Y' + str(y[0]) + ' ' + getSpeed() + ' \n')
        g.write(putToolDown())
        g.write(wait())

        for i in range(1,len(x)):
            g.write('G0 X'+str(x[i]) + ' ' + 'Y' + str(y[i]) + ' ' + getSpeed() + ' \n')

        # Close the shape
        g.write('G0 X'+str(x[0]) + ' ' + 'Y'+str(y[0]) + ' ' + getSpeed() + ' \n')

    g.write(putToolUp())
    g.write(wait())
    g.write("G0 X0 Y0 \n")
    g.close()

def exportPathsToSVGFile( paths, svgFilePath, width, height):
    f = open(svgFilePath, 'w+')

    f.write('<svg width="'+str(width)+'mm" height="'+str(height)+'mm" xmlns="http://www.w3.org/2000/svg" fill="transparent" >')

    for j in range(len(paths)) :
        sys.stdout.write ( str(j+1)+"/"+str(len(paths))+"          \r" )
        x = paths[j][0];
        y = paths[j][1];

        f.write('<path d="M')
        f.write(str(x[0])+  ' ' + str(y[0])+' ')

        for i in range(1,len(x)):
            f.write('L' +str(x[i])+  ' ' + str(y[i])+' ')

        # Close the Shape
        f.write(str(x[0])+  ' ' + str(y[0])+' ')

        f.write('" stroke="black" fill="transparent"/>\n')

    f.write('</svg>')

    f.close()

def getDpiFromImagePath(imagePath):
    image = Image.open(imagePath)
    try:
        dpiX , dpiY = image.info['dpi']
        return dpiX, dpiY
    except:
        return None

def toolDiameterInmmToPixels ( diameterInmm, scaleCorrectionFactor ):
    return float(diameterInmm) / float(scaleCorrectionFactor)

def getBluePixels(image):
    height, width, depth = image.shape

    pixelSelection = np.logical_and(np.logical_and(image[:,:,0] >=127, image[:,:,1] == 0),  image[:,:,2] == 0)

    return pixelSelection

def getRedPixels(image):
    height, width, depth = image.shape

    pixelSelection = np.logical_and(np.logical_and(image[:,:,0] == 0 , image[:,:,1] == 0),  image[:,:,2] >= 127 )

    return pixelSelection

def getGreenPixels(image):
    height, width, depth = image.shape

    pixelSelection = np.logical_and(np.logical_and(image[:,:,0] == 0 , image[:,:,1] >=127),  image[:,:,2] == 0 )

    return pixelSelection


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process image files into SVG and output GCODE.')
    parser.add_argument('--input-path', metavar='FILE', dest="input_path", help='Path to the image file to process.')
    parser.add_argument('--speed', type=int, default=1000, help="The speed for the machine X and Y motors")
    parser.add_argument('--image-width-in-mm', type=int, help="The with of the target/output image in mm")
    parser.add_argument('--fill', choices=['no-fill', 'fill-in', 'auto-fill'], default='no-fill', help='If fill-in: fill all shapes. If no-fill : just find contours. If auto-fill: if red: just contours if blue: fill shape.')
    parser.add_argument('--filtering', action="store_true", help='If True, smooth path with low pass filter, quick but dirty.')
    parser.add_argument('--hd-smoothing', action="store_true", default=False, help='If True, HD smoothing, good quality result but might be slow.')
    parser.add_argument('--tool-diameter-in-mm', type=float, default=21, help='Tool diameter in millimeters.')
    parser.add_argument('--hd-precision-factor', type=int, default=3, help='The highest, the best quality, the longer to compute. 3 is default.')

    args = parser.parse_args()
    print( "Starting to processs file: " + args.input_path )

    #create output dir if not existing
    if not os.path.exists('output'):
        os.makedirs('output')

    hdPrecisionFactor = args.hd_precision_factor

    #get file name from path
    tmp = os.path.basename(args.input_path)
    outputName = os.path.splitext(tmp)[0]

    print("Loading Picture ...")
    image = cv2.imread(args.input_path)

    print("Computing Correction factor ...")
    if len(image.shape) == 3 :
        heightInPixel, widthInPixel, channels = image.shape
    else:
        heightInPixel, widthInPixel = image.shape

    if args.image_width_in_mm is None :
        ret = getDpiFromImagePath(args.input_path)
        if ret is None:
            raise ValueError("[FAIL] No DPI found and no image with in parameter, cannot compute size.")
        dpix, dpiy = ret

        scaleCorrectionFactor = 1.0/float(dpix) * 25.4
    else:
        scaleCorrectionFactor = float(args.image_width_in_mm) / float(widthInPixel)

    heightInmm = scaleCorrectionFactor * float(heightInPixel)
    widthInmm = scaleCorrectionFactor * float(widthInPixel)

    print("Reading speed ...")
    speed = args.speed

    print("Computing Tool size ...")
    toolDiameterInmm = args.tool_diameter_in_mm
    toolDiameterInPixel = int(round( (float(toolDiameterInmm) / scaleCorrectionFactor) * float(hdPrecisionFactor) ))

    if args.hd_smoothing :
        print("Scaling image up ...")
        image = cv2.resize(image, (0,0), fx=hdPrecisionFactor, fy=hdPrecisionFactor)

    print("Computing tool path ...")
    if args.fill == 'fill-in':
        paths = findToolPathsFromImage(image, fillContours=True, toolDiameterInmm=toolDiameterInPixel)
    elif args.fill == 'no-fill':
        paths = findToolPathsFromImage(image, fillContours=False, toolDiameterInmm=toolDiameterInPixel)
    elif args.fill == 'auto-fill' :
        blackColor = [0,0,0]
        whiteColor = [255,255,255]

        blueImage = np.copy(image)
        redImage = np.copy(image)
        Image = np.copy(image)

        bluePixels = getBluePixels(image)

        blueImage[bluePixels] = blackColor
        blueImage[np.logical_not( bluePixels )] = whiteColor

        redPixels = getRedPixels(image)

        redImage[redPixels] = blackColor
        redImage[np.logical_not( redPixels )] = whiteColor

        filledPaths = findToolPathsFromImage(blueImage, fillContours=True, toolDiameterInmm=toolDiameterInPixel)

        emptyPaths = findToolPathsFromImage(redImage, fillContours=False, toolDiameterInmm=toolDiameterInPixel)
        
        if emptyPaths is not None:
            paths = emptyPaths
            if filledPaths is not None:
                paths = filledPaths + emptyPaths
 
        elif filledPaths is not None:
            paths = filledPaths

    if args.hd_smoothing :
        print("Reducing hd factor...")
        paths = np.divide(paths, hdPrecisionFactor)

    if args.filtering :
        print("Filtering paths ...")
        paths = applyLowPassFilterToPaths(paths)

    paths = np.multiply(paths, scaleCorrectionFactor)

    print("Exporting to "+outputName+".gcode")
    exportPathsToGcodeFile( paths, 'output/'+outputName+'.gcode')

    print("Exporting to "+outputName+".svg")
    exportPathsToSVGFile( paths, 'output/'+outputName+'.svg', widthInmm, heightInmm)

    print("Done !!")
