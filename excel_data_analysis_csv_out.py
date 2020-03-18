import csv
import pandas as pd 

#data = pd.read_csv('product_codez.csv')

data = pd.ExcelFile('product_codes_p.xlsx')

data_1 = data.parse('scraped_produc_codes')

data_2 = data.parse('Order_data_Purchase_Data')

#scraped product price record
procesed_data_1 = data_1[['Product_Codes','Price_1']]
#scraped data product code list
pCodesList = procesed_data_1['Product_Codes'].tolist()

# purchased product price record
procesed_data_2 = data_2[['Row Labels','Average of Unit Price']]

numRow = len(procesed_data_2.iloc[:,0])-1
#numCol = len(procesed_data_2.iloc[0,:])

prod_tab_list = ['Product_code','Average_Purchase_price','Listed_Price','Cost_Status']

with open('product_cost_analysis.csv', 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(prod_tab_list)
    
    for r in  range(numRow):
       prodCode = procesed_data_2.iloc[r,0]
       buy_price = procesed_data_2.iloc[r,1]
       
#      find purchased product code row number in scraped data if it exist
       try:
           pCodesList.index(prodCode)
       except:
           print("Product code not in scraped data")
       else:
           sProdRowNum =  pCodesList.index(prodCode)
           list_price = procesed_data_1.iloc[sProdRowNum,1]
           if buy_price < list_price:
               cost_status = 'Cost_savings'
           else:
               cost_status = 'Cost_avoidance' 
               
           prod_cost_rec = [prodCode, buy_price, list_price, cost_status]
           writer.writerow(prod_cost_rec)
   