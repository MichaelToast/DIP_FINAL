# Motion Blur: 
Motion blur can be a very costly for the loss of data, and it can be difficult to locate extensive datasets with a controlled set and amount of motion blur for model training. In addition, motion blur can also be hard to quantify and describe, and important aspect for motion blur correction. 
We need to create a way to simulate controlled motion blur for usage in our systems that we can use to create data for experimentation of quantification and correction techniques.

## Data Sets: 
Text: 
https://www.kaggle.com/datasets/anggadwisunarto/text-deblurring-dataset-with-psf-for-ocr

Circle: 
https://www.kaggle.com/datasets/nonsakhoo/directional-motion-blur-minimal-v1?select=MADE_minimal_dataset

### Set Up: 
env_variables.py - Enviornment variables for where to get the input and output images, and what datasets to use. 

#### Static Michaelsons Contrast
Used or motion blur to calculate contrast lost. (Modilation Transfer) = C_blurred/C_static
- A value near 1.0 means almost no contrast was lost
- A value approaching 0 means the motion blure completely washed out the pattern
Take pictures of the "Moving" image and measure the drop in Michelson contrast

Problems:
- np.max and n.min will grab the single brightest and darkest pixels. 
- Large uniform areas will survive the motion blur
Solution:
- Measure l_max and l_min locally across the periodic patterns. (Where the bar width is smaller than or comparable to the blur length)
- **Crop to a high drequency Region** . Slice the image to include only the fine bars whose width is smaller than the motion blur length, and take the mean across the perpendicular axis to supress pixel noise. 

#### Fast Fourier Transform
Michelson contrast is not defined globally (aka for images without neat stripes).
measure the drop in high frequenct amplitude with a 2d Fast Fourier Transform. Mathmatical equivalent of MTF across all spatial frequencies.
