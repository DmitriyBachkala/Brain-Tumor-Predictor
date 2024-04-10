# Brain MRI - CNN Model 

## Objective: 
Determine the presence or absence of brain tumors in MRI images with at least 75% accuracy. 

## Data: 
Data was pulled from Kaggle. Ethical considerations were made to use a publicly available dataset without copyright infringement. The data was given in two folders: training and testing. Within each folder, four subfolders of images were saved: glioma, meningioma, no tumor, and pituitary. 

## Preprocessing: 
We used ImageDataGenerater to take images, flip, contort, zoom, tilt and then feed our model. This was needed for variation, allowing us to have more parameters for the model to be trained on. 

## Training: 
We used 4 convolutional layers. The first layer consisted of 32 filters, 64 filters for the second layer, 128 filters for the third layer, and 128 layers for the 4th layer. We used a flatten parameter to further shape the data. As a counter to overfitting we applied a dropout parameter of 50%. Our dense layer had 512 filters and our output layer had 1 filter.   


## Optimization: 
![image](https://github.com/DmitriyBachkala/Brain-Tumor-Predictor/assets/111262299/9d41f331-7f9b-480c-9b65-5941a282f15e)



## Testing: 
The model was tested against the testing folder (contains unseen images), this is how we determined the testing accuracy.
We used a confusion matrix to determine the accuracy versus recall values for the models as we ran them. We also looked at the validation accuracy versus training accuracy, and validation loss versus training loss to determine if the model was overfitting. 

![image](https://github.com/DmitriyBachkala/Brain-Tumor-Predictor/assets/111262299/a5243b86-8de8-4057-b5f4-125b0b87bc65)
![image](https://github.com/DmitriyBachkala/Brain-Tumor-Predictor/assets/111262299/6bbb2eb0-b742-4ec3-a58f-ad458288cd77)


Our initial tests involved categorizing images into 4 classification groups by tumor type: glioma, meningioma, pituitary, or no tumor present. However, the overall accuracy, and especially in the “no tumor” category yielded less than optimal results at 57% overall accuracy. After hypertuning, we were able to increase the overall accuracy to 69%, but we determined a binary model would be a better overall solution to the problem. It is more important to predict whether a tumor is present or absent than knowing the specific type of tumor: glioma vs meningioma vs pituitary. 

![Screenshot 2024-04-08 211627](https://github.com/DmitriyBachkala/Brain-Tumor-Predictor/assets/111262299/048a99f2-f794-47db-8f61-87e9e5a8e970)


After switching our model to a binary convolutional neural network model, we were able to achieve 94% overall accuracy, with an 83% precision and 98% recall for no tumor, and 99% precision and 93% recall for the presence of a tumor. 

![image](https://github.com/DmitriyBachkala/Brain-Tumor-Predictor/assets/111262299/3c0ca3a6-4ef7-4898-b8f3-aa4800907b67)

Augmentation for binary: After combining all the tumor classes we had an unbalanced data set, we had about 2000 more images in the tumor class than the no tumor class. Used code to augment and save slightly altered images in the no tumor class to balance the data set. This allowed us to achieve an optimal accuracy score.

Website was built with an api_flask python file, an html, and a css for styling. 

