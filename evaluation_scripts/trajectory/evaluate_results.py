import json
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report, accuracy_score, f1_score
import numpy as np

def evaluate_traj(groundtruth='', prediction='', args=None):
    with open(groundtruth, 'r') as f:
        gt_traj = json.load(f)

    with open(prediction, 'r') as f:
        pred_traj = json.load(f)

    gt = []
    pred = []
    for vid in gt_traj.keys():
        for pid in gt_traj[vid].keys():
            for fid in gt_traj[vid][pid].keys():
                gt.append(gt_traj[vid][pid][fid]['traj'])
                pred.append(pred_traj[vid][pid][fid]['traj'])
    gt = np.array(gt)
    pred = np.array(pred)
    traj_results = measure_traj_prediction(gt, pred, args)

    for key in ['ADE', 'FDE', 'ARB', 'FRB']: #, 'Bbox_MSE', 'Bbox_FMSE', 'Center_MSE', 'Center_FMSE']:
        for time in ['0.5', '1.0', '1.5']:
            val = traj_results[key][time]
            print(f'Eval/Results/{key}_{time}', val)

    score = np.mean([traj_results['ADE'][t] for t in ['0.5', '1.0', '1.5']])
    return score

def measure_traj_prediction(target, prediction, args):
    print("Evaluating Trajectory ...")
    target = np.array(target)
    prediction = np.array(prediction)
    assert target.shape[1] == args.predict_length
    assert target.shape[2] == 4  # bbox
    assert prediction.shape[1] == args.predict_length
    assert prediction.shape[2] == 4
    results = {
        'ADE': {'0.5': 0, '1.0': 0, '1.5': 0},  # center
        'FDE': {'0.5': 0, '1.0': 0, '1.5': 0},  # center
        'ARB': {'0.5': 0, '1.0': 0, '1.5': 0},  # bbox - B: bbox
        'FRB': {'0.5': 0, '1.0': 0, '1.5': 0},  # bbox - B: bbox
    }
    bs, ts, _ = target.shape
    # Correct error of calculating RMSE of bbox for ARB and FRB
    # performance_MSE = np.square(target - prediction).sum(axis=2)  # n_samples x ts x 4 --> bs x ts
    performance_MSE = np.square(target - prediction).mean(axis=2)
    performance_RMSE = np.sqrt(performance_MSE)  # bs x ts
    for t in [0.5, 1.0, 1.5]:
        end_frame = int(t * args.fps)
        # 5. ARB - bbox
        results['ARB'][str(t)] = performance_RMSE[:, :end_frame].mean(axis=None)
        # 6. FRB - bbox
        results['FRB'][str(t)] = performance_RMSE[:, end_frame - 1].mean(axis=None)

    # centers
    center_target = np.zeros((bs, ts, 2))
    center_pred = np.zeros((bs, ts, 2))
    for i in range(bs):
        for j in range(ts):
            center_target[i, j, 0] = (target[i, j, 0] + target[i, j, 2]) / 2
            center_target[i, j, 1] = (target[i, j, 1] + target[i, j, 3]) / 2
            center_pred[i, j, 0] = (prediction[i, j, 0] + prediction[i, j, 2]) / 2
            center_pred[i, j, 1] = (prediction[i, j, 1] + prediction[i, j, 3]) / 2

    performance_CMSE = np.square(center_target - center_pred).sum(axis=2)  # bs x ts x 4 --> bs x ts
    performance_CRMSE = np.sqrt(performance_CMSE)  # bs x ts

    for t in [0.5, 1.0, 1.5]:
        end_frame = int(t * args.fps)
        # 7. ADE - center
        results['ADE'][str(t)] = performance_CRMSE[:, : end_frame].mean(axis=None)
        # 8. FDE - center
        results['FDE'][str(t)] = performance_CRMSE[:, end_frame - 1].mean(axis=None)

    return results


if __name__ == '__main__':
    args = None
    # Evaluate driving decision prediction
    test_gt_file = './val_traj_gt.json'
    test_pred_file = './val_traj_prediction.json'
    score = evaluate_traj(test_gt_file, test_pred_file, args)
    print("Rankding score is : ", score)