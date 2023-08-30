# Guidance of Using Test Data for Evaluation

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
5. Double check and modify the data path in the code and evaluate the results. 