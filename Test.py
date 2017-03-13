from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf 

FLAGS = None


def main(_):
	print("Begin") 


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)