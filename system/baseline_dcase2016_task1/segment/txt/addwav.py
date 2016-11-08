import csv
import os
for fold in range(1,5,1):
    evaluation_data = []
    with open( ('segfold' + str(fold) + '_test.txt'), 'rt') as f:

        for row in csv.reader(f, delimiter='\t'):
            if len(row) == 2:
                # Scene meta
                orifilename = os.path.splitext(row[0])[0]

                newfile = orifilename + '.wav'
                evaluation_data.append((newfile, row[1]))

    with open (('fold'+str(fold) + '_test.txt'),'wt') as f:
    #with open(current_segtrain_file, 'wt') as f:
        writer = csv.writer(f, delimiter='\t')
        for seg_item in evaluation_data:
            writer.writerow(seg_item)