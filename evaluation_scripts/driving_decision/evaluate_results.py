import json
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report, accuracy_score, f1_score
import numpy as np


def evaluate_driving(groundtruth='', prediction='', args=None):
    with open(groundtruth, 'r') as f:
        gt_driving = json.load(f)

    with open(prediction, 'r') as f:
        pred_driving = json.load(f)

    gt_speed = []
    gt_dir = []
    speed_pred = []
    dir_pred = []

    for vid in pred_driving.keys():
        for fid in pred_driving[vid].keys():
            speed_pred.append(pred_driving[vid][fid]['speed'])
            dir_pred.append(pred_driving[vid][fid]['direction'])
            gt_speed.append(gt_driving[vid][fid]['speed'])
            gt_dir.append(gt_driving[vid][fid]['direction'])

    gt_speed = np.array(gt_speed)
    gt_dir = np.array(gt_dir)
    speed_pred = np.array(speed_pred)
    dir_pred = np.array(dir_pred)

    res = measure_driving_prediction(gt_speed, gt_dir, speed_pred, dir_pred, args)
    for key in ['speed_Acc', 'speed_mAcc', 'direction_Acc', 'direction_mAcc', 'speed_confusion_matrix', 'dir_confusion_matrix']:
        print(key, res[key])

    return (res['speed_mAcc'] + res['direction_mAcc']) / 2



def measure_driving_prediction(gt_speed, gt_dir, speed_pred, dir_pred, args):
    results = {'speed_Acc': 0, 'speed_mAcc': 0, 'direction_Acc': 0, 'direction_mAcc': 0}
    print("Evaluating Driving Decision Prediction ...")

    bs = gt_speed.shape[0]
    results['speed_Acc'] = accuracy_score(gt_speed, speed_pred)
    results['direction_Acc'] = accuracy_score(gt_dir, dir_pred)

    speed_matrix = confusion_matrix(gt_speed, speed_pred)
    results['speed_confusion_matrix'] = speed_matrix
    sum_cnt = speed_matrix.sum(axis=1)
    sum_cnt = np.array([max(1, i) for i in sum_cnt])
    speed_cls_wise_acc = speed_matrix.diagonal() / sum_cnt
    results['speed_mAcc'] = np.mean(speed_cls_wise_acc)

    dir_matrix = confusion_matrix(gt_dir, dir_pred)
    results['dir_confusion_matrix'] = dir_matrix
    sum_cnt = dir_matrix.sum(axis=1)
    sum_cnt = np.array([max(1, i) for i in sum_cnt])
    dir_cls_wise_acc = dir_matrix.diagonal() / sum_cnt
    results['direction_mAcc'] = np.mean(dir_cls_wise_acc)
    # print("dir: ", dir_matrix.diagonal(), sum_cnt, dir_cls_wise_acc, np.mean(dir_cls_wise_acc))
    return results


if __name__ == '__main__':
    args = None
    # Evaluate driving decision prediction
    test_gt_file = './val_driving_gt.json'
    test_pred_file = './val_driving_prediction.json'
    score = evaluate_driving(test_gt_file, test_pred_file, args)
    print("Rankding score is : ", score)