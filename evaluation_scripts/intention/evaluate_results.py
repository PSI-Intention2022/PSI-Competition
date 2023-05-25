import json
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report, accuracy_score, f1_score
import numpy as np
import os

def evaluate_intent(groundtruth='', prediction='', args=None):
    with open(groundtruth, 'r') as f:
        gt_intent = json.load(f)

    with open(prediction, 'r') as f:
        pred_intent = json.load(f)

    gt = []
    pred = []
    for vid in gt_intent.keys():
        for pid in gt_intent[vid].keys():
            for fid in gt_intent[vid][pid].keys():
                gt.append(gt_intent[vid][pid][fid]['intent'])
                pred.append(pred_intent[vid][pid][fid]['intent_pred'])
    gt = np.array(gt)
    pred = np.array(pred)
    res = measure_intent_prediction(gt, pred, args)
    print('Acc: ', res['Acc'])
    print('F1: ', res['F1'])
    print('mAcc: ', res['mAcc'])
    print('ConfusionMatrix: ', res['ConfusionMatrix'])
    return res['F1']



def measure_intent_prediction(target, prediction, args):
    print("Evaluating Intent ...")
    results = {
        'Acc': 0,
        'F1': 0,
        'mAcc': 0,
        'ConfusionMatrix': [[]],
    }

    bs = target.shape[0]
    lbl_target = target # bs
    lbl_pred = np.round(prediction) # bs, use 0.5 as threshold

    # hard label evaluation - acc, f1
    Acc = accuracy_score(lbl_target, lbl_pred) # calculate acc for all samples
    F1_score = f1_score(lbl_target, lbl_pred, average='macro')

    intent_matrix = confusion_matrix(lbl_target, lbl_pred)  # [2 x 2]
    intent_cls_acc = np.array(intent_matrix.diagonal() / intent_matrix.sum(axis=-1)) # 2
    intent_cls_mean_acc = intent_cls_acc.mean(axis=0)

    # results['MSE'] = MSE
    results['Acc'] = Acc
    results['F1'] = F1_score
    results['mAcc'] = intent_cls_mean_acc
    results['ConfusionMatrix'] = intent_matrix
    return results


if __name__ == '__main__':
    args = None
    # evaluate_intent('gt.json', 'pred.json', args)
    test_gt_file = './val_intent_gt.json'
    test_pred_file = './val_intent_prediction.json'
    score = evaluate_intent(test_gt_file, test_pred_file, args)
    
    ROOT_PATH = os.getcwd()
    ################################
    # the scores for the leaderboard must be in a file named "scores.txt"
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    with open(os.path.join(ROOT_PATH, "output", 'scores.txt'), 'w') as score_file:
#         for key, ap in ap_dictionary.items():
#             score_file.write("%s:%f\n"%(key, ap*100))
#         score_file.write("mAP:%f\n"%(mAP*100))
        score_file.write("F1:%f\n"%(score))
    ################################
    print("Rankding score is : ", score)
