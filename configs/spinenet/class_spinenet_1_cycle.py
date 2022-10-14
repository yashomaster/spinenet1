# The new config inherits a base config to highlight the necessary modification
_base_ = 'spinenet_1_cycle.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=52),
        mask_head=dict(num_classes=52)))

# Modify dataset related settings
dataset_type = 'CocoDataset',
classes = ('WO-01', 'WO-11', 'WO-17', 'WO-23', 'SO-02', 
'SO-03', 'SO-09', 'SO-11', 'SO-12', 'SO-21', 'SO-24', 'SO-27',
'SO-30', 'SO-32', 'SO-34', 'SO-35', 'SO-36', 'SO-37', 'SO-38',
'SO-40', 'SO-41', 'SO-42', 'SO-44', 'SO-45', 'SO-46', 'SO-47',
'DO-01', 'DO-04', 'DO-06', 'Y-01', 'Y-11', 'Y-12', 'Y-13', 'Y-14',
'Y-32', 'Y-33', 'Y-35', 'Y-37', 'Y-44', 'N-11', 'N-12',
'N-13', 'N-28', 'N-32', 'N-33', 'N-34', 'N-37', 'N-38',
'C-02', 'C-04', 'WO-07', 'SO-23')
data = dict(
    train=dict(
        img_prefix='D:/2022_NIA_project/mmdetection/data/1_cycle/training/',
        classes=classes,
        ann_file='D:/2022_NIA_project/mmdetection/data/1_cycle/annotations/ContilTrain.json'),
    val=dict(
        img_prefix='D:/2022_NIA_project/mmdetection/data/1_cycle/validation/',
        classes=classes,
        ann_file='D:/2022_NIA_project/mmdetection/data/1_cycle/annotations/ContilValidation.json'),
    test=dict(
        img_prefix='D:/2022_NIA_project/mmdetection/data/1_cycle/test/',
        classes=classes,
        ann_file='D:/2022_NIA_project/mmdetection/data/1_cycle/annotations/ContilTest.json'))
   
    

    
