#by richard libreros
import pandas as pd
import numpy as np
from help_functions import is_cat,resource_path
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.metrics as metrics



class phishingDetector():
    
    def __init__(self,odf = pd.DataFrame(),y = "",neightbors=1) :
        self.df     = odf.copy()
        self.y      = y  #independent variable name from the dataset
        self.neightbors = neightbors
        self.f1 = 0
        path = resource_path('complete_balanced_dataset.csv')      
        df = pd.read_csv(path)  

        y    = df["Class"]
        df   = df.drop("Class", axis=1)

        X_train_prep, X_test_prep,y_train,y_test = self.preprocessing(df,y)
        
        self.trainAlgorithm(X_train_prep, X_test_prep,y_train,y_test)
        


    def preprocessing(self,df,y):

        X_train, X_test, y_train, y_test = train_test_split(df, y,shuffle=True, test_size=0.2, random_state=42, stratify=y)
        
        global test
        test = X_test.copy()
        
        
        X_train, X_test,y_train,y_test = self.transformCatTonum(X_train, X_test,y_train,y_test) #transfrom categorical data to numeric        
        X_train_prep,X_test_prep         = self.scaling(X_train, X_test,y_train,y_test) 
        return X_train_prep, X_test_prep,y_train,y_test
        

            
    def deleteinvalidData(self,df): 
        for i in df.columns[df.isin([np.inf, -np.inf]).any()].tolist():
            df = df.drop(i, axis=1)
            
        return df    
    
    def scaling(self, X_train, X_test, y_train, y_test):
        
        ss = StandardScaler()

        X_train_transformed = ss.fit_transform(X_train)
        X_test_transformed = ss.fit_transform(X_test) 
        
    
        X_train_transformed = pd.DataFrame(X_train_transformed, columns=X_train.columns, index=y_train.index)
        X_test_transformed  = pd.DataFrame(X_test_transformed, columns=X_test.columns, index=y_test.index)
        return X_train_transformed,X_test_transformed
                
        
    def transformCatTonum(self,X_train, X_test, y_train , y_test): #transform categorical data to numerical        
        if is_cat(y_train) == True:         
            y_train = y_train.astype('category').cat.codes
            y_test  = y_test.astype('category').cat.codes     
        for col in X_train.columns:
           if is_cat(X_train[col]) == True:
                X_train[col]   = X_train[col].astype('category').cat.codes 
                X_test[col]    = X_test[col].astype('category').cat.codes  
        return X_train, X_test, y_train  , y_test   
    
    
    
    
    def trainAlgorithm(self, X_train_prep , X_test_prep, y_train, y_test):

        clf_tree = KNeighborsClassifier(self.neightbors)
        clf_tree.fit(X_train_prep, y_train)
        model = clf_tree
        
        y_pred  = clf_tree.predict(X_test_prep)


        f1 = f1_score(y_pred, y_test)

  
        #---some ev.metrics----
        # explained_variance=metrics.explained_variance_score(y_test, y_pred)
        # mean_absolute_error=metrics.mean_absolute_error(y_test, y_pred) 
        # mse=metrics.mean_squared_error(y_test, y_pred) 
        # mean_squared_log_error=metrics.mean_squared_log_error(y_test, y_pred)

        # explained_variance = round(explained_variance,4)
        # mean_squared_log_error =   round(mean_squared_log_error,4)
        # MAE = round(mean_absolute_error,4)
        # MSE = round(mse,4)
        # RMSE = round(np.sqrt(mse),4)     
        
        print(f1)   


        

trainModel = phishingDetector()


        
    
