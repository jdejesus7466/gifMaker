# GIF Generator

This script creates an animated GIF from a set of images using the `imageio.v3` library.

## How It Works
- The script reads multiple images from a predefined list of filenames.
- It combines them into a GIF with a set frame duration and infinite looping.
- The final GIF is saved as `kiryu.gif`.

## Getting Started
### Prerequisites
Make sure you have `imageio` installed. If you don’t have it yet, install it with:

```bash
pip3 install imageio
```

### Running the Script
1. Place your images (`kiryu1.jpg`, `kiryu2.jpg`, `kiryu3.jpg`, `kiryu4.jpg`, `kiryu5.jpg`) in the same directory as the script.
2. Run the script with:

```bash
python create_gif.py
```

3. The script will generate `kiryu.gif` in the same directory.

## Customization
- Modify the `filenames` list to use different images (The more images there are, the more smooth the gif will be).
- Adjust the `duration` value (in milliseconds) to speed up or slow down the animation.
- Change the `loop` setting (`0` for infinite loops, or set a specific number).

## What You Get
At the end, you’ll have an animated GIF named `kiryu.gif` that cycles through your images. This image name can also be changed in the code.

## Author
Joseph De Jesus
