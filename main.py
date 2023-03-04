#
# Точка входа
#
#import turtle
#import this

import numpy as np
import pandas as pd
import os


if __name__ == '__main__':
    
    #os.system('clear')
    df1 = pd.read_excel('./zzz.xlsx',0)
    df2 = pd.read_excel('./zzz_1.xlsx',0)
    #df1 = pd.read_excel('./sample.xlsx', 2, header = 0)
    #print(type(df))
    print(df1.columns)
    print(df2.columns)    

    #print(df1)
    #print(df1.dtypes)
    
    #col1 = df1['140.000']
    
#    col1 = df1['Таблица-приемник'] 
    
    #print(col1)
   # print('Количество записей', col1.aggregate('count'))
    
    #col1 = col1.unique()
  #  col1 = np.array(col1)
    
    #col3.sort()
    #print(type(col3),col3)

 #   col4 = np.array( ['Сайлент блоки задних продольных рычагов',
 #'Регулировка углов установки колес (сход-развал)',
 #'Замена бачка охлаждающей жидкости + пробка', 'Чистка радиаторов',
 #'Ремонт кондиционера'])

 #, 'Замена бензонасоса в баке', 'Поворотник',
 #'Поправить бампер', 'Полировка фар', 'Болт на АКПП1', 'Подкрасить кузов',
 #'Замена радиатора', 'Рулевые наконечники', 'Рулевые тяги',
 #'Диски тормозные передние'

    #col4 = np.array([140, 150, 160, 170,  np.nan],str)
    #col4.
    #col4.sort()
    #print(type(col4), col4)
    #res = np.array_equal(col3,col4)
    #print (res)

    #col5 = np.array(col4)
    #col6 = col3 != col4
    #print(col6)

    #df_s = pd.DataFrame(col1)
    #col1.unique
    #print('Количество уникальных записей', col1.aggregate('count'))
    #df_t = pd.DataFrame(col1)
    #df_s = pd.DataFrame(col4)
    #print (df_s)
    #print (df_t)

    #Таблица-приемник
    
    
    df_t = pd.DataFrame(pd.Series( df1['Таблица-приемник'].unique(),name = 'Таблица-приемник'))
    df_s = pd.DataFrame(pd.Series( df2['Таблица-приемник'].unique(),name = 'Таблица-приемник'))
    m = df_t.merge(df_s, how='outer', on=['Таблица-приемник'], sort = True, indicator=True)
    #print(m.columns)
    #print(m)
    
    #tmp_l = pd.Series(,name ='uq')
    tmp_df = pd.DataFrame({'uq':['left_only','right_only']})
    #print(tmp_df.columns)

    m2 = m.merge(tmp_df, left_on = '_merge', right_on=['uq'])
    print(m2)
    ##Таблица-приемник

    #Поле приемника
    
    df_t = pd.DataFrame (df1, columns = ['Таблица-приемник','Поле приемника'])
    df_s = pd.DataFrame (df2, columns = ['Таблица-приемник','Поле приемника'])
    #print(df_t)
    m = df_t.merge(df_s, how='outer', on=['Таблица-приемник','Поле приемника'], indicator=True)
    m = m.merge(tmp_df, left_on = '_merge', right_on=['uq'])
    print(m)
   
   
    ##Поле приемника

    #Тип данных поля приемника
    df_t = pd.DataFrame (df1, columns = ['Таблица-приемник','Поле приемника','Тип данных поля приемника'])
    df_s = pd.DataFrame (df2, columns = ['Таблица-приемник','Поле приемника','Тип данных поля приемника'])
    #print(df_t)
    m = df_t.merge(df_s, how='outer', on=['Таблица-приемник','Поле приемника','Тип данных поля приемника'], indicator=True)
    m = m.merge(tmp_df, left_on = '_merge', right_on=['uq'])
    print(m)
    ##Тип данных поля приемника


    
    #print( df_t)


    print('End!!!')
