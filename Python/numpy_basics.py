import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#                                           THE ARRAYS                       

array= np.array(["lucky","bholu","golu","chotu","raunak"])
print(array)
print("reshaped the following array:\n",array.reshape(5,1))

array_2d= np.array([[23,45,76,87],[43,89,90,99]])
print(array_2d)
print(array_2d.ndim)
print("reshaped in form of matrix:\n",array_2d.reshape(4,2))

np_array= np.array([1,2,3,4])
print("arrayas:",np_array)
print("RESHAPED ARRYA:\n",np_array.reshape([4,1]))

array_3d= np.array([[[23,43,54],[65,98,90],[45,76,98]]])
print("\n ARRAY IN 3D TYPE LETS SEE:\n",array_3d)
print("\n\n ARRAY DIMENSIONS:\n", array_3d.ndim)

                                           DIFFERENCE IN LIST AND ARRAYS

py_list= [2,3,5,6]
print("py.lists:",py_list*3)

array= np.array([2,3,4,6,8])
print("np.arrays:\n",array*3)
print(np.tile(array,5))

array= np.identity(3)
print("\n IDENTITY MATRICES:\n",array)
array_1= np.fill_diagonal(array,7)
print(array_1)
#                                           ARRAYS METHODS                      


zeros= np.zeros([3,3])
print("ZEROS ARRYAS:\n",zeros)

ones= np.ones([3,5])
print("ONES ARRAYS:\n",ones)
print("to transform it in simple 1d array:\n",ones.ravel())


FULL= np.full([3,3],34)
print("FULLS ARRYAS:\n",FULL)

sequence= np.arange(0,12,2)
print("SEQUENCE ARRYAS:\n",sequence)
reshaped=sequence.reshape([3,2])
print("reshaped array:\n",reshaped)
print("Transpose of arryas:\n",reshaped.T)

random= np.random.random([3,4])
print("RANDOM ARRYAS:\n",random)

random_2= np.random.randint(1,101,(3,4))
print("\n ARRAY IN MATRICES FORM BY RANDOM METHODS:\n",random_2)
print("\n NOW FALTTEN OR RAVEL THIS MATRICE IN 1 D FORMAT:\n",random_2.ravel())
print("\n TRANSPOSE OF THE UPPER MATRICES:\n",random_2.T)

                                      VECTORS/ MATRICES/ TENSORS DIFFERENCES


VECTOROS= np.array([4,5])
print("VECTOR:\n",VECTOROS)
print("shape of array:",VECTOROS.shape)
print(VECTOROS.ndim)
print(VECTOROS.size)
print(VECTOROS.dtype)

matrices= np.array([[1,2,3],[4,5,6],[77,87,90]])
# print("matrices:\n",MATRICES)
print("shape of array:",matrices.shape)
print(matrices.ndim)
print(matrices.size)
print(matrices.dtype)


tensors= np.array([[[1,2,6],[3,4,5],[6,9,8],[7,5,4],[34,76,89]]])
print("tensor:\n",tensors)
print(tensors.ndim)
print(tensors.shape)
print(tensors.size)
print(tensors.dtype)


                                          ARRAYS PROPERTY                 

x= np.array([[1,3,5],[3,2,6],[7,0,8]])

print("ARRAYS IN NUMPY:\n",x)

print("shape:\n",x.shape)

print("DIMENSION:\n",x.ndim)


print("SIZE:\n",x.size)


print("DTYPE:\n",x.dtype)



#                                      ARRAYS RESHAPING                

array= np.arange(12)
print("OREIGINAL ARRAY:\n",array)

reshaped= array.reshape([4,3])
print("reshaped array:\n",array.reshape([4,3]))

# flattend= reshaped.flatten()
print("FLATTEND ARRYA:\n", reshaped.flatten())

# raveled=  reshaped.ravel()
print("RAVELED ARRAY:\n", reshaped.ravel())

# transpose=  reshaped.t
print("TRANSPOSE ARRYA:\n",reshaped.T)

                                               INDICES AND SLICING                

arr_1d= np.array([2,4,6,8,10,12,14,16,18])
print(arr_1d)

print("for any specific element:\n",arr_1d[3])

print("basic slicing:",arr_1d[1:6])

print("with step:",arr_1d[1:7:2])

print("negative indexing:",arr_1d[-5])

print("\n FOR ALL FROM LEFT SIDE ONLY :\n",arr_1d[:6])

