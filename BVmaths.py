import nibabel as nib
import numpy as np
import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def add_extension_if_needed(filename):
    if not filename.lower().endswith('.nii.gz'):
        return filename + '.nii.gz'
    return filename

def apply_operation(data, operation, operand=None):
    if operation == '-mul':
        return data * operand
    elif operation == '-div':
        return data / operand
    elif operation == '-add':
        return data + operand
    elif operation == '-sub':
        return data - operand
    elif operation == '-bin':
        return np.where(data > 0, 1, 0)
    elif operation == '-thr':
        return np.where(data > operand, data, 0)
    elif operation == '-uthr':
        return np.where(data < operand, data, 0)
    else:
        raise ValueError(f"Invalid operation specified: {operation}")

def process_nifti(input_file_path, operations, output_file_path):
    img = nib.load(input_file_path)
    data = img.get_fdata()

    for operation, operand in operations:
        if operand is not None and not is_number(operand):
            operand = add_extension_if_needed(operand)
            operand_value = nib.load(operand).get_fdata()
        elif operand is not None:
            operand_value = float(operand)
        else:
            operand_value = None
        data = apply_operation(data, operation, operand_value)

    result_img = nib.Nifti1Image(data, img.affine)
    nib.save(result_img, output_file_path)

def display_help():
    help_text = """
    Usage: python BVmaths.py <image> [operations and inputs] <out>

    The '.nii.gz' extension is automatically added to filenames if not provided.

    Operations:
    -mul   : Multiply by following input (image or number)
    -div   : Divide by following input (image or number)
    -add   : Add following input (image or number)
    -sub   : Subtract following input (image or number)
    -bin   : Binarize image (set all voxels >0 to 1)
    -thr   : Threshold image (zero voxels below following number)
    -uthr  : Upper threshold (zero voxels above following number)

    Example:
    python BVmaths.py image1 -mul image2 -add 5 -bin out
    python BVmaths.py image1 -thr 2.0 -uthr 3.5 -bin out
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        display_help()
        sys.exit(0)

    if len(sys.argv) < 3:
        print("Invalid usage. For help, use: python BVmaths.py -h")
        sys.exit(1)

    input_file = add_extension_if_needed(sys.argv[1])
    output_file = add_extension_if_needed(sys.argv[-1])
    operation_args = sys.argv[2:-1]

    # Pair up the operations with their operands
    operations = []
    i = 0
    while i < len(operation_args):
        operation = operation_args[i]
        operand = None
        if i + 1 < len(operation_args) and not operation_args[i + 1].startswith('-'):
            operand = operation_args[i + 1]
            i += 1
        operations.append((operation, operand))
        i += 1

    process_nifti(input_file, operations, output_file)
