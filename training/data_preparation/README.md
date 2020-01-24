## Object Detection - Data Preparation

Training the Object Detector requires a dataset of images, annotated with the bounding boxes of each object identified in each image.

There are two possible ways to create traiing data:

1.  CloudAnnotation
    To easily create annotated image datasets, we can use [the Cloud Annotation Tool](https://cloud.annotations.ai/login), 
    a fast, easy and collaborative open source image annotation tool that makes it easy interactively draw bounding boxes around objects in images residing on [IBM Cloud Object Storage](https://www.ibm.com/cloud/object-storage). 

2. LabelImg + conversion in Python

# 1. Cloud Annotation
Follow the instructions in this document to prepare your data for training the object detector model.
- [Prerequisites](#prerequisites)
- [Preparing Your Data](#preparing-your-data)

## Prerequisites

Login into [Cloud Annotation Tool](https://cloud.annotations.ai/login) using your IBM Cloud credentials.

![login](imgs/login.png)

## Preparing Your Data

1. Choose the configured input bucket from the available buckets.

   _NOTE_ : The configured input bucket name can be obtained from the credentials displayed after running 
            the setup script. 
   
   ```bash
   
   ------------------------------------------------------------------------------
   NEW YAML CONFIGURATION VALUES
   ------------------------------------------------------------------------------
   input_bucket  : object-detector-input
   local directory  : ../data
   result bucket  : object-detector-output
   compute  : k80
   ------------------------------------------------------------------------------

   ```
   
![bucket](imgs/bucket.png)
   
2. Choose `Localization` from the options displayed on the screen and click `Confirm`.

![choice](imgs/choice.png)

3. Data uploaded during setup will be available inside the bucket for annotation. Click on `Add Label` to add
   class names.
   
![annotate](imgs/data.png)

4. Add the class names before proceeding with the annotation process.

![label](imgs/label.png)

  Continue adding label names if there are multiple objects for detection.
  
![multiple](imgs/multiple_objects.png)

5. Click on the image to start the annotation process. Select an appropriate label from the list displayed on the
   right side of the screen. Draw bounding box around the image. Follow the same steps for other images.

![process](imgs/bounding_box.png)

6. To view only unlabeled images, click on `unlabeled` option on the bottom of the screen.

![unlabeled](imgs/unlabeled.png)

Once you have completed annotating all your images, proceed to training parameter customization and initiate training.

# 2. labelImg + python

<Clone labelImg from: [Github labelImg](https://github.com/tzutalin/labelImg)
<Follow instructions in the README.md to get it running.
<Create a new folder under /training, for example: 'sample_pictures' (this is your $DATA_DIR int he training project)
<Create a subfolder called 'data' in /training/sample_pictures
<Copy all the your images 

    How to use the tool:
    << Click 'Open Dir' and navigate to the folder where all the picture are stored you want to annotate. All will be loaded to the tool.
    << Click 'Create RectBox' on the left side and draw a rectangle over the part of the picture you want to annotate
    <<From the pop-up window either select an existing label or add a new one.
    <<Currently you can only add one annotation per picture. (should/would be extended in the future)
    <<< Click save

<The xml files will be saved in the same folder where you had the pictures.
<Move the xml-s one folder-level higher: in /training/sample_pictures ($DATA_DIR)

The train-command.sh contains a new step to call xml2json for the $DATA_DIR that was defined in prepare_envs.sh. The output will be _annotations.json in the $DATA_DIR

