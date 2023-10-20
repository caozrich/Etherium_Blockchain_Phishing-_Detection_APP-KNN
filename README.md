# Etherium Blockchain phishing detection APP using KNN 

<p align="center">
  <img alt="Files Logo" src="https://user-images.githubusercontent.com/34092193/219829292-d6555e66-b002-45de-ad59-3e14a2016dfe.png" width="450" />
  <h2 align="center">Ether Phishing Classifier</h2>
</p>

## Contents
- [Description](#Description)
- [About](#About)
- [Download](#Download)

## Description

The major blochains have been implicated in problems related to cyberattacks, scams, ponzi and pishing, the latter associated with at least 50% of cybercrime in the etherium network. this application uses a dataset of transactions in the etherium blockhain to classify by means of a KNN algorithm those that are pishing (the scope of this application is limited to the samples obtained from the dataset).

## About

<img src="https://user-images.githubusercontent.com/34092193/219829210-641c9419-77fd-41ca-b234-da363bdd40d8.gif" width="600" height="338"/>

Allows you to retrain the algorithm in real time by changing the hyperparameters and then see the impact on the ranking performance.


<img src="https://user-images.githubusercontent.com/34092193/219829211-a05ba0ce-51fe-4afb-9b54-4e2955df92c8.gif" width="600" height="338"/>

New samples can be used to be classified by the previously trained model.


<img src="https://user-images.githubusercontent.com/34092193/219829207-8f49d404-e06d-4deb-ab71-86f7fb9fad90.gif" width="600" height="338"/>

It also has a preview of the dataset used,(This dataset contains benign Ethereum blockchain transfers and officially reported phishing scam address transfers. The source of the dataset is the following [**research article**](https://ieeexplore.ieee.org/document/9943287)

## Download
This app can be downloaded from drive:

https://drive.google.com/file/d/1Gm_UUo8ijopbgOrRNGiTIbtPXzdn0_Or/view?usp=share_link

**Usage**: simply double-click on the Ether_Phishing_Classifier.exe file and follow the on-screen instructions.

## Known issues

- when executing, the dataset preprocessing procedure is carried out, and the KNN training, so it may take time to open depending on your system specs.
- The file weight is 230mb due to the compression of the required data science libraries.

## Libs used:
* scikit-learn==1.2.1
* numpy==1.24.2
* requests==2.28.2
* matplotlib==3.7.0
* pandas==1.5.3 
* seaborn==0.12.2
* PyQt5==5.15.4

#### Support:
If you have any questions or problems with the app, please contact the author at libreros00@gmail.com
