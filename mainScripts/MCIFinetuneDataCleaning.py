from os.path import join
from collections import defaultdict

# Data pipeline to prepare subjects used for model finetuning with MCI -> AD progression

READ_DIR = '/home/ec2-user/mnt/home/ec2-user/alzstudy/AlzheimerData/'


# return the list of subjects that satisfy our criteria for finetuning
def find_mci_subjects(img_dir=READ_DIR + 'ADNI_CAPS', idx_fold=0):
    subjects_to_labels = defaultdict(list) # subject: [label]


    csv_path = join(img_dir, f'split.pretrained.{idx_fold}.csv')
    text = [line.strip() for line in open(csv_path)]

    for line in text[1:]:
        items = line.split(',')

        split = items[-1]
        csv_label = items[-2]
        subject = items[0]
        session = items[1]
        subjects_to_labels[subject].append(f'split: {split} session:{session} label: {csv_label}')

    print(subjects_to_labels)


find_mci_subjects()

