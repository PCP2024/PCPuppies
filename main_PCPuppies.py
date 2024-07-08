import sys
from processing.processing_fun import *
from dataio.loading_fun import *
from dataio.saving_fun import *
from analyze.analysis_fun import *
from analyze.dogbreed_fun import *

import argparse

def process_arguments():
    #Create parser and add all arguments
    parser = argparse.ArgumentParser() 
    parser.add_argument('-v', '--version', action='store_true', help='show program version')
    parser.add_argument('-i', '--input_path', type=str, help='Path to retreive input image.')
    parser.add_argument('-o', '--output_path', type=str, help='Path to store output image.')
    parser.add_argument('--rotate', type=float, metavar='ANGLE', help='Rotates image given input ANGLE.')
    parser.add_argument('--mirror', action='store_true', help='Mirrors the image.')
    parser.add_argument('--blur', action='store_true', help='Blurs the image.')
    parser.add_argument('--edge_enhance', action='store_true', help='Enhances edges in the image.')
    parser.add_argument('--find_edges', action='store_true', help='Finds eges in the image.')
    parser.add_argument('--smooth', action='store_true', help='Makes image smoother.')
    parser.add_argument('--invert', action='store_true', help='Inverts image.')
    parser.add_argument('--autocontrast', type=float, metavar='THRESH', help='Applies autocontrast in image given input THRESHOLD')
    parser.add_argument('--get_breed', action='store_true', help='Calls classifier to predict dog breed.')

    #Check if user wants to retrieve program version
    args = parser.parse_args()
    if args.version: 
        with open('VERSION', 'r') as file:
            v = file.read()
            print(f"PC Puppies version {v}")
            sys.exit(0)

    #Otherwise, process given parameters
    else:
        args_dict = vars(args)
        given_args = {}
        for arg in args_dict.keys():
            given_args[arg] = False if args_dict[arg] == None or  vars(args)[arg] == False else True
        if not (given_args['input_path'] and given_args['output_path']):
            print("ERROR: Please enter input_path and output_path")
        else:
            image_input = load_image_as_PILimage(args.input_path)
            if given_args['rotate']:
                image_processed = rotate(image_input, args_dict['rotate'])
            elif given_args['mirror']:
                image_processed = mirror(image_input)
            elif given_args['blur']:
                image_processed = blur(image_input)
            elif given_args['edge_enhance']:
                image_processed = edge_enhance(image_input)
            elif given_args['find_edges']:
                image_processed = find_edges(image_input)
            elif given_args['smooth']:
                image_processed = smooth(image_input)
            elif given_args['invert']:
                image_processed = invert(image_input)
            elif given_args['autocontrast']:
                image_processed = apply_threshold(image_input, args_dict['autocontrast'])
            elif given_args['get_breed']:
                print('Breed is:', classify_dogbreed(args.input_path)[0])
            else:
                print("ERROR: Please enter a valid processing function")
            if not given_args['get_breed']:
                saveImage(image_processed, args.output_path)

if __name__ == '__main__':
    process_arguments()