import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dict= {
    "name": ["lucky","sovit","raounak","bholu","pallu"],
    "marks": ["34","56","76","89","90"],
    "its cgpa": ["9.9","8.9","8.8","9,0","7.6"]
}  
 
df= pd.DataFrame(dict,index= ["rowA","rowB","rowC","rowD","rowE"],)
print("pandas dataframe:\n",df)

                                        TO Acess any row and column in data frames                

dict= {
    "name": ["lucky","sovit","raounak","bholu","pallu"],
    "marks": ["34","56","76","89","90"],
    "its cgpa": ["9.9","8.9","8.8","9,0","7.6"]
}  
 
df= pd.DataFrame(dict,index= ["rowA","rowB","rowC","rowD","rowE"],)
print("pandas dataframe:\n",df)

z= df.loc["rowA","name"]
print("values of all the row and column :\n",z)
print("values of all row and column :\n",df.loc["rowA","marks"])


                                      TO ACESS GROUP OF ROW AND COLUMN BY INTEGER POSITION

dict= {
    "name": ["lucky","sovit","raounak","bholu","pallu"],
    "marks": ["34","56","76","89","90"],
    "its cgpa": ["9.9","8.9","8.8","9,0","7.6"]
}  

df= pd.DataFrame(dict,index= ["rowA","rowB","rowC","rowD","rowE"],)
print("pandas dataframe:\n",df)

x= df.iloc[[3,4]]
print("values of row and coulumn by integer :\n",x)
print("values of row and coulumn by integer :\n",df.iloc[[2,4]])


                                              TO NAME THE INDIUCES BY ROW AND COLUMN

dict= {
    "name": ["lucky","sovit","raounak","bholu","pallu"],
    "marks": ["34","56","76","89","90"],
    "its cgpa": ["9.9","8.9","8.8","9,0","7.6"]
}  
 
df= pd.DataFrame(dict,index= ["S1","S2","S3","S4","S5"],)
print("pandas dataframe:\n",df)


                                              TO ITERATE THE ROW AND COLUMN

dict= {
    "name": ["lucky","sovit","raounak","bholu","pallu"],
    "marks": ["34","56","76","89","90"],
    "its cgpa": ["9.9","8.9","8.8","9,0","7.6"]
}  
 
df= pd.DataFrame(dict,index= ["rowA","rowB","rowC","rowD","rowE"],)
print("pandas dataframe:\n",df)

print("\n display the column")

for col in df :
    print(col)


                              VARIOIUS ATTRIBUTES ON DATA FRAMES 
                          1.  DATA TYPES

data= {
    "names":["lucky","bholu","raunak","golu"],
    "marks":["34","54","76","98"],
    "city":["gurgao","patna","banglore","gaya"]
}

df= pd.DataFrame(data,index=["student1","student2","student3","student4"],)
print("dataframes:\n",df)

print("its give the d type \n:",df.dtypes)

                                 2 . N DIMENSUON

data= {
    "names":["lucky","bholu","raunak","golu","romi","soviet","chotu"],
    "marks":["34","54","76","98","56","87","98"],
    "city":["gurgao","patna","banglore","gaya","delhi","gurgaon","rongha"]
}

df= pd.DataFrame(data,index=["student1","student2","student3","student4","student5","student6","student7"],)
print("dataframes:\n",df)

print("\nfor dimrnsion of the data frame:\n",df.ndim)
print("to find the indices:\n",df.index)


                                  3 . FOR SIZES

df= pd.DataFrame(data,index=["student1","student2","student3","student4"],)
print("dataframes:\n",df)

print("for sizes of data frames:\n",df.size)

#                                   4. FOR SHAPES

df= pd.DataFrame(data,index=["student1","student2","student3","student4"],)
print("dataframes:\n",df)

print("for shapes of dataframes:\n",df.shape)

                                     5. FOR INDEXES

df= pd.DataFrame(data,index=["student1","student2","student3","student4"],)
print("dataframes:\n",df)

print("for indices in data frames:\n",df.index)

                                      6.  TRANSPOSES

df= pd.DataFrame(data,index=["student1","student2","student3","student4","student5","student6","student7"],)
print("dataframes:\n",df)
z= df.T
print("transposes of data frame:\n",z)
print("shape of the transpose data :",z.shape)

                                  7. HEAD ()
df=pd.DataFrame(data,index=["student1","student2","student3","student4"],)
print("dataframes:\n",df)

print("to get the row from begging except last row:\n",df.head(0))

#                                   8. TAIL()

df= pd.DataFrame(data,index=["student1","student2","student3","student4","styudent5","student6","student7"],)
print("dataframes:\n",df)

print("to get row from last except first one if more then 5 :\n\n",df.tail(6))


                                      TO JOIN TWO PANDAS DATA FRAMES

data1={
    "name":["lucky","golu","bholu","raunak","romi"],
    "marks":["65","98","65","43","90"],
    "rank":["1","2","45","65","4"]
}