print("\n FOR ALL RIGHT  SIDE:\n",arr_1d[1:])

print("\n ALL VALUES NO SLICINGS:\n",arr_1d[:])

                                          SLICING IN 2- D                 

arr_2d= np.array([[1,2,3],[4,5,7],[8,9,0]])
print("basoic printing:\n",arr_2d)

print("\n FOR SPECIFIC ROW:\n",arr_2d[2])

print("specific element:\n",arr_2d[0,1])  # it means o row ka 1 colomun   # 2

print("entire row:\n",arr_2d[:])          # # for entire ROW

print("for specific range:\n",arr_2d[0:2])

print("entire coloumn:\n",arr_2d[:,0:])   # for entire colomn



                                          SORTING             

unsorted_1d= np.array([1,3,9,7,5,2,6,0])
print("sorted array:",np.sort(unsorted_1d))

#                                          IN 2D SORTINGS

unsorted_2d= np.array([[3,1],[1,2],[2,4]])
print(unsorted_2d)
print("sorted 2d array by column:\n",np.sort(unsorted_2d,axis=0))


                                              FILTERS IN ARRAYS

numbers= np.array([1,2,3,4,5,6,7,8,9,10])

even_number= numbers[numbers % 2== 0]
print("EVEN NUMBER:",numbers[numbers % 2== 0])


#                                               FILTER WITH MASKS                   

mask=numbers[numbers > 5]
print("NUMber greater than 5",mask)

print("divisible by 3 :\n",numbers[numbers % 3== 0])


                                              FANCY INDEXING VS NP.WHERE                  

indices= [0,2,4]
print(numbers[indices])

where_result= np.where(numbers> 5)
print(where_result)
print("np where",numbers[where_result])


#                                              ADDING AND REMOVING DATA ARRAYS
  
arr1= np.array([2,4,6]) 
arr2= np.array([8,10,12])
arr3= np.array([98,66,90])

print("combined:\n",np.concatenate((arr1,arr2,arr3)))

                                                 ARRAYS COMPATIBILITY                 

a= np.array([1,2,3])
b= np.array([4,5])
c= np.array([8,9])

print("COMPATIBILITY SHAPE:\n",a.shape== c.shape)
print("COMPATIBILITY SHAPE:\n",a.shape== b.shape)
print("COMPATIBILITY SHAPE:\n",b.shape== c.shape)

original= np.array([4,5,6])
new_row= np.array([89,90,91])
adding= np.vstack((original,new_row))
print("combined:\n",adding)
print("MATRIX FORM:\n",adding.reshape((3,2)))   # V.STACK SE HAM ROW ADD HOGA BUT COCANTANETE SE SIDHA ARRYA KE TYPE ME ANS AAYEGA

with_new_row=np.vstack((original,new_row))
print(original)
print(with_new_row)


#                                                  DELETING A ARRAYS 

arr= np.array([2,4,6,8,10])
deleted= np.delete(arr,4)

print("array after deletion:\n",deleted)



                                      ADVANCE OPERATION WITH BUSSINESS EXAMPLES           

data_structure = ["restaurant id", 2021,2022,2023,2024,2025]

sales_data= np.array([
    [1,220000,110000,320000,430000,145000],#  biryani hyderabadi
    [2,650000,540000,760000,870000,980000],#  chibnese restaurabt
    [3,340000,430000,440000,560000,870000],#  zomatao restautant
    [4,550000,990000,760000,590000,320000],#  swiggy restautant
    [5,220000,540000,440000,320000,120000] #  chicken tikka masala
])

print("shape of the following data\n",sales_data.shape)
print("for dimensions of the following data :\n",sales_data.ndim)
print(sales_data)

# print("===== ZOMATO SALES ANALYSIS===== ")

print("\n sales data for 1st 3rd:",sales_data[0:3]) # IT MEANS 0 ROW SE 3 ROW TAK SAB 

print("\n for entire row",sales_data[3])

print("\n data for the 1st three only:\n",sales_data[0:2])

print("\n ENTIRE COLOUMN",sales_data[:,2])

print("\n sales data for all yea:\n",sales_data[:,1:4])

print("for specific element:\n",sales_data[2,2])


                                    VARIOUS METHODS ON  UPPER DATA

                  1. TOTAL SALES PER YEAR

total_sales= np.sum(sales_data[:,:],axis=0)
print("total sales per month :\n",total_sales)

yearly_total=np.sum(sales_data[:,1:],axis=0)
print(yearly_total)

