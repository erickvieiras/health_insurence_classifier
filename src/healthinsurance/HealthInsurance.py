import pickle
import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path = 'C:/Users/ErickVieira/Documents/repos/health_insurance/'
        self.annual_premium_scaler =            pickle.load( open( self.home_path + 'feature/annual_premium_scaler.pkl', 'rb' ) )
        self.age_scaler =                       pickle.load( open( self.home_path + 'feature/age_scaler.pkl', 'rb' ) ) 
        self.vintage_scaler =                   pickle.load( open( self.home_path + 'feature/vintage_scaler.pkl', 'rb' ) ) 
        self.target_encode_gender_scaler =      pickle.load( open( self.home_path + 'feature/target_encode_gender_scaler.pkl', 'rb' ) )
        self.target_encode_region_code_scaler = pickle.load( open( self.home_path + 'feature/target_encode_region_code_scaler.pkl', 'rb' ) )
        self.fe_policy_sales_channel_scaler =   pickle.load( open( self.home_path + 'feature/fe_policy_sales_channel_scaler.pkl', 'rb' ) )
        
    def data_cleaning( self, data ):
        # 1.1. Rename Columns
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code',
       'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
       'policy_sales_channel', 'vintage', 'response']

        # rename 
        data.columns = cols_new
        
        return data 

    
    def feature_engineering( self, data ):
        # 2.0. Feature Engineering

        # Vehicle Damage Number
        data['vehicle_age']    = data['vehicle_age'].apply(lambda x: 'Over 2 Years' if x == '> 2 Years' else 'Between 1 and 2 Years' if x == '1-2 Year' else 'Below 1 Year')
        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        return data
    
    
    def data_preparation( self, data ):
        # anual premium - StandarScaler
        data['annual_premium'] = self.annual_premium_scaler.transform( data[['annual_premium']].values )

        # Age - MinMaxScaler
        data['age'] = self.age_scaler.transform( data[['age']].values )

        # Vintage - MinMaxScaler
        data['vintage'] = self.vintage_scaler.transform( data[['vintage']].values )

        # gender - One Hot Encoding / Target Encoding
        data.loc[:, 'gender'] = data['gender'].map( self.target_encode_gender_scaler )

        # region_code - Target Encoding / Frequency Encoding
        data.loc[:, 'region_code'] = data['region_code'].map( self.target_encode_region_code_scaler )

        # vehicle_age - One Hot Encoding / Frequency Encoding
        data = pd.get_dummies( data, prefix='vehicle_age', columns=['vehicle_age'] )

        # policy_sales_channel - Target Encoding / Frequency Encoding
        data.loc[:, 'policy_sales_channel'] = data['policy_sales_channel'].map( self.fe_policy_sales_channel_scaler )
        
        # Feature Selection
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'policy_sales_channel', 'vehicle_damage', 'previously_insured']
        
        return data[ cols_selected ]
    
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )
        
        # join prediction into original data
        #original_data['prediction'] = pred
        original_data['response'] = pred[:, 0].tolist()
        original_data['score'] = pred[:, 1].tolist()        
        
        return original_data.to_json( orient='records', date_format='iso' )