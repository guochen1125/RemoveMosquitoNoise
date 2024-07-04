# RemoveMosquitoNoise
## Algorithm Steps
Should be performed separately for each color channel of YCrCb.
### 1. Calculate the ε matrix
Divide the image into blocks (5×5, 7×7 or 9×9 is recommended) to find the sharp contour areas in the image. Calculate the standard deviation or variance coefficient of the brightness value of each block (variance coefficient = standard deviation of the brightness value of the pixels in the block divided by the average value). Each standard deviation or variance coefficient is the ε value of the ε filter of the corresponding block.
### 2. ε filtering
Apply ε filtering to each pixel in the image. For each pixel in the image, the brightness value is x, extract all the brightness values ​​within the range of x±ε in the block where the pixel is located, calculate their average value as the output y, and form the denoised image.