diff_sales= np.diff(sales_data,axis= 1)
print("substraction in sales data:\n",diff_sales)


# #                  2. MINIMUM SALES PER RESTAURANT

min_sales= np.min(sales_data[:,1:],axis=1)

print("MINIMUM SALES PER RESTAURANT:\n",min_sales)


 ##                 3. MAXIMUM SALES PER YEARS 

max_sales= np.max(sales_data[:,1:],axis=0)

print("MAXIMUM SALES PER YEAR:\n",max_sales)

# #                   4. AVERAGE SALES PER RESTAURANT

avg_sales= np.mean(sales_data[:,1:],axis=1)
print(avg_sales)

##                    5. MEDIAN OF ALL DATA 

print("median of all data:\n",np.median(sales_data,axis=1))

#                   5. COMMULATIVE SUMS 

cum_sum= np.cumsum(sales_data[:,1:],axis=1)

print("COMMULATIVE SUM PER RESTAUTRANT:\n",cum_sum)


##                                     FOR FIGURES                                                     


plt.figure(figsize=(10,6))
plt.plot(np.min(cum_sum,axis=0))
plt.title("AVERAGE COMMULATIVE SALES ACROSS ALL RESTAUTANT")
plt.xlabel("years")
plt.ylabel("SALES")
plt.grid(True)
plt.show()


#                                              VECTORS    
vec1= np.array([1,2,3])
vec2= np.array([6,7,8])

print("vector addtion:\n",vec1+vec2)
print("vector substraction:\n",vec2- vec1)
print("vector multiplication:\n",vec1@vec2)
print("dot product of vectors:\n",np.dot(vec1,vec2))
print("vector cross product:",np.cross(vec1,vec2))



#                                   FOR ANGLES IN VECTORS           

angle= np.arccos(np.dot(vec1,vec2)/np.linalg.norm(vec1)*np.linalg.norm(vec2))

print(angle)


#                                  BROADCASTINGS 

restaurant_types= np.array(['biryani','chinese','pizza','burgers','cafe'])

vectorized_upper=np.vectorize(str.capitalize)

print("vectorized upper:\n",vectorized_upper(restaurant_types))

monthly_avg= sales_data[:,1:]/12
print(monthly_avg)


#                                              HOW TO PRINT SOME DATA ON THE RESPECTED GRAPH

try:
    logo= np.load('numpy-logo.npy')

    # display
    plt.figure(figsize=(10,5))
    plt.subplot(121)
    plt.imshow(logo)  
    plt.title("numpy logo")
    plt.grid(False)  
    plt.show()

except FileNotFoundError:
    print("numpy logo not found")
    
                                  ANOTHER ONE BECAUSE UPPER CODE DIIDNT WORK


"create a blank canvas(blue background)"
logo = np.zeros((200, 200, 3))   # 200x200 pixels, 3 channels (RGB)
logo[:, :] = [0.0, 0.3, 0.7]     # set everything to blue (R=0, G=0.3, B=0.7)

