import pandas as pd
import utilities as u
from calendar import monthrange

df = pd.read_excel(r'Volve production data.xlsx', sheet_name = 'Monthly Production Data', header =0)
df.drop(0,inplace=True)

df['NPDCode'] =df['NPDCode'].astype('int32')
df['Year'] =df['Year'].astype('int32')
df['Month'] =df['Month'].astype('int32')

WellsNPDc = df.loc[:,('Wellbore name','NPDCode')].drop_duplicates()

minYear= df['Year'].min()
minMonth = df[df['Year']==minYear]['Month'].min()
maxYear= df['Year'].max()
maxMonth = df[df['Year']==maxYear]['Month'].max()


for well in WellsNPDc['NPDCode']:
    iYear = minYear
    iMonth = minMonth
    while iYear*100+iMonth   <=maxYear*100+maxMonth:
        if df[(df['NPDCode'] == well) & (df['Year']==iYear) & (df['Month']==iMonth)].empty:
            name = WellsNPDc[WellsNPDc['NPDCode'] == well]['Wellbore name'].iloc[0]
            row = pd.DataFrame({'Wellbore name':name, 'NPDCode':[well],'Year':iYear,'Month':iMonth})
            df = df.append(row, ignore_index=True)
        if iMonth==12:
            iMonth =1
            iYear=iYear+1
        else:
            iMonth=iMonth+1

df['Day'] = df.apply(lambda x: monthrange(x['Year'], x['Month'])[1], axis=1)
df['Date']=pd.to_datetime(df.loc[:,('Year', 'Month','Day')])
df=df.sort_values(['Date']).reset_index(drop=True)
df.loc[:,('On Stream','Oil', 'Gas','Water','GI','WI')] =\
    df.loc[:,('On Stream','Oil', 'Gas','Water','GI','WI')].apply(pd.to_numeric,errors='coerce')

df['NGas']=df.loc[:,('Gas','GI')].apply(lambda x: u.netting(x['Gas'], x['GI']), axis=1)
df['NWater']=df.loc[:,('Water','WI')].apply(lambda x: u.netting(x['Water'], x['WI']), axis=1)
