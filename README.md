# PSI-Competition
This folder contains scripts for the PSI competition. 


## 1. Results evaluation scripts

### (1) Intention
```python
python evaluate_results.py
```
The evaluation ranking score is the F1-score of intention binary prediction.

Example intention ground-truth/prediction JSON format:
```
# Ground-truth
video_name: {
    pedestrian_ID: {
        frame_ID: {
            intent: int # 0-not cross, 1-crossing
        }
    }
}
# Intent Prediction
video_name: {
    pedestrian_ID: {
        frame_ID: {
            intent_pred: int, # 0-not cross, 1-crossing
            intent_pred_prob: float
        }
    }
}
```

### (2) Trajectory

```python
python evaluate_results.py
```
The evaluation ranking score is the average ADE of predicted trajectory over ['0.5s', '1.0s', '1.5s'] time steps.

Example trajectory ground-truth/prediction JSON format:
```
# Trajectory Prediction
video_name: {
    pedestrian_ID: {
        frame_ID: {
            traj_gt/traj_pred: {
                0: [xtl, ytl, xbr, ybr],
                1: [xtl, ytl, xbr, ybr],
                2: [xtl, ytl, xbr, ybr],
                ...
            }
        }
    }
}
```


### (3) Driving Decision


## 2. Baselines

### (1) Intention

### (2) Trajectory

### (3) Driving Decision

## 3. Other ...