#!/usr/bin/env python3
#
# The script is used for downloading the three datasets used by the examples.
#
# All three datasets come from LIBSVM website, and are stored in LIBSVM format.
# For more details, please refer to the following link:
# https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html
#
# Besides, all three datasets are for binary classification, since most of the
# state-of-the-arts active learning algorithms (query strategies) are only
# suitable for binary classification.
#
# The following table describes some informations about
# the three datasets: australian, diabetes, and heart.
#
# +------------+-----+----+
# |   dataset  |  N  |  D |
# +============+=====+====+
# | australian | 690 | 14 |
# +------------+-----+----+
# |  diabetes  | 768 |  8 |
# +------------+-----+----+
# |    heart   | 270 | 13 |
# +------------+-----+----+
#
# N is the number of samples, and D is the dimension of the input feature.
# labels y \in {-1, +1}

import os
import urllib.request
import random

DATASETS = [
    {
        'name': 'australian',
        'url': 'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/australian_scale',
        'size': 690,
    },
    {
        'name': 'diabetes',
        'url': 'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/diabetes_scale',
        'size': 768,
    },
    {
        'name': 'heart',
        'url': 'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/heart_scale',
        'size': 270,
    },
]

TARGET_PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    for dataset in DATASETS:
        print('downloading {} ... '.format(dataset['name']))
        rows = list(urllib.request.urlopen(dataset['url']))
        selected = random.sample(rows, dataset['size'])
        with open(os.path.join(TARGET_PATH, '{}.txt'.format(dataset['name'])), 'wb') as f:
            for row in selected:
                f.write(row)
        print('{} downloaded successfully !\n'.format(dataset['name']))

    print('All datasets have been downloaded!')


if __name__ == '__main__':
    main()
