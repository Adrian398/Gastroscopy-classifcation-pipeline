_base_ = [
        '../../model/resnet50.py',
        '../../data/phase1/bepn32.py',
        '../../schedule/sgd_decr.py',
        '../../runtime/default.py'
]

load_from = None
resume = False

