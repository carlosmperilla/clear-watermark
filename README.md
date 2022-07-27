# Clear Watermark

It allows you to insert one image into another and make the respective edits to make it a presentable watermark.

- Easy positioning, by means of a tuple.
- Percentage watermark resizing.
- Percent opacity.
- Optional grayscale for the watermark.
- Support for multiple color models.
- Cross-platform compatibility.

### Dependencies
Budget System requires three external dependencies.
- [Pillow][pillow install]
 This allows us to handle image editing.

### Instalation
```sh
pip install clear-watermark
```

## Index
* [Pre-requirements](https://github.com/carlosmperilla/clear-watermark#pre-requirements)
* [Usage example](https://github.com/carlosmperilla/clear-watermark#usage-example)
    * [Black and white](https://github.com/carlosmperilla/clear-watermark#black-and-white)
    * [Preserving the color](https://github.com/carlosmperilla/clear-watermark#preserving-the-color)
    * [Default jpg simplified](https://github.com/carlosmperilla/clear-watermark#default-jpg-simplified)
    * [Additional Notes](https://github.com/carlosmperilla/clear-watermark#additional-notes)
* [License](https://github.com/carlosmperilla/clear-watermark#license)

## Pre-requirements
* An image to put the watermark on.

<img src="https://github.com/carlosmperilla/clear-watermark/blob/main/example_imgs/summer_beach.jpg" alt="summer beach" width="400"/>

* An image for watermark (Clear Watermark allows you to resize the image, reduce its size, but not increase it because it reduces the quality of the image).

<img src="https://github.com/carlosmperilla/clear-watermark/blob/main/example_imgs/party_logo.png" alt="party logo" width="400"/>

## Usage example
### Black and white

<img src="https://github.com/carlosmperilla/clear-watermark/blob/main/example_imgs/summer_beach_with_watermark_byn.jpg" alt="Black and White watermark" width="400"/>

* We insert the watermark at **25% (from left to right)** of the width of the base image and **75% (from top to bottom)**.
* With **40% opacity**.
* We **reduce the watermark** image to **half** its original size (**50%**).
    * **n_percentage** It is the variable that handles this attribute. 
* We convert the watermark to **black and white**.
* We convert the base image to **RGB** color mode.
* We **display** it **without closing** the inner image object.
* And we **save it** (the internal object of the image is **closed by default**)
```python
from clear_watermark import ImgWithWatermark

img_path_src = 'images/summer_beach.jpg'
img_path_dest = 'images/branding/summer_beach_with_watermark.jpg'
watermark_path_src = 'images/logotipes/party_logo.png'

img_with_watermark = ImgWithWatermark(
                    img_path_src, 
                    watermark_path_src, 
                    pos=(25, 75), 
                    opacity=40, 
                    n_percentage=50, 
                    gray_mode=True, 
                    final_color_model="RGB"
                    )
img_with_watermark.show(close=False)
img_with_watermark.save(img_path_dest)
```
### Preserving the color

<img src="https://github.com/carlosmperilla/clear-watermark/blob/main/example_imgs/summer_beach_with_watermark_color.jpg" alt="Color watermark" width="400"/>

* The same as the previous example, but without **gray_mode.**
```python
from clear_watermark import ImgWithWatermark

img_path_src = 'images/summer_beach.jpg'
img_path_dest = 'images/branding/summer_beach_with_watermark.jpg'
watermark_path_src = 'images/logotipes/party_logo.png'

img_with_watermark = ImgWithWatermark(
                    img_path_src, 
                    watermark_path_src, 
                    pos=(25, 75), 
                    opacity=40,
                    n_percentage=50,
                    final_color_model="RGB"
                    )
img_with_watermark.show(close=False)
img_with_watermark.save(img_path_dest)
```
### Default jpg simplified
* Same as the previous example, but without explicit declarations.
```python
from clear_watermark import ImgWithWatermark

img_path_src = 'images/summer_beach.jpg'
img_path_dest = 'images/branding/summer_beach_with_watermark.jpg'
watermark_path_src = 'images/logotipes/party_logo.png'

img_with_watermark = ImgWithWatermark(
                        img_path_src, watermark_path_src, 
                        (25, 75), 40, 50
                        )
img_with_watermark.show(close=False)
img_with_watermark.save(img_path_dest)
```
### Additional Notes
* The **close argument**, available for both the **.show** and **.save** methods, defaults to **True**, but if you **don't want the internal image to close**, you must specify **close=False**.
* If you want the image to retain some kind of transparency, you should use **final_color_mode="RGBA"**.
* The default watermark **retains its color**, when activating the gray mode, with **gray_mode=True**, it not only changes to black and white, it also **adds brightness** to stand out despite the transparency.

## License

MIT License

Copyright (c) 2022 Carlos Perilla Budget System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


[pillow install]: https://pypi.org/project/Pillow/
