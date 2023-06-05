# IEEE ITSS Student Competition in Pedestrian Behavior Prediction

# WE are hosting the [IEEE ITSS Student Competition in Pedestrian & Driver Behavior Prediction](https://psi-intention2022.github.io). 

The challenge has three tracks:
- [Pedestrian Intent Prediction (PIP)](https://github.com/PSI-Intention2022/PSI-Intent-Prediction.git)
- [Pedestrian Trajectory Prediction (PTP)](https://github.com/PSI-Intention2022/PSI-Trajectory-Prediction.git)
- [Driver Decision Prediction (DDP)](https://github.com/PSI-Intention2022/PSI-DriverDecision-Prediction.git)

The challenge is based on the [Pedestrian Situated Intent (PSI) 2.0](https://github.com/PSI-Intention2022/PSI-Dataset.git) dataset. 


## 1. Overview
Pedestrian behavior prediction is one of the most critical challenges for fully automated driving in urban settings, as it requires autonomous vehicles to interact safely and efficiently with pedestrians in diverse and dynamic environments. Accurate and robust pedestrian behavior prediction is crucial to ensure the safety of both pedestrians and the autonomous vehicles. 

## 2. Challenge Tracks

***Track 1 (Pedestrian Intent Prediction (PIP)):***  to predict the intention of a pedestrian crossing a street, such as whether they intend to cross or stop.

***Track 2 (Pedestrian Trajectory Prediction (PTP)):*** to predict the future trajectory of the pedestrian, given the pedestrian’s current position and intention.

***Track 3 (Driver Decision Prediction (DDP)):*** to predict the decision of the autonomous vehicle, given the pedestrian's intent and trajectory, to ensure safe and efficient interactions.

## 3. Qualification
We welcome competitors from all round the world. The leading attendee must be a student, graduate student or undergraduate student. Each team can join more than one track. Please check more details in the below website. 


## 4. Prizes
For each challenge track, there will be cash prizes for the top 3 winners as:

| Challenge Track | Gold | Silver | Bronze|
| - | :- | :-: | :-: |
|***Track 1 (Pedestrian Intent Prediction (PIP))***| $ 2,000 | $ 1,000 | $ 500 |
|***Track 2 (Pedestrian Trajectory Prediction (PTP))***| $ 2,000 | $ 1,000 | $ 500 |
|***Track 3 (Driver Decision Prediction (DDP))***| $ 2,000 | $ 1,000 | $ 500 |


## 5. Timeline
**Competition**: 
- *Training*: June , 2023 - August, 2023
- *Test submission*: Aug. 31st, 2023 (TBD)

**ITSC 2023 Conference**: Sep. 24th, 2023 - Sep. 28th, 2023


## 6. Dataset - Pedestrian Situated Intent (PSI) 2.0 [[Homepage](http://pedestriandataset.situated-intent.net/)]

- Prepare Dataset: Please follow [[Github](https://github.com/PSI-Intention2022/PSI-Dataset.git)] to prepare the PSI 2.0 dataset.
  - Training set: 
  - Validation set: 
  - Test set: TBD

- Data Splits: The PSI 2.0 dataset is splitted into Train/Val/Test split as [./splits/PSI2_split.txt](./splits/PSI2_split.json).

## 7. Baselines 
We provide baselines for all tracks of challenges as hints about using the PSI 2.0 dataset for a quick start. 

***Track 1 ([Pedestrian Intent Prediction (PIP)](https://github.com/PSI-Intention2022/PSI-Intent-Prediction.git))***

***Track 2 ([Pedestrian Trajectory Prediction (PTP)](https://github.com/PSI-Intention2022/PSI-Trajectory-Prediction.git))***

***Track 3 ([Driver Decision Prediction (DDP)](https://github.com/PSI-Intention2022/PSI-DriverDecision-Prediction.git))***



## 8.Evaluation

### Evaluation Metrics
| Challenge Track | Reported Metrics | Ranking Metric | Ranking Rule|
| - | :- | :-: | :-: |
|***Track 1 (Pedestrian Intent Prediction (PIP))***| F1, Recall, Precision | $F1$ | $\uparrow$|
|***Track 2 (Pedestrian Trajectory Prediction (PTP))***| ADE@1.5s <br> FDE@1.5s | $\frac{(ADE_{0.5s}+ADE_{1.0s}+ADE_{1.5s})}{3}$| $\downarrow$|
|***Track 3 (Driver Decision Prediction (DDP))***| speed: Acc, mAcc <br> direction: Acc, mAcc | $\frac{(mAcc_{speed} + mAcc_{direction})}{2}$| $\uparrow$|

### Evaluation Scripts

***Track 1 (Pedestrian Intent):*** The evaluation ranking score is the F1-score of intention binary prediction.
```python
cd ./evaluation_scripts/intention
python evaluate_results.py
```

***Track 2 (Pedestrian Trajectory):*** The evaluation ranking score is the average ADE of predicted trajectory over the future ***1.5s*** time.
```python
cd ./evaluation_scripts/trajectory
python evaluate_results.py
```

***Track 3 (Driver Decision):*** The evaluation ranking score is the average of mean-Accuracy of speed and direction predictions.
```python
cd ./evaluation_scripts/driving_decision
python evaluate_results.py
```


## 9. Submission

### Submission Policy
TBD

### Winners Validation
Winners would be required to provide their code and trained weights for valication process. More details about code submission will be updated. 

### Submission Format
***Track 1 (Pedestrian Intent):*** Example intention ground-truth/prediction JSON format:
```
# Filename: val/test_intent_gt/prediction.json
video_name: {
    pedestrian_ID: {
        frame_ID: {
            intent: int # 0-not cross, 1-crossing
        }
    }
}
```

***Track 2 (Pedestrian Trajectory):*** Example trajectory ground-truth/prediction JSON format:
```
# Filename: val/test_traj_gt/prediction.json
video_name: {
    pedestrian_ID: {
        frame_ID: {
            traj/traj: {
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
# Filename: val/test_driving_gt/predictio.json
video_name: {
    frame_ID: {
        speed: int, 
        direction: int
    }
}
```

## 10. Organizers
[Zhengming Ding](https://allanding.github.io), [Renran Tian](https://et.iupui.edu/people/rtian), [Taotao Jing](https://scottjingtt.github.io/about/), [Xin Hu](), [Zhengming Zhang]().

## 11. Sponsorship

IEEE ITSC 2023

## 12. Questions & Contact
If you have any questions, please contact [psi.intent.benchmark@gmail.com](psi.intent.benchmark@gmail.com)

## 13. Reference

[1] Chen, Tina, Taotao Jing, Renran Tian, Yaobin Chen, Joshua Domeyer, Heishiro Toyoda, Rini Sherony, and Zhengming Ding. "Psi: A pedestrian behavior dataset for socially intelligent autonomous car." arXiv preprint arXiv:2112.02604 (2021).

[2] Chen, Tina, Renran Tian, and Zhengming Ding. "Visual reasoning using graph convolutional networks for predicting pedestrian crossing intention." In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 3103-3109. 2021.

[3] Jing, Taotao, Haifeng Xia, Renran Tian, Haoran Ding, Xiao Luo, Joshua Domeyer, Rini Sherony, and Zhengming Ding. "InAction: Interpretable action decision making for autonomous driving." In Computer Vision–ECCV 2022: 17th European Conference, Tel Aviv, Israel, October 23–27, 2022, Proceedings, Part XXXVIII, pp. 370-387. Cham: Springer Nature Switzerland, 2022.

[4] Zhang, Zhengming, Renran Tian, and Zhengming Ding. "TrEP: Transformer-based Evidential Prediction for Pedestrian Intention with Uncertainty." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36, no. 3, pp. 3589-3597. 2022.