data2= {
    "city":["patna","delhi","gurgao","gaya","uttamnagar"],
    "its cgpa":["4.5","6.7","9.8","8.7","7.7"]
}

                                   to ADD by column  USE JOIN METHODS

df1= pd.DataFrame(data1)
print(df1)
df2= pd.DataFrame(data2)
print(df2)

# x= df1.join(df2)
print("to join two dataframes by column:\n",df1.join(df2))

                                      TO CONCATE THE TWO DATAFRAMES

data1={
    "name":["lucky","golu","bholu","raunak","romi"],
    "marks":["65","98","65","43","90"],
    "rank":["1","2","45","65","4"]
}

data2= {
    "name":["patna","delhi","gurgao","gaya","uttamnagar"],
    "marks":["45","76","76","89","90"],
    "rank":["3","5","6","7","9"]
}

df1= pd.DataFrame(data1)
print(df1)
df2= pd.DataFrame(data2)
print(df2)

Z= pd.concat([df1,df2])
print("to add two dataframes:\n",Z)


                                          Create PANDAS SERIES 

data= ["56","87","80","65","55","44"]

s= pd.Series(data)
print("dataframes in series:\n",s)
print("to FIND THE DIMENSION OF THE PANDAS SERIES:\n",s.ndim)


                                          ACCESS A value from pandas series

data= ["lucky","golu","raounak","romui"]

s= pd.Series(data,index=["row1","row2","row3","row4"])
print("to acess the value from dataframes:\n",s)

print("a specific element from the dataframes:\n",s[2])


                                          To Names the INDICES

data= ["20","45","56","90","54","lucky","golu"]

p= pd.Series(data,index=["row1","row2","row3","row4","row5","row6","row7"])
print("to names the indices in series:\n",p)

                                          TO ACCESS ANY ROW IN PANDAS SERIES

data= ["20","45","56","90","54","lucky","golu"]

p= pd.Series(data,index=[["row1","row2","row3","row4","row5","row6","row7"]])
print("to acess the value of row:\n",p)

print(p["row3"])
print(data[3])

#                                      pandas series : ATTRIBUTES AND METHODS

data= ["20","45","56","90","54","lucky","golu"]

s= pd.Series(data)                                      # first make it in series to apply methods
print(s)

print(s.dtype)

                              2 . for N DIMENSION 

s= pd.Series(data)                                      
print(s)

print("for n dimension in series:\n",s.ndim)


                              3. for SIZES 

s= pd.Series(data)
print(s)

print("for sizes in pandas series:\n",s.size)

                              4. for shapes
s= pd.Series(data)
print(s)

print("for shapes in pandas series:\n",s.shape)


                              5. for ATTRIBUTE

s= pd.Series(data, name="my first diaries")
print(s)

print("to find attributes:\n",s.name)

                              6 . FOR HAS NANS

s= pd.Series(data)
print(s)

print("for hasnans in series in pandas:\n",s.hasnans)

                                  7. INDEX ATTRIBUTE

s= pd.Series(data, index= ["rowA","row2","row3","row4","row5","row6","row7"],)
print(s)

print("for  attributes in pandas series:\n",s.index)


                                      8. HEAD ()

s= pd.Series(data)
print(s)

print("head in the pandas series:\n",s.head())


                                      9. TAILS()

s= pd.Series(data)
print(s)

print("for tail in pandas series:\n",s.tail(4))

                                      10. INFO ()METHODS

s= pd.Series(data)
print(s)

print("for info in panda series:\n",s.info())


                                      COMBINES TWO PANDAS IN SERIES

data1= [23,54,87,90,12]
data2= [44,88,78,98,100]

S1= pd.Series(data1) 
print("FIRSTLY PRINT THE DATA :\n",S1)

S2= pd.Series(data2)
print("THEN PRINT THE SECOND DATA:\n",S2)

def demo(x1,x2):
    if(x1 > x2):
        return(x1)
    else:
        return(x2)   

res= S1.combine(S2,demo)      
print("TO COMBINE THE TWO SERIES:\n",res)



#                                                       CATEGORICALS DATA FRAMES
#                                          1 . CREATE CATEGORICAL SERIES

data=["lucky","golu","bholu","raunak","rahul","chotu"]
s= pd.Series(data,dtype="category")
print(s)

#                                                  2 . CREATE CATEGORICAL DATAFRAMESS
dict={
    "names":["lucky","bholu","chotu","ankit"],
    "marks":[23,54,87,90],
    "rank":[22,1,3,7]
}
df= pd.DataFrame(dict,dtype="category")
print("CATEGORICAL DATAFRAMES:\n",df)


#                               TO APPEND NEW CATEGORIES IN PANDA SERIES

s= pd.Series(data,dtype="category")
print(s)

z= s.cat.add_categories("for")
print(z)


#                                  TO REMOVE A CATEGORIES IN PANDAS SERIES

