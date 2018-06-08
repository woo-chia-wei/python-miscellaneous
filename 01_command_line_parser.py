import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--dir', type = str, default = 'pet_images/', 
                    help = 'Path to the pet image files') 

parser.add_argument('--arch', type = str, default = 'vgg', 
                    help = 'CNN model architecture to use for image classification')

parser.add_argument('--dogfile', type = str, default = 'dognames.txt', 
                    help = 'Text file that contains all labels associated to dogs')

in_args = parser.parse_args()

print("	Argument 1:", in_args.dir, "\n", "	Argument 2:", in_args.arch,  "\n", "	Argument 3:", in_args.dogfile)