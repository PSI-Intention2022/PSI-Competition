# PSI Pedestrian & Driver Behavior Estimation Challenge - [IEEE ITSC 2023](https://2023.ieee-itsc.org/)

WE are hosting the Pedestrian & Driver Behavior Estimation Challenge based on the [Pedestrian Situated Intent (PSI) 2.0](ttps://github.com/PSI-Intention2022/PSI2) dataset. 

The challenge has three tracks, including [Pedestrian Intent Prediction (PIP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-PIP), [Pedestrian Trajectory Prediction (PTP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-PTP), and [Driver Decision Prediction (DDP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-DDP), during pedestrian encounters. 


## 1. Participation
(Information about platform ...)

## 2. Overview
(Introduction about the challenge ...)

## 3. Challenge Tracks

***Track 1 (Pedestrian Intent): [Pedestrian Intent Prediction (PIP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-PIP)***

***Track 2 (Pedestrian Trajectory): [Pedestrian Trajectory Prediction (PTP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-PTP)***

***Track 3 (Driver Decision): [Driver Decision Prediction (DDP)](https://github.com/PSI-Intention2022/ITSC2023-PSI-DDP)***

## 4. Prizes
For each challenge track, there will be cash prizes for the top 3 winners as:
|Prize| Number | Award | Total |
|-|-|-|-|
|First Prize| 1 | $2,000 | $2,000 |
|Second Prize| 1 | $1,000 | $1,000 |
|Third Prize| 1 | $500 | $500 |


## 5. Timeline
**Competition**: 
- *Training*: June 1st, 2023 - Aug. 31st, 2023
- *Test submission*: Aug. 25th, 2023 - Aug. 31st, 2023 

**ITSC 2023 Conference**: Sep. 24th, 2023 - Sep. 28th, 2023


## 6. Dataset - PSI 2.0
[Pedestrian Situated Intent (PSI) 2.0](ttps://github.com/PSI-Intention2022/PSI2)

## 7. Baselines 

***Track 1 (Pedestrian Intent)***

***Track 2 (Pedestrian Trajectory)***

***Track 3 (Driver Decision)***


## 8.Evaluation

### Evaluation Metrics
| Challenge Track | Reported Metrics | Ranking Rule | 
| - | :- | :-: |
|***Track 1 (Pedestrian Intent)***| F1, Recall, Precision | $F1$ |
|***Track 2 (Pedestrian Trajectory)***| ADE@1.5s <br> FDE@1.5s | $ADE@1.5s$|
|***Track 3 (Driver Decision)***| speed: F1, Recall, Precision <br> direction: F1, Recall, Precision | $\frac{(F1_{speed} + F1_{direction})}{2}$|

### Evaluation Scripts

***Track 1 (Pedestrian Intent):*** The evaluation ranking score is the F1-score of intention binary prediction.
```python
python ./evaluation_scripts/intention/evaluate_results.py
```

***Track 2 (Pedestrian Trajectory):*** The evaluation ranking score is the average ADE of predicted trajectory over the future ***1.5s*** time.
```python
python ./evaluation_scripts/trajectory/evaluate_results.py
```

***Track 3 (Driver Decision):*** The evaluation ranking score is the average of mean-Accuracy of speed and direction predictions.
```python
python ./evaluation_scripts/driving_decision/evaluate_results.py
```


## 9. Submission

### Submission Format
***Track 1 (Pedestrian Intent):*** Example intention ground-truth/prediction JSON format:
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

***Track 2 (Pedestrian Trajectory):*** Example trajectory ground-truth/prediction JSON format:
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

***Track 3 (Driver Decision):*** Example driving decision ground-truth/prediction JSON format:
```
# Ground-truth
video_name: {
    frame_ID: {
        speed: int, 
        direction: int
    }
}
# Intent Prediction
video_name: {
    frame_ID: {
        speed_pred: int, 
        direction_pred: int
    }
}
```

### Evaluation Server

### Submission Policy

## 10. Questions & Contact

## 11. Organizers

## 12. Reference