s=pd.Series(data,dtype="category")
print(s)

x= s.cat.remove_categories("chotu")
print(x)


##                                             PANDAS ------<< READ CSV

#                                  1 . READ A CSV

df=pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\studentsNew.csv")
print("to read any excel files:\n\n:",df)

                                  2 . display tHe TOP  N rows of DF

s= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\studentsNew.csv")
print("to read and print the data:\n",s)

x= s.head(3)
z= s.head()
print("to read tye top n rows of excel :\n",x)
print("to read tye top n rows of excel :\n",z)

                                  3 . to DISPLAY The last N rows

s= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\studentsNew.csv")
print("to read and print the data:\n",s)

print("to read the last n rows of the excel:\n",s.tail(3))


#                                     PANDAS -------><><  TO READ EXCEL FILES IN V.S CODE

df=pd.read_excel("C:\\Users\\user\\OneDrive\\Desktop\\cricket.xlsx")
print("to read any excel files:\n",df)

                      1 . to read fIRST N ROWS OF ANY EXCELS

df= pd.read_excel("C:\\Users\\user\\OneDrive\\Desktop\\cricket.xlsx")
print("first to read any excels:\n",df)

x= df.head()
print("to read the first n row of excels::\n",x)
print("to read the first n row of excels::\n",df.head(3))
print("to read the first n row of excels::\n",df.head(6))

                        2. to read the last n rows in excels

df= pd.read_excel("C:\\Users\\user\\OneDrive\\Desktop\\cricket.xlsx")
print("first to read the any excel files:\n",df)

z= df.tail()
print("to read the last n rows of any excels:\n",z)
print("to read the last n rows of any excels:\n",df.tail(4))
print("to read the last n rows of any excels:\n",df.tail(1))


#                                              PANDAS ---- INDEXINGS 

df=pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\studentsNew.csv")
print("first to read any csv:\n",df)

res= df["Marks"]
print("to get the indices of any csv in v.s code:\n",res)
print("to get the indices of any csv in v.s code:\n",df["Rank"])

                                      1 . INDEXING BY LOC METHODS

df=pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv",index_col="Frequency")

print("first to read any csv:\n",df)

res= df.loc[2.4]
print("to read any excels by his names:\n",res)
print("to read any excels by his names output:\n",df.loc[1.2])


                                      2 . INDEXING BY ILOC METHODS

df=pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv",index_col="Frequency")
print("first to read any csv:\n",df)

res= df.iloc[4]
print("to read any excels by its positions numbers:\n",res)
print("to read any excels by its positions numbers:\n",df.iloc[3])


#                                          PANDAS -----><><  TO SELECT MULTIPLE COLUMNS
data= {
    "names": ["lucky","golu","raunak","soviet","romi babu","lucky","chotu"],
    "ranks":["3","4","6","7","9","9","6"],
    "marks":["54","76","100","90","100","66","88"]
}

#                                 1 . SELECT TWO COLUMNS

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the data i dataframes:\n",df)

print("TO ACCES TWO COLUMN IN ANY DATA:\n",df[["marks","ranks"]])

#                                      2  . SELECTING MULTIPLES COLUMNS

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print(df)

print("TO ACCES MULTIPLE COLUMNS IN DATA FRAMES:\n",[df.columns[2:5]])


#                                      PANDAS -------><><  TO ADD NEW COLUMNS   

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

                                      1 . TO ADD ANY NEW COLUMNS  USING ---- INSERT METHODS & ATTRIBUTES

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the data i dataframes:\n",df)

df.insert(loc=1,column="roll no",value=[12,13,14,15,16,17,18])
print("to ADD a new COLUMN IN DATA FRAME:\n",df)
print(df["roll no"])

                                      2 . TO ADD NEW COLUMNS AT LAST OF DATA FRAMES ----><><         ASSIGN METHODS(())

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

resdf= df.assign(roll=[54,56,67,98,44,54,90])
print("to add new columns at the last of dataframes:\n",resdf)


#                                      PANDAS ------>< DELETE ANY COLUMNS BY DROP() METHODS

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

resdf= df.drop("ranks",axis="columns")                              # TAKE AXIS OF WHICH YOU WANT TO DELETE LIKE IN THIS WE WANT TO DELETE ANY SPECIIC COLUMNS AND ALSO TAKE THAT SPECIFIC CHARACTER WHICH WE HAVE TO DELETE LIKE "RANKS"
print("to DELETE ANY COLUMNS BY THIS DROP METHODS:\n",resdf)


#                                      2. to DELETE ANY ROWS  BY DROP METHODS 
df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

resdf= df.drop("row3",axis="index")                             # TAKE AXIS OF WHICH WE WANT TO DELETE AND ALSO TAKE THAT SPECIFIC CHARACTER WHICH WE HAVE TO DELETE LIKE "ROW3" "ROW4"
print("TO DELETE ANY ROW IN DATAFRAME\n:",resdf)


                                              PANDAS --- ITERATES ROW AND COLUMNS 

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