# Draw a white "N" shape
logo[40:160, 60:80] = [1, 1, 1]   # left vertical bar
logo[40:160, 120:140] = [1, 1, 1] # right vertical bar
for i in range(40, 160):
    logo[i, (i-40)//2 + 80] = [1, 1, 1]  # diagonal connector for N

# Display the fake logo
plt.figure(figsize=(5,5))
plt.imshow(logo)
plt.title("Fake NumPy Logo")
plt.axis("off")
plt.show()



#                                          NUMPY PRACTISE QUESTIONS FOR MORE CLEARNESS

# Q.NO 1

np_arrya= np.arange(1,21,1)
print("numpy array:\n",np_arrya)
X=np_arrya.reshape(4,5)
print("\n RESHAPINING THE UPPER ARRAY:\n",X)
print("\n TO TRASNSPOSE THE UPPER MATRICES :\n",X.T)
np_mean= np.mean(np_arrya)
print("numpy mean :\n",np_mean)

np_median= np.median(np_arrya)
print("np median:\n",np_median)

np_deviation= np.std(np_arrya)
print("standsard deviation:\n",np_deviation)

max= np.max(np_arrya)
print("\n MAXIMUM VALUES OF THE UPPER ARRYA:\n",max)

# Q.NO 2

arrya= np.arange(16,50,3)                         ## DO METHOD HAI EK YE AUR EK NICGHE WLAA           
arrya= np.random.randint(10,51,size=(3,4))
print("random number:\n",arrya)
reshaped= arrya.reshape([3,4])
print("reshaped arrya:\n",reshaped)

maximum= np.max(arrya,axis=1)
print("maximum:\n",maximum)

minimum= np.min(arrya,axis=0)
print("minimum :\n",minimum)

# Q.NO 3

identity= np.identity(3)
print("identity matrix:\n",identity)

identity[np.eye(5,dtype=bool)]= 7
print("REPLACE DIAGONAL:\n",identity)

np.fill_diagonal(identity,7)
print(identity)


# Q.NO 4

arrya_1d= np.random.randint(1,100,15)
print(arrya_1d)
simple= arrya_1d.ravel()
print(simple)

# sorting= np.sort(simple)
sorting= np.sort(arrya_1d)
print("SORTING OF ARRYA:\n",sorting)

third_largest= sorting[-3]
print("3 RD LARGEST NO:\n",third_largest)




# Q.NO 5

random= np.random.randint(1,101,size=(6,6))
print("RANDOM ARRYA:\n",random)

submatrix= random[1:5, 1:5]
print("MIDDLE 4*4 SUBSTRACTION:\n",submatrix)

flatten= random.flatten()
print("simple 1d arrya:\n",flatten)


# Q.NO 6

array= np.array([1,2,3])
print(array)

repeat= np.tile(array,3)
print(repeat)

# Q. NO 7  \\ CREATE A 1D ARRAY OF SIZES 100 WITH RANDOM INTEGER 

array= np.random.randint(1,200,100)
print("\n RANDOM INTEGER OF SIZE 100 :\n",array)

unique= np.unique(array)
print("\n UNIQUE VALUES OF UPPER ARRAY:\n",unique)

#           1 ....                                           NUMPYS MINI PROJECTS 

###                                                MATRIX VISULATION CALCULATORS BY NUMPYS

print(" ### 🎲🧮 MATRIX CALCULATOR BY NUMPY FUNCTIONS 🧮 ###@@")   

# --- Matrix Visualizer ---

print("\n🎨 MATRIX CALCULATORS VISUALIZER 🎨\n")

# Step 1: Take matrix size input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Step 2: Generate random matrices A and B
A = np.random.randint(1, 20, (rows, cols))
B = np.random.randint(1, 20, (rows, cols))

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Step 3: Perform operations
print("\n----------------------------")
print("🔹 MATRIX ADDITION (A + B):")
print(A + B)

# Step 4 : Substractions functions
print(" \n ---------------")
print("Matrixs substractions ( A- B):")
print(A-B)

# Only multiply if dimensions are valid
if A.shape[1] == B.shape[0]:
    print("\n🔹 MATRIX MULTIPLICATION (A × B):")
    print(A @ B)
else:
    print("\n❌ Cannot multiply A and B (shape mismatch).")

print("\n🔹 TRANSPOSE OF A:")
print(A.T)

print("Transpose of B:\n")
print(B.T)

# Step 4: Determinant and inverse (only if square matrix)
if A.shape[0] == A.shape[1]:
    det = np.linalg.det(A)
    print("\n🔹 DETERMINANT OF A:")
    print(round(det, 0))

if  B.shape[0] == B.shape[1]:
    print("DETerminant of B :\n")
    print(np.round(np.linalg.det(B),0))

    if det != 0:
        inv= np.linalg.inv(A)
        print("\n🔹 INVERSE OF A:")
        print(np.round(inv,0))
        # print(np.round(np.linalg.inv(A), 0))
    else:
        print("\n❌ Inverse not possible (Determinant = 0).")
else:
    print("\n❌ Determinant and inverse only for square matrices.")

print("\n----------------------------")
print("✅ All operations completed successfully!")


## NUMPY PROJECTS REVISIONS

print("❤️🙌 \n MATRIX CALUCULATORS USING NUMOYS FUNCTIONS 🧮🎲")

#MAKE THE INPUT OF ROW AND COLUMN FOR LATER USES

rows= int(input("entered the rows:"))
columns= int(input("entered the columns:"))

#now make THE ANY TWO RANDOMS MATRICES

A= np.random.randint(1,40,(rows,columns))
B= np.random.randint(1,40,(rows,columns))

print("----------><><>")
print("Matrix A:\n\n",A)
print("Matrixs B:\n\n:",B)

## nows MATRICES OPERSTIONS

print("\n --------------<>")
print("MATRICES ADDITION(A+B)")
print(A+B)

print("\n\n---------------<>")
print("matrices substractions:(A-B)")
print(A-B)

## FOR MULTIPLICATIONS
print("\n----------<>")
if A.shape[1] == B.shape[0]:
    print("MATRIX MULTIPLICATIONS:[A*B]")
    print(A*B)

else:
    print("❌❌ ERROR OCURED BECAUSE OF SHAPE DISORDER")   

## FOR TRANSPOSE OF A AND B 
print("\n___________><><")
print("TRANSPOSE OF A:\n\n",A.T)   
print("\n___________><><")
print("TRANSPOSE OF B:\n\n",B.T)   

## FOR DETERMINANTS AND INVERSES OF MATRICES (if only the matrices are squares ) rows== columns
print("\n\n___---------><><><")
if A.shape[0]== A.shape[1]:
    detA= np.linalg.det(A)
    print("DETERMINANTS OF A :\n\n",np.round(detA,0))

if B.shape[0]== B.shape[1]:
    detB= np.linalg.det(B)
    print("DETERMINANTS OF B :\n\n",np.round(detB,0))

## FOR INVERSES IN MATRICES
if detB!= 0:
    inv=(np.linalg.inv(A))
    print("INVERSE OF MATRICES:\n",np.round(inv,0))

else:
     print("CANNOT FIND THE INVERSE BCZ (DETERMINAT ==0)")


print("❤️🎉🎉 ALL OPERATIONS HAD DONE SUCCESFULLY")


## NUMPYS SECONDS PROJECTS

print("🎲🤦‍♀️\n ARRYAS STATISTICS FINDERS :><><><------❤️🧮🤞")

--- Step 1: Take user input ---
You can skip input() and directly define an array if you want

X= list(map(float,(input("Enter numbers separated by space: ").split())))
arr = np.array(X)

# --- Step 2: Compute statistics ---
mean = np.mean(arr)
median = np.median(arr)
mode = stats.mode(arr, keepdims=True).mode[0]  # returns most frequent value
variance = np.var(arr)
std_dev = np.std(arr)
minimum = np.min(arr)
maximum = np.max(arr)
range_ = maximum - minimum
sum_ = np.sum(arr)

# --- Step 3: Display results ---
print("\n===== ARRAY STATISTICS =====")
print("Array:", arr)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_}")
print(f"Sum: {sum_}")

