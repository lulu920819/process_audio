import csv
import os
for fold in range(1,5,1):
    evaluation_data = []
    with open( ('meta.txt'), 'rt') as f:

        for row in csv.reader(f, delimiter='\t'):
            if len(row) == 2:
                # Scene meta
                orifilename = os.path.splitext(row[0])[0]
                for segid in range (0,15,1):
                    newfile = orifilename + '_' +str(segid) + '.wav'
                    evaluation_data.append((newfile, row[1]))

    with open (('segmeta.txt'),'wt') as f:
    #with open(current_segtrain_file, 'wt') as f:
        writer = csv.writer(f, delimiter='\t')
        for seg_item in evaluation_data:
            writer.writerow(seg_item)