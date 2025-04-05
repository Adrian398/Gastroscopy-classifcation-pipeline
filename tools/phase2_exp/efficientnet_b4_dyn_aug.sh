#!/bin/bash

cd ..

python train.py ../config/phase2/efficientnet_b4_dyn_aug.py --work-dir ../work_dirs/phase2/efficientnet_b4/dyn_aug/lr_decr/

python train.py ../config/phase2/efficientnet_b4_dyn_aug.py --lr 0.01 --work-dir ../work_dirs/phase2/efficientnet_b4/dyn_aug/lr_0.01/

python train.py ../config/phase2/efficientnet_b4_dyn_aug.py --lr 0.001 --work-dir ../work_dirs/phase2/efficientnet_b4/dyn_aug/lr_0.001/


