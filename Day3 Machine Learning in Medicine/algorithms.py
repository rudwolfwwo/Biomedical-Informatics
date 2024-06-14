#-----------------------------------------------------#
#                   Library imports                   #
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
#-----------------------------------------------------#

#-----------------------------------------------------#
#                 Logistic Regression                 #
#-----------------------------------------------------#
class Logistic_Regression:
    def __init__(self):
        self.modul = LogisticRegression()

    def train(self, train_x, train_y):
        return self.modul.fit(train_x, train_y)

    def predict(self, data):
        return self.modul.predict(data)

class Naive_Bayes:
    def __init__(self):
        self.modul = GaussianNB()

    def train(self, train_x, train_y):
        return self.modul.fit(train_x, train_y)

    def predict(self, data):
        return self.modul.predict(data)

class Support_Vector_Machine:
    def __init__(self):
        self.modul = svm.SVC()

    def train(self, train_x, train_y):
        return self.modul.fit(train_x, train_y)

    def predict(self, data):
        return self.modul.predict(data)

class K_Nearest_Neighbor:
    def __init__(self):
        self.modul = KNeighborsClassifier()

    def train(self, train_x, train_y):
        return self.modul.fit(train_x, train_y)

    def predict(self, data):
        return self.modul.predict(data)

class Random_Forest_Classifier:
    def __init__(self):
        self.modul = RandomForestClassifier()

    def train(self, train_x, train_y):
        return self.modul.fit(train_x, train_y)

    def predict(self, data):
        return self.modul.predict(data)