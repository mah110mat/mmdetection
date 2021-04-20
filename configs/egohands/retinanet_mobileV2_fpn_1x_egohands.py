_base_ = [
    '../mobilenet_backbone/retinanet_mobileV2_fpn.py',
    '../egohands/egohands_dataset.py',
    '../_base_/schedules/schedule_1x.py', 
    '../_base_/default_runtime.py'
]
# optimizer
optimizer = dict(type='SGD', lr=0.0001, momentum=0.9, weight_decay=0.0001)

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])