print("\n\n YOUR OPERATION ARE SUCCESFULLY DONED ✔️✔️")


#      PROJECTS 3.  STUDENTS MARKS ANALYZERS 

print(" --------------><><><>< ")
print("✔️🎉💕\n STUDENT MARKS ANALYZERS :-------")

# MARKS= np.array([[54,56,67,98,90],[98,21,34,22,87]])
MARKS=np.random.randint(10,40,size=[3,4])
print("numpys arrays:--\n\n",MARKS)

## VARIOUS OPERATIONS ON UPPER ARRYAS

get_sum= np.sum(MARKS,axis=1)
print("-- for total sum of all subjects:\n\n ",get_sum)

max= np.max(MARKS,axis=1)
print("------><\n MAXIMUM OF EACH SUBJECTS:\n")
print(max)

min= np.min(MARKS,axis=1)
print("------><\n MINIMUM OF ALL SUBJECTS:\n")
print(min)

average= np.mean(MARKS,axis=1)
print("--->< \nMEANS OF ALL EACH SUBJECTS:\n\n")
print(average)

middle_value= np.median(MARKS,axis=0)
print(" ------><\n MEDIAN OF EACH SUBJECTS:\n\n")
print(middle_value)

std_dev= np.std(MARKS,axis=1)
print("----><>< \nSTANDARD DEVISTION OF SUBJECTS:\n\n")
print(std_dev)

variance= np.var(MARKS,axis=1)
print("------><>< \nVARIANCCE OF SUBJECTS:\n\n")
print(variance)

range= max - min
print(" ------><\n RANGE OF THIS ARRYAS:\n\n")
print(range)

mode=stats.mode(MARKS,keepdims=True).mode[0]
print("----><><\n MODE OF THE SUBJECTS:\n\n")
print(mode)

cum_sum= np.cumsum(MARKS,axis=0)
print("\n COMMULATIVE SUM OF UPPER ARRAY:\n",cum_sum)



print("------\n\n✔️🎉🎉 ALL  OPERATIONS EXECUTED SUCCESFULLY ---------🤞🙌❤️")
