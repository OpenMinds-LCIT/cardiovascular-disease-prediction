from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
import xgboost as xgb
import matplotlib.pyplot as plt
import lightgbm as lgbm


def plot_roc(fpr, tpr):
    # Plot ROC curve
    plt.plot(fpr, tpr, color='blue', label='ROC Curve')
    plt.plot([0, 1], [0, 1], color='red',
             linestyle='--', label='Random Guessing')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()


def metrics(y_test, predictions, proba):
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f_score = f1_score(y_test, predictions)
    roc_auc = roc_auc_score(y_test, proba)

    return accuracy, precision, recall, f_score, roc_auc


class TrainModel():

    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

   
    def logistic_regression_model(self):
        # Train the classifier
        logreg = LogisticRegression(random_state=0)
        logreg.fit(self.X_train, self.y_train)

        # make prediction
        prediction = logreg.predict(self.X_test)
        predict_proba = logreg.predict_proba(self.X_test)

        result = metrics(self.y_test, prediction, predict_proba[:, 1])

        return result
    
    def xg_boost(self):
        # Define parameters for XGBoost
        params = {
            'booster': 'gbtree',  # gblinear
            'learning_rate': 0.15,
            'n_estimators': 200,
            'subsample': 0.8,
            'max_depth': 2,  # Tree Depth
            'objective': 'binary:logistic',  # Binary classification
            'eval_metric': 'merror'  # Evaluation metric
        }

        # XGB CLF
        xgb_clf = xgb.XGBClassifier(**params)
        xgb_clf.fit(self.X_train, self.y_train)

        # Make predictions
        predictions_clf = xgb_clf.predict(self.X_test)
        binary_predictions_clf = (predictions_clf > 0.5).astype(int)
        predict_proba = xgb_clf.predict_proba(self.X_test)

        # Calculate metrics
        result = metrics(self.y_test, binary_predictions_clf, predict_proba[:, 1])
        
        return result
    
    def gbm_model(self):
        # Initialize the Gradient Boosting Classifier
        gradient_boosting = GradientBoostingClassifier(
            n_estimators=150, learning_rate=0.14, max_depth=2)

        # Train the model
        gradient_boosting.fit(self.X_train, self.y_train)

        prediction = gradient_boosting.predict(self.X_test)
        predict_proba = gradient_boosting.predict_proba(self.X_test)

        # Calculate metrics
        result = metrics(self.y_test, prediction, predict_proba[:, 1])

        return result
    
# Unused Models

    def knn_model(self):
        # Train the classifier
        knn_classifier = KNeighborsClassifier(n_neighbors=10)
        knn_classifier.fit(self.X_train, self.y_train)

        # make prediction
        prediction = knn_classifier.predict(self.X_test)
        predict_proba = knn_classifier.predict_proba(self.X_test)
        result = metrics(self.y_test, prediction, predict_proba[:, 1])

        return result

    def random_forest_model(self):
        # Train the classifier
        rf = RandomForestClassifier(n_estimators=100, random_state=95)
        rf.fit(self.X_train, self.y_train)

        # Make predictions
        predictions = rf.predict(self.X_test)
        predict_proba = rf.predict_proba(self.X_test)

        result = metrics(self.y_test, predictions, predict_proba[:, 1])

        return result

    def svm_model(self):
         # Train the classifier
         svm_clf = svm.SVC(kernel='linear', C=1.0, probability=True)
         svm_clf.fit(self.X_train, self.y_train)

         # Make predictions
         predictions = svm_clf.predict(self.X_test)
         predict_proba = svm_clf.predict_proba(self.X_test)

         result = metrics(self.y_test, predictions, predict_proba[:, 1])

         return result

    def light_gbm(self):

        parameters = {
            "objective": "binary",  # binary_logloss/multiclass
            # droptrees#gbdt(decision trees)/goss(one side sampling(DO NOT Understand))
            "boosting_type": "dart",
            "is_unbalance": True,
            "max_depth": 3,
            "learning_rate": 0.1,
            "subsample": 0.8,  # sub samples or bagging to reduce overfitting for each model
            "metric": 'binary_error',
            "num_leaves": 7,  # NEEDS RESEARCH
            # "early_stopping_rounds":10 :NEEDS RESEARCH
            "force_row_wise": True  # NEEDS RESEARCH
        }
        # Initialising Light GBM
        lgb_clf = lgbm.LGBMRegressor(**parameters)
        lgb_clf.fit(self.X_train, self.y_train)

        # Predicting
        predictions = lgb_clf.predict(self.X_test, num_iteration=lgb_clf.best_iteration_)
        binary_predictions = (predictions > 0.5).astype(int)
        # predict_proba = lgb_clf.predict_proba(self.X_test)

        # Evaluating Model
        results = metrics(self.y_test, binary_predictions, predictions)

        return results
