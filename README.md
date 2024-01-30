
# BVmaths

BVmaths is a Python utility for performing arithmetic and thresholding operations on NIFTI (.nii.gz) files, similar to the functionality offered by FSL's `fslmaths` tool.

One advantage is that it runs directoly on python using only numpy and nibabel libraries, and can therefore be run on Windows easily.

## Features

- Supports of operations such as addition, subtraction, multiplication, division, binarization, thresholding, and upper thresholding.
- Automatically appends `.nii.gz` extension to filenames if not provided.
- Command-line interface for easy integration into processing pipelines.

## Installation

To use BVmaths, you will need to have Conda installed. You can use either Anaconda or Miniconda.

### Step 1: Install Conda

Download and install [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Step 2: Clone the Repository

Clone the BVmaths repository from GitHub:

```
git clone https://github.com/BV-RADS/BVmaths.git
```

### Step 3: Create and Activate Conda Environment

Navigate to the cloned repository and create a Conda environment using the `environment.yml` file:

```
cd BVmaths
conda env create -f environment.yml
```

Once the environment is created, activate it:

```
conda activate BV-RADS
```

## Usage

To use BVmaths, run the script with the desired operation and operands. Here are some examples:

```
python BVmaths.py inputImage -mul 2 outputImage
python BVmaths.py inputImage -thr 2.0 -uthr 3.5 -bin outputImage
```

For detailed usage instructions, run:

```
python BVmaths.py -h
```
