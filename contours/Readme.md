# Picture2Gcode

You should use python3 to get a better result. Hd-smoothing option does not works well with python2.7.

## Options

```
--input-path : path to a picture

--image-width-in-mm: allows to set a target width in millimeter.

--hd-smoothing : increase resolution and help getting a better result, should be enbaled.

--tool-diameter-in-mm : used inly when filling shapes.

--fill : choose among 'no-fill', 'fill-in', 'auto-fill':
          'no-fill' : just contours. Input a black and white image.
          'fill-in' : always fill shapes. Input a black and white image.
          'auto-fill' : fill blue-shapes (Red:0, Green:0, Blue>=127).
                        Draw contours of red-shapes (Red>=127, Green:0, Blue:0).
```

## Example

### Example fill

`python3 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill fill-in`

`python2.7 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill fill-in`

**Input :**

![Input Image](https://github.com/eumorpurgo/TextileDrawingMachine/blob/master/contours/src/joker2.jpg "joker Input")

**Output :**

![Output Image](https://github.com/eumorpurgo/TextileDrawingMachine/blob/master/contours/src/jokerfilledsvg.png "joker output filled svg")

### Example contours only

`python3 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill no-fill`

`python2.7 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill no-fill`

**Input :**

![Input Image](https://github.com/heb-dtc/DigitalWaxPrint/blob/master/contours/src/joker2.jpg "joker Input")

**Output :**

Inline-style: 
![Output Image](https://github.com/heb-dtc/DigitalWaxPrint/blob/master/contours/src/jokercontourssvg.png "joker output contours svg")


### Example auto fill

`python3 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill auto-fill`

`python2.7 contours.py --input-path /path/to/input/picture --image-width-in-mm 5000 --hd-smoothing --tool-diameter-in-mm 17 --fill auto-fill`

**Input :**

![Input Image](https://github.com/eumorpurgo/TextileDrawingMachine/blob/master/contours/src/joker2.png "joker Input")

**Output :**

![Output Image](https://github.com/eumorpurgo/TextileDrawingMachine/blob/master/contours/src/jokerautofillsvg.png "joker output auto fill svg")



## TODO

- Adding initial erode
- ~~If Blue-->contours, if Red-->fill~~
- Changing actions in `putToolDown()` and `putToolUp`
