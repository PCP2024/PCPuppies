import sys
from processing.processing_fun import *
from dataio.loading_fun import *
from dataio.saving_fun import *
from analyze.analysis_fun import *
import argparse

parser =  argparse.ArgumentParser(description="first cli")

def run_command(image_path, function, output_path, **options):

    # Load the data    
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

if __name__ == '__main__':

    if len(sys.argv) == 2:
        parser.add_argument('-v', '--version', type=int, help='version of program', default=0)
        args = parser.parse_args()
        if args.version:
            # print VERSION file that is in this directory
            with open('VERSION', 'r') as file:
                print(file.read())
        else:
            print("Please enter a valid argument")
    else:
        parser.add_argument('image_path', type=str, help='path to image')
        parser.add_argument('function', type=str, help='processing function to apply to the image')
        parser.add_argument('output_path', type=str, help='path to save the image')
        parser.add_argument('-a', '--angle', type=int, help='angle to rotate the image', default=0)
        parser.add_argument('-t', '--threshold', type=int, help='threshold to apply to the image', default=0)
        args = parser.parse_args()
        run_command(**vars(args))