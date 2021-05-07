from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('HousePrice_Capstone_Project_1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Neighborhood_NoRidge=0
    Neighborhood_NridgHt=0
    Neighborhood_StoneBr=0
    Neighborhood_Veenker=0
    OverallQual_6=0
    OverallQual_7=0
    OverallQual_8=0
    OverallQual_9=0
    OverallQual_10=0
    ExterQual_Gd=0
    Heating_OthW=0
    TotRmsAbvGrd_9=0
    TotRmsAbvGrd_10=0
    TotRmsAbvGrd_11=0
    TotRmsAbvGrd_12=0
    GarageQual_Gd=0
    GarageQual_Po=0
    GarageCond_Gd=0
    GarageCond_Po=0
    Alpha_Ridge=0.7
    if request.method == 'POST':
        MSSubClass_160 = request.form['MSSubClass_160']
        if(MSSubClass_160=='2-STORY PUD - 1946 & NEWER'):
            MSSubClass_160=1
        else:
            MSSubClass_160=0
            
        LotConfig_CulDSac = request.form['LotConfig_CulDSac']
        if(LotConfig_CulDSac=='Cul-de-sac'):
            LotConfig_CulDSac=1
        else:
            LotConfig_CulDSac=0
            
        Neighborhood_Crawfor=request.form['Neighborhood_Crawfor']
        if(Neighborhood_Crawfor =='Crawford'):
            Neighborhood_Crawfor=1
            Neighborhood_NoRidge=0
            Neighborhood_NridgHt=0
            Neighborhood_StoneBr=0
            Neighborhood_Veenker=0
        elif (Neighborhood_NoRidge=='Northridge'):
            Neighborhood_Crawfor=0
            Neighborhood_NoRidge=1
            Neighborhood_NridgHt=0
            Neighborhood_StoneBr=0
            Neighborhood_Veenker=0
        elif (Neighborhood_NridgHt=='Northridge Heights'):
            Neighborhood_Crawfor=0
            Neighborhood_NoRidge=0
            Neighborhood_NridgHt=1
            Neighborhood_StoneBr=0
            Neighborhood_Veenker=0
        elif (Neighborhood_StoneBr=='Stone Brook'):
            Neighborhood_Crawfor=0
            Neighborhood_NoRidge=0
            Neighborhood_NridgHt=0
            Neighborhood_StoneBr=1
            Neighborhood_Veenker=0
        else:
            Neighborhood_Crawfor=0
            Neighborhood_NoRidge=0
            Neighborhood_NridgHt=0
            Neighborhood_StoneBr=0
            Neighborhood_Veenker=1
            
        OverallQual_5=request.form['OverallQual_5']
        if(OverallQual_5=='Average'):
            OverallQual_5=1
            OverallQual_6=0
            OverallQual_7=0
            OverallQual_8=0
            OverallQual_9=0
            OverallQual_10=0
        elif(OverallQual_6=='Above Average'):
            OverallQual_5=0
            OverallQual_6=1
            OverallQual_7=0
            OverallQual_8=0
            OverallQual_9=0
            OverallQual_10=0
        elif(OverallQual_7=='Good'):
            OverallQual_5=0
            OverallQual_6=0
            OverallQual_7=1
            OverallQual_8=0
            OverallQual_9=0
            OverallQual_10=0
        elif(OverallQual_8=='Very Good'):
            OverallQual_5=0
            OverallQual_6=0
            OverallQual_7=0
            OverallQual_8=1
            OverallQual_9=0
            OverallQual_10=0
        elif(OverallQual_8=='Execellent'):
            OverallQual_5=0
            OverallQual_6=0
            OverallQual_7=0
            OverallQual_8=0
            OverallQual_9=1
            OverallQual_10=0
        else:
            OverallQual_5=0
            OverallQual_6=0
            OverallQual_7=0
            OverallQual_8=0
            OverallQual_9=0
            OverallQual_10=1
        
        OverallCond_3=request.form['OverallCond_3']
        if(OverallCond_3=='Fair'):
            OverallCond_3=1
        else:
            OverallCond_3=0
        
        ExterQual_Fa=request.form['ExterQual_Fa']
        if(ExterQual_Fa=='Fair'):
            ExterQual_Fa=1
            ExterQual_Gd=0
        else:
            ExterQual_Fa=0
            ExterQual_Gd=1
            
        BsmtExposure_Gd=request.form['BsmtExposure_Gd']
        if(BsmtExposure_Gd=='Good Exposure'):
            BsmtExposure_Gd=1
        else:
            BsmtExposure_Gd=0
            
        Heating_Grav=request.form['Heating_Grav']
        if(Heating_Grav=='Grav'):
            Heating_Grav=1
            Heating_OthW=0
        else:
            Heating_Grav=0
            Heating_OthW=1
            
        FullBath_3 = request.form['FullBath_3']
        if(FullBath_3=='3'):
            FullBath_3=1
        else:
            FullBath_3=0
            
        BedroomAbvGr_5 = request.form['BedroomAbvGr_5']
        if(BedroomAbvGr_5=='5'):
            BedroomAbvGr_5=1
        else:
            BedroomAbvGr_5=0
            
        KitchenAbvGr_2 = request.form['KitchenAbvGr_2']
        if(KitchenAbvGr_2=='2'):
            KitchenAbvGr_2=1
        else:
            KitchenAbvGr_2=0
            
        TotRmsAbvGrd_8=request.form['TotRmsAbvGrd_8']
        if(TotRmsAbvGrd_8=='8'):
            TotRmsAbvGrd_8=1
            TotRmsAbvGrd_9=0
            TotRmsAbvGrd_10=0
            TotRmsAbvGrd_11=0
            TotRmsAbvGrd_12=0
        elif(TotRmsAbvGrd_9=='9'):
            TotRmsAbvGrd_8=0
            TotRmsAbvGrd_9=1
            TotRmsAbvGrd_10=0
            TotRmsAbvGrd_11=0
            TotRmsAbvGrd_12=0
        elif(TotRmsAbvGrd_10=='10'):
            TotRmsAbvGrd_8=0
            TotRmsAbvGrd_9=0
            TotRmsAbvGrd_10=1
            TotRmsAbvGrd_11=0
            TotRmsAbvGrd_12=0
        elif(TotRmsAbvGrd_11=='11'):
            TotRmsAbvGrd_8=0
            TotRmsAbvGrd_9=0
            TotRmsAbvGrd_10=0
            TotRmsAbvGrd_11=1
            TotRmsAbvGrd_12=0
        else:
            TotRmsAbvGrd_8=0
            TotRmsAbvGrd_9=0
            TotRmsAbvGrd_10=0
            TotRmsAbvGrd_11=0
            TotRmsAbvGrd_12=1
        
        Functional_Maj2 = request.form['Functional_Maj2']
        if(Functional_Maj2=='Maj2'):
            Functional_Maj2 = 1
        else:
            Functional_Maj2=0
        
        GarageQual_Fa = request.form['GarageQual_Fa']
        if(GarageQual_Fa=='Fair'):
            GarageQual_Fa=1
            GarageQual_Gd=0
            GarageQual_Po=0
        elif(GarageQual_Gd=='Good'):
            GarageQual_Fa=0
            GarageQual_Gd=1
            GarageQual_Po=0
        else:
            GarageQual_Fa=0
            GarageQual_Gd=0
            GarageQual_Po=1
            
        GarageCond_Fa = request.form['GarageCond_Fa']
        if(GarageCond_Fa=='Fair'):
            GarageCond_Fa=1
            GarageCond_Gd=0
            GarageCond_Po=0
        elif(GarageCond_Gd=='Good'):
            GarageCond_Fa=0
            GarageCond_Gd=1
            GarageCond_Po=0
        else:
            GarageCond_Fa=0
            GarageCond_Gd=0
            GarageCond_Po=1
            
        SaleCondition_Partial = request.form['SaleCondition_Partial']
        if(SaleCondition_Partial=='Partial'):
            SaleCondition_Partial=0
        else:
            SaleCondition_Partial=1
        
        prediction=model.predict([[MSSubClass_160,LotConfig_CulDSac,Neighborhood_Crawfor,Neighborhood_NoRidge,Neighborhood_NridgHt,Neighborhood_StoneBr,Neighborhood_Veenker, OverallQual_5, OverallQual_6, OverallQual_7, OverallQual_8, OverallQual_9, OverallQual_10,
                                   OverallCond_3,ExterQual_Fa,ExterQual_Gd,BsmtExposure_Gd, Heating_OthW, Heating_Grav,FullBath_3,BedroomAbvGr_5,KitchenAbvGr_2,TotRmsAbvGrd_8,TotRmsAbvGrd_9,TotRmsAbvGrd_10,TotRmsAbvGrd_11,TotRmsAbvGrd_12,Functional_Maj2,GarageQual_Fa,GarageQual_Gd,GarageQual_Po,GarageCond_Fa,GarageCond_Gd,GarageCond_Po,SaleCondition_Partial,Alpha_Ridge]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)