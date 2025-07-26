from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
X = wine_quality.data.features 
y = wine_quality.data.targets 
  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import torch
from torch.utils.data import TensorDataset , DataLoader
import torch.nn as nn 
import torch.optim as optim


df = pd.concat([X.reset_index(drop=True), y.reset_index(drop=True)], axis=1)



class_count = df['quality'].value_counts().sort_index()

print(class_count)


mapping = {3: 00 , 4:00 , 5:00,
           6:1,
           7:2,8:2, 9:2}

df['quality'] = df['quality'].map(mapping)

class_count = df['quality'].value_counts().sort_index()

print(class_count)

plt.figure(figsize=(10, 6))
plt.bar(class_count.index.astype(str), class_count.values, color='skyblue')
plt.title('Distribution of Wine Quality Classes')
plt.xlabel('Quality Class')
plt.ylabel('Count')
plt.savefig('wine_quality_distribution.png', dpi = 100)

# Correlation Heatmap
num_df = df.drop(columns=['quality'])
corr = num_df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.savefig('wine_quality_correlation_heatmap.png', dpi = 100)

# Split the data into features and target
X = df.drop(columns=['quality'])
y = df['quality']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


class MpalaourasNN(nn.Module):
    def __init__(self , features_number , number_classes):
        super().__init__()
        self.mpalaouras = nn.Sequential(
            nn.Linear(features_number,32),
            nn.LeakyReLU(),
            nn.Linear(32,64),
            nn.LeakyReLU(),
            nn.Linear(64,128),
            nn.LeakyReLU(),
            nn.Linear(128,256),
            nn.LeakyReLU(),
            nn.Linear(256,128),
            nn.LeakyReLU(),
            nn.Linear(128,64),
            nn.LeakyReLU(),
            nn.Linear(64,32),
            nn.LeakyReLU(),
            nn.Linear(32,number_classes)
        )
    def forward(self, x):
        return self.mpalaouras(x)
    

X_train=torch.tensor(X_train , dtype = torch.float32)
X_test=torch.tensor(X_test, dtype = torch.float32)
y_train=torch.tensor(y_train.values , dtype = torch.long)
y_test=torch.tensor(y_test.values , dtype =torch.long) 
print(y_test.shape[0])
print(X_train.shape[0])
train = TensorDataset(X_train,y_train)
test = TensorDataset(X_test, y_test)

train = DataLoader(train , batch_size=32)
test = DataLoader(test ,batch_size=8)
print(len(train))

number_classes = len(y_train.unique())

model = MpalaourasNN(X_train.shape[1],number_classes)
loss_function = nn.CrossEntropyLoss()
optimazer = torch.optim.Adam(model.parameters(), lr = 0.001)

val_loss_mean, val_loss_accur =[], []
train_losses,train_acc =[], []

for epoch in range(1,100):
    model.train()
    total_loss_epoch =0
    acc_train_epoch =0 
    for xbatman , ybatman in train:
        out=model(xbatman)
        loss =loss_function(out, ybatman)
        total_loss_epoch += loss
        acc_train_epoch +=(torch.argmax(out)==ybatman).sum()
        optimazer.zero_grad()
        loss.backward()
        optimazer.step()
    train_losses.append(total_loss_epoch/len(train))
    train_acc.append(acc_train_epoch/len(train))
    # print(train_losses)
    # print(train_acc)

    model.eval()
    val_loss =0
    val_correct =0
    totalsamples =0
    with torch.no_grad():
        for x_test , y_test in test:
            out_val=model(x_test)
            val_loss += loss_function(out_val,y_test)
            val_correct += (torch.argmax(out_val) == y_test).sum()
            totalsamples += y_test.size(0)
    val_loss_mean.append(val_loss/len(test))
    val_loss_accur.append(val_correct /totalsamples)
    print("-------------------------------------------------")
    print(f"--------------------EPOCH({epoch})-----------------------")
    print("-------------------------------------------------")
    print(val_loss_mean[-1])
    print(val_loss_accur[-1])

