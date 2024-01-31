
# BVmaths

BVmaths is a Python utility for performing arithmetic and thresholding operations on NIFTI (.nii.gz) files, similar to the functionality offered by FSL's `fslmaths` tool.

One advantage is that it runs directoly on python using only numpy and nibabel libraries, and can therefore be run on Windows easily.

## Features

- Supports of operations such as addition, subtraction, multiplication, division, binarization, thresholding, and upper thresholding.
- Automatically appends `.nii.gz` extension to filenames if not provided.
- Command-line interface for easy integration into processing pipelines.

## Installation

To use BVmaths, you only need to have a working `Python` with `nibabel` and `numpy` libraries available.  

However, if you also plan on using the rest of our [BV-RADS tools](https://github.com/BV-RADS/BV-BIDS), we recommend installing the full environment with the necessary libraries: 

You will need to have Conda installed. You can use either Anaconda or Miniconda.

### Step 1: Install Conda

Download and install [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Step 2: Clone the Repository

Clone the BVmaths repository from GitHub:

```
git clone https://github.com/BV-RADS/BV-Maths.git
```

### Step 3: Create and Activate Conda Environment

Navigate to the cloned repository and create a Conda environment using the `environment.yml` file:

```
cd BV-Maths
conda env create -f environment.yml
```

Once the environment is created, activate it:

```
conda activate BV-RADS
```

## Usage

To use BVmaths, run the script with the desired operation and operands. 

```
    Usage: python BVmaths.py <image.nii.gz> [operations and inputs] <out.nii.gz>

    Operations:
    -mul   : Multiply by following input (image or number)
    -div   : Divide by following input (image or number)
    -add   : Add following input (image or number)
    -sub   : Subtract following input (image or number)
    -bin   : Binarize image (set all voxels >0 to 1)
    -thr   : Threshold image (zero voxels below following number)
    -uthr  : Upper threshold (zero voxels above following number)

    Example:
    python BVmaths.py image1.nii.gz -mul image2.nii.gz -add 5 -bin out.nii.gz
    python BVmaths.py image1.nii.gz -thr 2.0 -uthr 3.5 -bin out.nii.gz

For detailed usage instructions, run:

python BVmaths.py -h
```
