#!/usr/bin/env python
 
import numpy as np
import matplotlib.pyplot as plt
import string
import sys

from wordcount import load_word_counts

"""
Given a list of (word, count) tuples, plot these as a histogram. Only
the first limit tuples are plotted.
"""
def plot_word_counts(counts, limit = 10):
  plt.title("Word Counts")
  limited_counts = counts[0:limit]
  word_data = [word for (word, count) in limited_counts]
  count_data = [count for (word, count) in limited_counts]
  position = np.arange(len(word_data))
  width = 1.0
  ax = plt.axes()
  ax.set_xticks(position + (width/2))
  ax.set_xticklabels(word_data)
  plt.bar(position, count_data, width, color='b')

if  __name__ =='__main__':
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  limit = 10
  if (len(sys.argv) > 3):
    limit = int(sys.argv[3])
  counts = load_word_counts(input_file)
  plot_word_counts(counts, limit)
  if (output_file == "show"):
    plt.show()
  else:
    plt.savefig(output_file)