#                               TO ITERATE THE ROWS 

for row in df.iterrows():
    print("TO ITERATE THE ROWS IN DATAFRAMES:\n",row)

for columns in df.iterrows():
    print(columns)

 #                              TO ITERATE THE COLUMNS 

for row in df.itertuples():
    print(row)   


                                                           PANDAS ---  items to ITERATES OVERS  COLUMNS ><><

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

for a , b in df.items():
    print(a)
    print(b)

                                                              PANDAS ------><> SORTINGS
df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",df)

resdf=df.sort_values(by=["names"])
print("TO PRINT MARKS IN ASCENDING ORDER:\n",resdf)

#                                               2. TO SORT IT IN DESCENDINGS ORDER

nump= pd.DataFrame(data,index=["row1","row2","row3","row4","row5","row6","row7"],)
print("to print the dataframes:\n",nump)

x= df.sort_values(by=["ranks"],ascending=False)
print(x)


#                                              PANDAS -----><>< HANDLINGS DUPLICATES

#                                      1. TO FIND THE DUPLICATE BY DUPLICATED() ATTRIBUTES

df= pd.DataFrame(data)
print("to print the dataframes:\n",df)

x= df.duplicated("names")
print("to FIND THE DUPLICATES THE IN DATA FRAMES:\n",x)

##                                      2 . to delete the DUPLICATES BY [ DROP DUPLICATES() ] ATTRIBUTES

f= pd.DataFrame(data)
print("to print the dataframes:\n",f)

df=f.drop_duplicates("ranks")
print("to DELETE THE DUPLICATES IN THE DATA FRAMES :\n",df)


#                                            @@  PANDAS ----><>< CLEAN THE DATA ( CLEANING THE DATA )
#                                                  BUILT - IN FUNCTIONS

#                                  1 .  IS NULL()  ---- TO FIND NULL VALUE AND REPALCE THEM WITH TRUE

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("first PRINT THE CSV DATA FRAME:\n",df)

resdf= df.isnull()
print("to print the null value and exchange them with true:\n",resdf.to_string())
print("to print the null value and exchange them with true:\n",resdf)

#                                  2 . NOT NULL() ----- TO FIND NOT NULL VALUE AND REPLACE THEM WITH TRUE ,ELSE FALSE IS RETURNED

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("first PRINT THE CSV DATA FRAME:\n",df)

resdf= df.notnull()
print("to print the not null value and exchange them with true:\n",resdf.to_string())

#                                      3 . df.DROPNA() ------- > < DELETE THE ROW WITH THE NULL VALUES::: 

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("first PRINT THE CSV DATA FRAME:\n",df)

resdf= df.dropna()
print("used to DROP AND REMOVE ROW WITH NULL VALUE:\n",resdf.to_string())

#                                          4 . df.fill na() functions --------><>< FILL THE ROW WITH NULL VALUE WITH SOME SPECIFIC NUMBER TAKEN BY THE USERS:;:

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("first PRINT THE CSV DATA FRAME:\n",df)

resdf= df.fillna(234)
print("USED TO REPLACE NULL VALUE WITH SPECIFIC VALUE:\n",resdf.to_string)


#                                      STRINGS OPERATIONS OF TEXT DATA

#                                              1 . lower () Methods

data= ["Lucky","Golu","Bholu","Chotu","Romi","Raunak","Ankit"]
df= pd.Series(data)

print(df)
print(df.str.lower())


#                                              2. UPPER() METHODS

data= ["Lucky","Golu","Bholu","Chotu","Romi","Raunak","Ankit"]
df= pd.Series(data)
print(df)

print(df.str.upper())


#                                              3. TITLE () METHODS

data= ["lucky","golu","bholu","chotu","romi","raunak","ankit"]
df= pd.Series(data)

print(df)
print(df.str.title())

##                                              4 . len() METHODS

data= ["Lucky","Golu","Bholu","Chotu","Romi","Raunak","Ankit"]
df= pd.Series(data)

print(df)
print(df.str.len())

#                                                      5 . COUNT() METHODS             # TO COUNT THE NON- EMPTY CELLS IN THE DATA

data= ["Lucky","Golu","Bholu","Chotu","Romi","Raunak","Ankit","Bholu"]
df= pd.Series(data)
print(df)

print(df.count())

###                                                        6 . CONTAINS() METHODS

data= ["Lucky","Golu","Bholu","Chotu","Romi","Raunak","Ankit"]
df= pd.Series(data)
print(df)

print(df.str.contains("Ankit"))


                                               PANDAS ---->< DATE AND TIMES OPERATIONS ()

                                                  1 . GET The CUreent Date And Times ()

x= pd.Timestamp.now()
print("to get current time and date:\n",x)

print("to get current day of week:\n",x.day_of_week)
print("TO get current day of the year:\n",x.day_of_year)
print("CURRENT DATE AND TIME: \n",pd.Timestamp.now())

                                                  2. GET THE DAY OF THE DAY OF THE WEEK()

