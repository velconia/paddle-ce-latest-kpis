import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import AccKpi

flowers_resnet50_dist_train_acc_kpi = AccKpi('flowers_resnet50_dist_train_acc', 0.323588, 0, actived=True)
flowers_resnet50_dist_train_speed_kpi = AccKpi('flowers_resnet50_dist_train_speed', 93.94776, 0, actived=True)

tracking_kpis = [
    flowers_resnet50_dist_train_speed_kpi,
    flowers_resnet50_dist_train_acc_kpi,
]
