# Guidance of Using Test Data for Evaluation

### Please download the data from https://drive.google.com/drive/folders/1vnRFzeMftAabUD7gqRn9PS8Ql_sVKO9-?usp=sharing

## 1. Test Data Information
For all three tasks, the test data contains **videos, CV annotations, and generated database**.
- **Videos**: There are 50 new videos released for test purpose.
- **CV annotations**: The CV annotations are provided in the same format as the training and validation data. There are annotations of the bounding boxes of pedestrians and other common objects.
- **Generated database**: The generated database follows the same format as the training and validation data. The database contains the information of the target pedestrians. It is noteworthy that the three tracks should have different generated databases.

## 2. How to Use the Test Data
If you follow the pipeline and structure of the provided baselines, using the test data is straightforward. You can simply replace the validation data with the test data.
1. Download the test data videos, cv annotations, and generated database.
2. Move downloaded *\*.zip* files to the dataset *ROOT_PATH*.

```shell
    unzip '*.zip' -d .
    rm *.zip
```
3. Use the script ```split_clips_to_frames.py``` to split the videos into frames, then move the frames and annotations to the corresponding folders.

```shell
    python split_clips_to_frames.py *ROOT_PATH*
```
4. Move the provided database file into the *database* folder as the validation and train database in the baseline. (It is noteworthy that you may not be able to generate the database for the test data for yourself since the cognitive annotations of the pedestrians intent are not provided.)
5. Double check and modify the data path in the code and evaluate the results. Then use the script ```prepare_data.py``` in the ```data``` folder to generate the dataloader, which is the same as the baseline training and validation processes.


## 3. IMPORTANT!!!: You SHOULD NOT use the test data to train or finetune the model.
We understand that certain annotations in the test data might inadvertently reveal information about other cases. Nevertheless, we have faith in our participants' commitment to adhering to the rules and refraining from using the test data for model training or fine-tuning. Our team will rigorously inspect the submitted code and model to ensure that the test data has not been utilized in any way during these processes.

To maintain the integrity of the competition and prevent any potential breaches, we will request all participants to provide their "code + training pipeline + trained weights." This information will undergo validation and result reproduction to minimize the risk of any unethical practices.

In the event of any rule violations, the implicated team will be disqualified from the competition.