timestamp= pd.Timestamp(year=2023,month=12,day=29,hour=11)
print("firstly get the current timestamp:\n",timestamp)

print("for the day of thE WEEK :\n",timestamp.day_of_week)                # 4

#                                                      3 . GET THE DAY OF THE YEAR ().

timestamp= pd.Timestamp(year=2025,month=6,day=17,hour=12)
print("firstly get the current time stamp:\n\n",timestamp)

print("to gET THE DAY OF THE YEAR:\n\n",timestamp.day_of_year)         # 168

#                                                      4 . GET THE NUMBERS OF DAYS IN MONTHS()

today=pd.Timestamp.now()
print("get the current timestamp:\n",today)

print("to GET THE NUMBERS OF DAY IN MONTH:\n",today.days_in_month)              # 31

#                                                      5 . IF THE YEAR IS LEAP YEAR OR NOT()

timestamp= pd.Timestamp(year=2006,month=11,day=23,hour=1)
print("to bet the current time stanmp:\n",timestamp)

print("to get if the year is leap or not:\n",timestamp.is_leap_year)

                                                       6. IF THE DATE IS LAST DAY OF MONTH OR NOT()

timestamp= pd.Timestamp.now()
print("firstly get the current date:\n",timestamp)

print("to find if the last day of month or not:\n",timestamp.is_month_end)

                                                      7 . IF THE DATE IS FIRST DAY OF MONTH OR NOT()

timestamp= pd.Timestamp(year=2023,day=1,month=1,hour=3)
print("firstly get the current date:\n",timestamp)

print("to find if the first day of month or not:\n",timestamp.is_month_start)


                                                      8. IF DATE IS LAST DAY OF YEAR OR NOT()

timestamp= pd.Timestamp(year=2021,month=12,day=31,hour=4)
print("firstly get the current date:\n",timestamp)

print("to find the last of year or not:\n",timestamp.is_year_end)

                                                      9. IF DATE IS FIRST DAY OF YEAR()


timestamp= pd.Timestamp.now()
print("firstly get the current date:\n",timestamp)

print("if the date is first day of year or not:\n",timestamp.is_year_start)


#                                                   REMOVE WHITESPACES OR SPECIFIC CHARACTER()
                                                          1 . STRIP()METHOD

data= ["lucky@","raunak#","bholu","golu!!","soviet@","rausan!!"]
series= pd.Series(data,index=["name1","name2","name3","name4","name5","name6"],)
print(series)

print("to remove the specific character from both left and the right side:\n\n",series.str.strip("!@#$"))


#                                                              2 . LSTRIP METHOD()

data= ["@!lucky@","#@raunak#","@@bholu","golu!!","!soviet@","##rausan!!"]
series= pd.Series(data,index=["name1","name2","name3","name4","name5","name6"],)
print(series)

print("TO REMOVE THE SPECIFIC CHARA FROM LEFT SIDE ONLY:\n",series.str.lstrip("!@#$%"))


#                                                                  3 . R STRIP METHOD()

data= ["@!lucky@","#@raunak#","@@bholu","golu!!","!soviet@","##rausan!!"]
series= pd.Series(data,index=["name1","name2","name3","name4","name5","name6"],)
print(series)

print(" TO REMOVE THE SOECIFIC CHARACTER FROM THE RIGHT SIDE ONLY:\n",series.str.rstrip("!@#$%"))


#                                                       PANDAS --><> GROUP THE DATA
#                                                          1. SPLIT OBJECT AND COMBINE THE RESULT

data={
    "names":["lucky","golu","bholu","soviet","romi","alexander"],
    "marks":["34","56","67","90","65","23"],
    "rank": ["2","4","6","7","1","3"]
}

df= pd.DataFrame(data,index=["rowa","rowB","rowC","rowD","rowE","rowF"])
print(df)    

res= df.groupby("names")

print(res.first())

#                                                      2 . ITERATE THE GROUP()

groupres= df.groupby("names")

for name,group in groupres:
    print(name)
    print(group)

#                                                      3 . VIEW THE GROUP 

print(df.groupby("names").groups)

#                                                  --- STATISTICAL FUNCTIONS -----><>>< 

                                          1 . SUM () FUNCTIONS 

marks={
    "math":[45,78,98,90,65],
    "chemistry":[54,89,55,66,72],
    "physics":[66,67,86,44,90],
    "biology":[10,42,44,60,80]
}

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)

print("to PRINT THE SUM OF ABOVE DATA FRAME:\n",df.sum())

##                                                      2 . COUNT () FUNCTIONS

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)

print("TO FIND THE NON EMPTY VALUES IN THE DATAFRAME:\n",df.count())

##                                                       3 . MAX () FUNCTIONS:

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)
x=df.max()
print("to finD THE MAXIMUM OF THE FOLLOWING DATA:\n",x)

