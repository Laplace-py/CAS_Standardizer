import pandas as pd
import numpy as np

"""
Coluna com cas-id, o cas id tem que ser n-00-0
cas id 0000
"""
def cas_standardizer(file_from,cas_col):
        sheets = pd.ExcelFile(file_from).sheet_names
        
        for sheet in sheets:
            
            if sheet != ".":
                if file_from.find(".xlsx")!=-1:
                        df = pd.read_excel(file_from,sheet_name=sheet)
        
                if file_from.find(".csv")!=-1:
                        df = pd.read_csv(file_from,sheet_name=sheet)
                
                if cas_col in df.columns:
                        cas_ids = [str(cas) for cas in df[cas_col].values]
                        cas_list=[]

                        for cas in cas_ids: #cas=5-26-08
                                
                                rev_cas=cas[::-1]
                                
                                temp_cas=""
                                
                                for algarismo,letra in enumerate(rev_cas):
                                        temp_cas+=letra
                                        if algarismo==0:
                                                temp_cas=temp_cas+"-"
                                        if algarismo==2:
                                                temp_cas=temp_cas+"-"
                                
                                cas=temp_cas[::-1]
                                
                                cas_list.append(cas)
                        
                        df[cas_col]=cas_list

                        df.to_excel(f"{sheet}.xlsx")
                else:
                        pass
                
                
if __name__ =='__main__':
        
        inp1=input("File location: ")
        
        inp2=input("Columns containing cas numbers: ")
        
        cas_standardizer(file_from=inp1,cas_col=inp2)