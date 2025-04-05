#construct dataloader and evaluator
dataset_type = 'CustomDataset'
data_preprocessor = dict(
    # Input image data channels in 'RGB' order
    mean=[143.14, 79.59, 58.27],
    std=[68.06, 53.97, 41.29],
    to_rgb=True,
)

train_pipeline = [
    dict(type='LoadImageFromFile'),     # read image
    dict(type='Resize', scale=(640, 640), interpolation='bicubic'),
    dict(type='PackInputs'),         # prepare images and labels
]

test_pipeline = [
    dict(type='LoadImageFromFile'),     # read image
    dict(type='Resize', scale=(640, 640), interpolation='bicubic'),
    dict(type='PackInputs'),                 # prepare images and labels
]

train_dataloader = dict(
    batch_size=8,
    num_workers=5,
    dataset=dict(
        type=dataset_type,
        data_root='../../SUN',
        ann_file='meta/train.txt',
        data_prefix='train',
        with_label=True,
        classes=['negative', 'positive'],
        pipeline=train_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=True),
    persistent_workers=True,
)

val_dataloader = dict(
    batch_size=8,
    num_workers=5,
    dataset=dict(
        type=dataset_type,
        data_root='../../SUN',
        ann_file='meta/val.txt',
        data_prefix='val',
        with_label=True,
        classes=['negative', 'positive'],
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
    persistent_workers=True,
)
val_evaluator = [
        dict(type='Accuracy', topk=(1)),
        dict(type='SingleLabelMetric', items=['precision', 'recall', 'f1-score'], average=None)
                ]

test_dataloader = val_dataloader
test_evaluator = val_evaluator