# ##                                                          4 . MIMIMUM () FUNCTIONS

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)
z= df.min()
print("TO FIND THE MINIMUM OF THE DATAFRAME:\n",z)

#3                                                          5 .  MEAN () FUNCTIOMS

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)

print("TO FIND THE MEAN OF THE FOLLOWING DATAFRAMES:\n",df.mean())

##                                                               6. MEDIAN() FUNCTION

df= pd.DataFrame(marks)
print("firstly print the daTAFRAmes:\n",df)

print("TO FIND THE MEDIAN OF THE FOLLOWING DATAFRAMES:\n",df.median())


##                                                                  7 . STANDARD DEVIATION () FUNCTIONS

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)

print("TO FIND THE STANDARD DEVIAION OF THE DATAFRAME:\n",df.std())

##                                                               8. DESCRIBES() FUNCTIONS

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("firstly print the daTAFRAmes:\n",df)

print("TO FIND THE SUMMARY STATISTICS OF FOLLOWING DATAFRAMES:\n",df.describe())

##                                                              9 . RANGE ()FUNCTION

print("TO FIND THE RANGE OF THE FOLLOWING DATAFRAME:\n",x- z)

print("tO FIND THE VARIANCE OF DATAFRAME:\n",df.var())

##                                                              10 . CUMMULATIVE SUMS (())

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("FIRSTLY PRINT THE DATAFRAMES:\n",df)

print("TO FIND THE CUMMULATIVE SUM IN PANDAS DATAFRAMES:\n",df.cumsum())

##                                                              11. MODE FUNCTIONS(())

df= pd.DataFrame(marks,index=["marks1","marks2","marks3","marks4","marks5"],)
print("TO FIND THE MODE OF DATAFRAMES:\n",df.mode())

#                                                              PLOOTING ----><>< PANDAS 

Data= {
    "temprature": [32,65,76,87,98,89,90],
    "humidity": [76,67,87,34,24,54,54],
    "wind":[45,89,90,54,42,23,54],
    "precipitaion":[54,77,89,90,88,21,34]
}

df= pd.DataFrame(Data, index=["patna","gaya","bahadurpur","kankarbagh","hanuman nagar","boring road","musalampur halt"])
print("dataframes in pandas:\n\n",df)

df["humidity"].plot(kind='hist')

df.plot()

plt.show()

#                                                           2. HISTOGRAMS()

df["humidity"].plot(kind='hist')

plt.show()

#                                                   3. PIE-- CHART><

df.plot.pie(y="precipitaion")

plt.show()

#                                                       4. SCATTER --- PLOT><><

df.plot(kind='scatter',x='temprature',y='humidity')

plt.show()




#                                                       ##<><>------  PRACTISE QUESTIONS ON ABOVE PANDAS THEORY -------?><?>m><>

# QUESTION NO 1.. CREATE A DATAFRAME OF STUDENT MARKS AND \\ DISPLAY THE TOP 3 ROW \\ GET COLUMN NAME AND DATA TYPE \\ FIND THE AVERAGE MARKS OF EACH STUDENTS

data= {
    "names":["lucky","golu","bholu","chotu","ankit"],
    "physics":[34,68,98,100,44],
    "chemistry":[54,22,13,54,87],
    "maths":[65,66,78,98,99],
    "biology":[77,66,65,98,78],
    "bussiness studies":[44,99,88,11,32]
}

df= pd.DataFrame(data,index=["row1","ro2","row3","row4","row5"],)
print("\nFIRSTLY PRINT THE DATAFRAME:\n",df)

print("\ntO DISPLAY THE TOP 3 ROWS IN DF:\n",df.head(3))

print("\nTO GET THE DATA TYPES:\n",df.dtypes)

print("TO GET the COLUMN NAMES:\n",df.columns.tolist())

print("\nTO FIND THE AVERAGE MARKS OF EACH STUDENT:\n",df[["physics","chemistry","maths","biology","bussiness studies"]].mean(axis=1))


#               QUESTIONS NO 2.., IMPORT A CSV FILE , AND CHECK FOR, \ CHECK FOR NULL VALUE AND / REPLACE NULL VALUE WITH COLUMN MEAN

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("\nTO PRINT THE CSV IN DATAFRAMES FIRSTLY:\n",df)

print("\nCHECK FOR THE NULL NULES IN THE CSV:\n",df.isnull())
Z= df.mean(axis=0)
print("\nTO FIND THE MEAN OF COULUMN PART :\n",Z)

print("\nTO FILL THE NULL VALUE WITH COLUMN MEAN:\n",df.fillna(Z))


#      QUESTION NO 3 . ---- , SORT A DATAFRAME BY ONE COLUMN IN ASCENDING ORDER AND ANOTHER IN DESCENDING ORDER 

data={
    "ranks":[ 23,45,76,65,88],
    "marks":[34,77,98,90,100],
    "names":["lucky","golu","soviet","raushan","bholu"]
}

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5"])
print("\nFIRSTLY PRINT THE DATAFRAMES:\n",df)

