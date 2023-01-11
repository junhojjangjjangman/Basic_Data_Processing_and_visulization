import pandas as pd
import matplotlib.pyplot as plt
dir = 'C:/Users/15/Desktop/DataSet/'
df = pd.read_csv(dir+'[Dataset]_Module_17_iris.data')
print(df.head())
names = ["sepal_length", "sepal_width","petal_length", "petal_width", "class"]
df.columns = names
print(df.head())
print(df.describe())

plt.figure(figsize=(12, 4));
plt.subplot(141);plt.boxplot(df['sepal_length'],showfliers=True,labels=['sepal length'])
plt.subplot(142);plt.boxplot(df['sepal_width'],showfliers=True,labels=['sepal length'])
plt.subplot(143);plt.boxplot(df['petal_length'],showfliers=True,labels=['sepal length'])
plt.subplot(144);plt.boxplot(df['petal_width'],showfliers=True,labels=['sepal length'])
plt.tight_layout()
plt.show()

figure, axis = plt.subplots()
axis.boxplot([df['sepal_length'],df['sepal_width'],df['petal_length'],df['petal_width']],
            showfliers=True,labels=['sepal length','sepal width','petal length','petal width']);
plt.show()

plt.hist(df['sepal_length'],bins=20,range=(4,8))
plt.title('Sepal Length');
plt.show()

plt.scatter(df['petal_length'],df['petal_width'])
plt.xlabel('petal length')
plt.ylabel('petal width');
plt.show()

# 데이터 프레임을 3개의 클래스로 분할
df_Setosa = df[df['class'] == 'Iris-setosa']
df_Versicolor = df[df['class'] == 'Iris-versicolor']
df_Virginica = df[df['class'] == 'Iris-virginica']
# 다른 컬러를 이용하여 클래스를 구분합니다. c=색상 제어, label=범례에 표시된 이름 제어
plt.scatter(df_Setosa['petal_length'],df_Setosa['petal_width'],c='r',label='Setosa')
plt.scatter(df_Versicolor['petal_length'],df_Versicolor['petal_width'],c='b',label='Versicolor')
plt.scatter(df_Virginica['petal_length'],df_Virginica['petal_width'],c='g',label='Virginica')
# 축 및 범례 추가
plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()