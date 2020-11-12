
import os
import sys
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True, type=str)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--split_ratio', default=0.95, type=float)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    with open(args.output_dir, 'w', encoding='utf-8') as fp:
        for line in open(args.input_dir).readlines():
            img = os.path.basename(line.strip().split('\t')[0])
            fp.write(img)
            fp.write('\n')
