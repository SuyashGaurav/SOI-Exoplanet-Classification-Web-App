import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from xgboost import XGBClassifier
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
tce_data = pd.read_csv("problem_dataset.csv")

tce_data["av_training_set"]= tce_data["av_training_set"].replace(['AFP', 'NTP', 'PC'], [0,1,2])

tce_data = tce_data[tce_data.av_training_set!='UNK']


X = tce_data.drop(['kepid', 'tce_plnt_num', 'tce_insol', 'tce_insol_err', 'tce_rogue_flag', 'av_training_set'], axis =1)
y = tce_data['av_training_set']

y=y.to_numpy()
y=y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0)

# forest = RandomForestClassifier(n_estimators=200, criterion='gini',max_depth=13)
#
# forest.fit(X_train, y_train)
# y_pred = forest.predict(X_test)
#
# print(classification_report(y_test, y_pred))
#
# print(accuracy_score(y_test,y_pred))

xgb = XGBClassifier(learning_rate=0.02, n_estimators=600, objective='multi:softprob',
                    silent=True, nthread=8)

xgb.fit(X_train,y_train)


pickle.dump(xgb, open('siemen.pkl', 'wb'))

y_pred1=xgb.predict(X_test)



print(classification_report(y_test, y_pred1))

print(accuracy_score(y_test,y_pred1))

cm = confusion_matrix(y_test,y_pred1)



ax= plt.subplot()
sns.heatmap(cm, annot=True, fmt='g', ax=ax);
ax.set_xlabel('Predicted labels');
ax.set_ylabel('True labels');

plt.show()