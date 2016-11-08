# !usr/bin/env python
# coding=utf-8

from Tkinter import *
from pydub import AudioSegment
from pydub import playback
from ui import *
import csv
import os
import wave
import matplotlib.pyplot as plt
import numpy as np


def do_segment(dataset, segment_txt, segment_wav , dataset_evaluation_mode='folds'):
    for fold in dataset.folds(mode=dataset_evaluation_mode):
        current_segtrain_file = get_segtraintxt_filename(fold=fold, path=segment_txt)
        current_segtest_file = get_segtest_filename(fold=fold, path=segment_txt)

        filetrain = []
        filetest = []
        for item_id, item in enumerate(dataset.train(fold)):
            if item['file'] not in filetrain:
                # 循环每个文件
                data_path = dataset.absolute_to_relative(item['file'])
                seglist1 = []
                seglist1 = wav_segment(item['file'],data_path,segment_wav,0,2,0,item['scene_label'])
                filetrain.extend(seglist1)
                # print item_id +'done '+ data_path
            # if item_id == 10:
            #         break
            progress(title_text='segmenting train file',fold = fold,
                         note=data_path)

        for item_id, item in enumerate(dataset.test(fold)):
            if item['file'] not in filetest:
                # 用extend
                data_path = dataset.absolute_to_relative(item['file'])
                seglist2 = []
                seglist2 = wav_segment(item['file'],data_path,segment_wav,0,2,0)
                filetest.extend(seglist2)
            # if item_id == 10:
            #         break

            progress(title_text='segmenting test file', fold=fold,
                    note=data_path)

        with open(current_segtrain_file, 'wt') as f:
            writer = csv.writer(f, delimiter='\t')
            for seg_item in filetrain:
                writer.writerow(seg_item)

        with open(current_segtest_file, 'wt') as f:
            writer = csv.writer(f, delimiter='\t')
            for seg_item in filetest:
                writer.writerow(seg_item)

    return


# todo
# file_path is single name
def wav_segment(wavfile, filename, segment_wav, seg_overlap = 0, seg_duration = 2, seg_hop = 0, scene_label=None):
    """Parameter wav_segment.
    segment the file into

        Parameters
        ----------
        file_path : dict or string???
            parameters in dict

        overlap :  int
            each segment has overlap

        segment_length: int
            the duration of the segment

        scene_label: str
            the label of the whole audio

        Returns
        -------
        params : int
            the count of the segmented file

    """

    # check the param
    if seg_overlap < 0 or seg_duration < seg_overlap or seg_hop > 0:
        overlap = 0

    # pydub does things in milliseconds
    seg_duration_ms = seg_duration * 1000
    seg_overlap_ms = seg_overlap *1000
    seg_hop_ms = seg_hop *1000
    # todo
    total_file = AudioSegment.from_wav(wavfile)
    total_duration_ms = len(total_file)
    #print total_file.duration_seconds
    if seg_duration_ms > total_duration_ms:
        return 0


    seglist =[]
    seg_id = 0
    seg_start = 0
    seg_end = seg_duration_ms
    filename_ = os.path.splitext(filename)[0]
    while seg_end <= total_duration_ms:
        # todo 文件名要处理切数据
        newfilename = filename_ + '_' + str(seg_id) + '.wav'
        newfilepath = os.path.join(segment_wav, newfilename)
        segmemt = total_file[seg_start:seg_end]
        #print len(segmemt)
        #print segmemt.duration_seconds
        exportfile = newfilepath + '.wav'
        file_handle = segmemt.export(exportfile, format="wav")
        seg_start = seg_end - seg_overlap_ms
        seg_end = seg_end - seg_overlap_ms + seg_duration_ms + seg_hop_ms
        seg_id = seg_id + 1
        seglist.append((newfilename, scene_label))
    return seglist


def get_segtraintxt_filename(fold, path, extension='txt'):
    """Get result filename

    Parameters
    ----------
    fold : int >= 0
        evaluation fold number

    path :  str
        result path

    extension : str
        file extension
        (Default value='cpickle')

    Returns
    -------
    result_filename : str
        full result filename

    """

    if fold == 0:
        return os.path.join(path, 'seg.' + extension)
    else:
        return os.path.join(path, 'segfold' + str(fold) + '_train.' + extension)

# def main():
#     # wave_data = wav_segment("a001_30_60.wav")
#     wave_data = wav_segment("a001_30_60.wav",1,2,0,"bus")
#
# if __name__ == "__main__":
#     main()

def get_segtest_filename(fold, path, extension='txt'):
    """Get result filename

    Parameters
    ----------
    fold : int >= 0
        evaluation fold number

    path :  str
        result path

    extension : str
        file extension
        (Default value='cpickle')

    Returns
    -------
    result_filename : str
        full result filename

    """

    if fold == 0:
        return os.path.join(path, 'seg.' + extension)
    else:
        return os.path.join(path, 'segfold' + str(fold) + '_test.' + extension)

# def main():
#     # wave_data = wav_segment("a001_30_60.wav")
#     wave_data = wav_segment("a001_30_60.wav",1,2,0,"bus")
#
# if __name__ == "__main__":
#     main()