_base_ = [
        '../../model/swin_pretrained_relative_loc_128.py',
        '../../data/phase4/bepn8_128.py',
        '../../schedule/sgd_decr.py',
        '../../runtime/default.py'
        ]

load_from = None
resume = False
