## How to use the trainin_code folder to perform a local training

* Create a virtual python environment it not already done and activate it. Take a look at https://www.tensorflow.org/install/pip to see how it is done.
* Change DATA_DIR in prepare_envs.sh to point to the image folder. It should be similar to the directory that is alrady configured in this file.
* Create a folder one level above training_code and configure it in prepare_envs. This will be your model output
* Run ". prepare_envs.sh" from your terminal (from your training_code folder)
* Test if step6 was successful: run in terminal "echo $DATA_DIR" the result should be the file path you set in step2
* I you have not already setup the dependencies run pip install -r training_requirements.txt
* Execute "sh train-max-model.sh" to start your training
* If everything is finished (or while training is in progress) you can take a look at the training results using tensorboard. Instructions below.

`pip show tensorboard`<br/>
`cd into directory/tensorboard`<br/>
`python main.py --logdir=$RESULT_DIR/checkpoint` #if opening a new terminal make sure to rerun . prepare_envs.sh in /training_code

## Please add useful instructions that are currently missing
