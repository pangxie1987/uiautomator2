'''
argparse练习
https://www.jianshu.com/p/a50aead61319
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose',  help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")