X= df.sort_values(by=["ranks"])
print("\nSORTING I ASCENDING ORDER:\n",X)

Z= df.sort_values(by=["ranks"],ascending=False)
print("\nSORTING IN DESCENDING ORDER:\n",Z)


#                   QUESTIONS NO 4 ---><>< SELECT ONLY THOSE ROWS WHERE A COLUMNS VALUE IS GREATER THAN THAN A GIVEN NUMBER:::,,

data= {
    "marks":[98,90,100,76,34],
    "ranks":[34,89,99,97,95],
    "id":[22,11,34,43,22]
}

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5"])
print("\nFIRSTLY PRINT THE DATAFRAMES:\n",df)

filtered_df= df[df["marks"]>80]
print("\n STUDENT WHO HAVE GOT MARKS>80 ARE:\n",filtered_df)

## FOR MULTIPLE COLUMNS AT ONCE THEN THIS CODE ----<><<><
filtered_and=df[(df["marks"]>70)& (df["ranks"]>80)]
print("\nSTUDENT WHO HAVE MARKS >>70 AND RANKS >> 80 ARE:\n ",filtered_and)


#                 QUESTIONS NO . 5 --- \ ADD A NEW COLUMNS AS A SUM OR DIFFERENCES OF TWO EXISTING COLUMNS 

data={
    "marks":[98,90,10,76,34],
    "ranks":[34,89,99,97,95],
}

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5"])
print("\nFIRSTLY PRINT THE DATAFRAMES:\n",df)

X= df.sum(axis=1)
print("\nFIRSTLY PRINT THE SUM OF BOTH TWO EXISTING COLUMNS:\n",X)

Z= df.assign(total=X)
print("\nADDING NEW COLUMNS:\n",Z)

# ## ALTERNATIVE METHODS

df["total"]= df["marks"]+ df["ranks"]
print(df)


#               QUESTION NO 6. ----><><>\ GIVEN A DATASET OF EMPLOYEE[NAMES,AGES,DEPARTMENT,SALARY]\ FIND AVERAGE SALARY PER DEPARTMENT \\ FILTER THE EMPLOYEE EARNING MORE THAN DEPARTMENT AVERAGES

dataset={
    "names":["lucky","golu","bholu","chotu"],
    "ages":[19,23,20,22],
    "department":["officers","tax department","incometax","meterological department"],
    "salary":[34000,56000,78000,89000]
}

df= pd.DataFrame(dataset,index=["row1","row2","row3","row4"])
print("\n NOW PRINT THE DATASET IN FRAME MODE:\n",df)

## COMPUTE DEPARTMENT AVERAGE FOR EACH ROW
df['dept_avg'] = df.groupby('department')['salary'].transform('mean')

## FILTER EMPLOYE EARNING 

result= df[df['salary'] > df['dept_avg']].reset_index(drop=True)
print(result)


#              QUESTIONS NO 7.-----><>< REMOVE DUPLICATES ROWS AND RESET INDEX-----

series= ["lucky","golu","lucky","chotu","soviet","raunak singh","romi"]

s= pd.Series(series,index=["row1","row2","row3","row4","row5","row6","row7"])
print("\n FIRSTLY PRINT THE SERIES IN FRAMES:\n",s)

Z= s.drop_duplicates()
print("to delete any duplicates in series:\n",Z)

## ANOTHER METHOD TO DLETE THE ROWS AND COLUMNS
X= s.drop("row3",axis="index")
print("\n TO DLETE ANY ROW BY THIS ATTRIBUTES:\n",X)

print("\nTO RESET ANY INDEX IN SERIES:\n",s.reset_index(drop=True))
print(s[s.index[2:5]])


#                       QUESTION NO. 8 -----><><>< CONVEERT A COLUMN DATATYPES(e.g,.STRING TO DATE TIME)----

data= {
    "names":["lucky","golu","bholu"],
    "joining_date":['2023-01-10','2025-11-25','2022-06-17']
}

df= pd.DataFrame(data)
print("\n print the dataframes:\n",df)
print("\n\n",df.dtypes)
df["joining_date"]=pd.to_datetime(df["joining_date"])
print("\n\n",df.dtypes)
df["names"]=df["names"].astype(bool)
print("\n\n",df.dtypes)

#                       QUESTIONS NO 9. GROUP BY MULTIPLE COLUMNS AND FIND COUNT AND MEANS VALUES-------

data={
    "names":["lucky","golu","chotu","bholu","romi babu"],
    "id":[201,202,203,205,None],
    "ranks":[23,34,None,21,11],
    "marks":[89,90,88,77,65]
}

df= pd.DataFrame(data,index=["row1","row2","row3","row4","row5"],)
print("\nPRINT THE DATAFRAMES FIRSTLY :\n",df)

