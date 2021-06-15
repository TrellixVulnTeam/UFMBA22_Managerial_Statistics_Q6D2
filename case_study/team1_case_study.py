
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os, sys


dirpath = os.path.dirname(os.path.realpath(__file__))
#dirpath = os.path.dirname(os.path.realpath('/mnt/g/programing_projects/UFMBA_stats/UFMBA22_Managerial_Statistics/case_study'))


# This is the file that will return all of the answers for the case project
def question_1():
    # Question 1
    print("QUESTION 1")
    print("========================================")
    # this will utilize the CEOSAL2.XLS file

    # df is a pandas dataframe object
    df = pd.read_excel(dirpath+'/CEOSAL2.xls')

    # Question 1 part i

    #average salary
    print("Question 1, Part I")
    print("Average salary")
    print(df['lsalary'].mean())
    print("\n")

    # average tenure
    print("Average tenure")
    print(df['ceoten'].mean())
    print("\n")

    # Question 1 part II

    # beginner CEOs
    print("Question 1, Part II")
    print("how many CEOs are in their first year as CEO?")
    print(df['ceoten'].value_counts()[0])
    print("\n")

    #longest running CEO
    print("What is the longest tenure as a CEO")
    print(df['ceoten'].max())
    print("\n")

    # Question  1 part III
    print("Question 1, Part III")
    print("simple regression result")

    # independent variable
    x = df['ceoten'].to_numpy().reshape((-1,1))
    y = np.log(df['salary'].to_numpy())
    
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    
    #intercept is b0
    print('intercept: {}'.format(model.intercept_))
    print("\n")

    # b1 is the predicted response per x
    print('slope: {}'.format(model.coef_[0]))
    print("\n")


    print('r_squared: {}'.format(r_sq))
    print("\n")

    print('predicted percentage increase given one more year as CEO: {} %'.format(np.round(model.coef_[0], decimals=6)*100))
    print("\n")
    
    


def question_2():
    
    # Question 2
    print("QUESTION 2")
    print("========================================")
    # this will utilize the WAGE2.XLS file
    # df is a pandas dataframe object
    df = pd.read_excel(dirpath+'/WAGE2.xls')

    # Question 2, part I
    print("Question 2, Part I")
    print("\n")

    print("Average salary ")
    print(df['lwage'].mean())
    print("\n")

    print("Average IQ")
    print(df['IQ'].mean())
    print("\n")

    print("IQ Standard deviation")
    print(df['IQ'].std())

    #Question 2, part2
    print("Question 2, Part II")
    print("\n")

    x = df['IQ'].to_numpy().reshape((-1,1))
    y = df['wage'].to_numpy()

    model = LinearRegression().fit(x, y)
    r_sq = model.score(np.log(x), y)
    intercept = model.intercept_
    coef = model.coef_[0]
    print(r_sq)
    print(intercept)
    print(coef)

    

# df.plot(x='IQ', y='wage', style='o')
# plt.title('IQ VS Wage')
# plt.xlabel('IQ')
# plt.ylabel('wage')
# plt.show()


# printing results to results.txt file
# original_stdout = sys.stdout
# with open(dirpath+'/results.txt', 'w') as f:
#     sys.stdout = f
#     print(question_1())
#     print("\n")
#     print(question_2())
#     sys.stdout = original_stdout
print(question_2())



# %%
