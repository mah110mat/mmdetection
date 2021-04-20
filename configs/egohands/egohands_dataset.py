_base_ = '../_base_/datasets/coco_detection.py'
data_root = 'data/egohands/'
classes = ('myleft', 'myright', 'yourleft', 'yourright')  # クラスラベル
data = dict(
    train=dict(
        classes=classes,  # COCOデータセットのクラスをオーバーライド
        ann_file=data_root+'annotations/train.json',
        img_prefix=data_root+'train/'),
    val=dict(
        classes=classes,  # COCOデータセットのクラスをオーバーライド
        ann_file=data_root+'annotations/valid.json',
        img_prefix=data_root+'valid/'),
    test=dict(
        classes=classes,  # COCOデータセットのクラスをオーバーライド
        ann_file=data_root+'annotations/test.json',
        img_prefix=data_root+'test/')
)