import sys
from processing.processing_fun import *
from dataio.loading_fun import *
from dataio.saving_fun import *
from analyze.analysis_fun import *
import argparse

def main():
    parser =  argparse.ArgumentParser(description="first cli")

    parser.add_argument('image_path', type=str, help='path to image')
    parser.add_argument('function', type=str, help='processing function to apply to the image')
    parser.add_argument('output_path', type=str, help='path to save the image')
    parser.add_argument('angle', type=int, help='angle to rotate the image')
    parser.add_argument('threshold', type=int, help='threshold to apply to the image')

    # Load the data
    args = parser.parse_args()
    image_input = load_image_as_PILimage(args.image_path)

    # Process the data
    if args.function == 'rotate':
        image_processed = rotate(image_input, args.angle)
    elif args.function == 'mirror':
        image_processed = mirror(image_input)
    elif args.function == 'blur':
        image_processed = blur(image_input)
    elif args.function == 'edge_enhance':
        image_processed = edge_enhance(image_input)
    elif args.function == 'find_edges':
        image_processed = find_edges(image_input)
    elif args.function == 'smooth':
        image_processed = smooth(image_input)
    elif args.function == 'invert':
        image_processed = invert(image_input)
    elif args.function == 'apply_threshold':
        image_processed = apply_threshold(image_input, args.threshold)
    else:
        print("ERROR: Please enter a valid processing function")

    saveImage(image_processed, args.output_path)

# TODO - version, optional arguments, --?????

if __name__ == '__main__':
    main()