res=df[df.columns[0:3]]
print("\nTO FIND THE MULTIPLE COLUMNS AT ONCE:\n",res)

print("\n TO FIND THE COUNT VALUES:",df.count())

print("\n\nTO FIND THE MEAN VALUE IN THIS DATAFRAMES=\n",df[["id","ranks","marks"]].mean(axis=0)) 

df[["id","ranks","marks"]]=df[["id","ranks","marks"]].astype(float)
print("\n\n",df.dtypes)

df["totals"]=df["id"]+df["ranks"]+df["marks"]
print(df)


#                           QUESTIONS NO 10. -------><><>< MERGE TWO DATAFRAMES (LIKE EMPLOYEE & DEPARTMENT INFO ) AND PERFORM AN INNER JOIN

data1={
    "employees names":["lucky","golu","raushan","bholu","chotu","romi sarkar"]
}

df1= pd.DataFrame(data1)
print("\n\n",df1)

data2= {
    "department info":["income tax","excise inspectors","meterogical department","police inspector","clerkical post","cid inspectors"]
}

df2= pd.DataFrame(data2)
print("\n\n",df2)

## NOW TO JOIN BOTH DATAFRAMES:==

resdf= df1.join(df2)
print("\n\n TO JOIN BOTH DATAFRAMES BY JoiN METHODS AND ATTRIBUTES:\n",resdf)


##                     QUESTION NO. 11 \  FROM A CSV FILES OF SALES DATA (DATE, REGION, SALES),\ FIND TOTAL MONTHLY SALES \\ PLOT SALES TREND USING MATPLOTLIB OR SEABORN 

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\demonew.csv")
print("\n FIRSTLY PRINT THE CSV FILE IN DATAFRAMES:\n",df)

X= df["SALES"].sum(axis=0)
print("\n TOTSL MONTHLY SALES:\n",X)

df.plot.pie(y="SALES")

plt.show()





##                                          PANDAS PROJECTS ------------><><><><?<><><\\\\\\

#                               1.  STUDENTS MARKS ANALYZERS --------><><<><\\\/?????

print("\n\n ------- ><>< STUDENTS MARKS ANALYZERS 🧮✔️🙌---------><><><\n")

df= pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\student_marksnews.csv")
print("\n PRINT THE CSV FIRSTLY IN DATAFRAMES:\n",df)

print("\n\n  VARIOUS OPERTIONS ON UPPER FUNCTIONS-----><><\n")
print("\n\n TOTALS SUM OF ALL MARKS")
df["TOTALS"]=df["PHYSICS"]+df["CHEMISTRY"]+df["MATHEMATICS"]+df["BIOLOGY"]
print(df)


print("\n\n AVERAGE OF ALL MARKS IN EACH SUBJECTS:\n")

mean_data= df[["PHYSICS","CHEMISTRY","MATHEMATICS","BIOLOGY"]].mean(axis=0)
print("\n\n  AVERAGE IN EACH SUBJECTS:\n",mean_data)

print("\n\n --- MEDIAN OF ALL STUDENTS:--------\n")

median= df[["PHYSICS","CHEMISTRY","MATHEMATICS","BIOLOGY"]].median(axis=0)
print("\n\n---- MEDIAN OF EACH SUBJECTS:\n",median)

print("\n\n----->< MODE OF ALL STUDENTS------\n")

mode= df[["PHYSICS","CHEMISTRY","MATHEMATICS","BIOLOGY"]].mode(axis=0)
print("\n MODE OF ALL SUBJECTS:---\n",mode)

print("\n\n------>< TO FIND THE TOPPERS BETWEEN THE ALL STUDENTS:\n")
topper=df.loc[df["TOTALS"].idxmax()]
print("\n\n----><> TOPPERS of all tHE SUBJECTS:\n",topper)

print("\n\n-----><>< HIGHEST MARKS PER SUBJECTS :\n")

X=(df[["BIOLOGY","MATHEMATICS","PHYSICS","CHEMISTRY"]].max())
print("\n\n",X)

print("\n\n----><< LOWEST MARKS PER SUBJECTS:----\n")

Z=(df[["BIOLOGY","MATHEMATICS","PHYSICS","CHEMISTRY"]].min())
print("\n\n",Z)

print("\n\n RANGE OF THE UPPER FUNCTIONS:\n")
print("\n\n RANGE =",X-Z)

print("\n\n-----><>< TO VISUALIZES THIS ALL DATA ON FRESH GRAPHS AND CHARTS:----\n")

df.plot("PHYSICS","CHEMISTRY",color=["red","blue","orange","black"],label=" 2025 STUDENT MARK ANALYZERS",marker="^")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS OBTAINED")
plt.legend()
plt.title("STUDENTS MARKS ANALYZERS")
plt.grid(color="blue",linestyle="--")
plt.show()


print("\n\n----><>< ALL OPERATIONS DONE✔️✔️ SUCCESFULLY ❤️🎉🎉-----") 
