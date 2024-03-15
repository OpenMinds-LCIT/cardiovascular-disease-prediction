from feature_extraction import extract_feature
from split_dataset import split_data
from fill_data import fill_data
from scale import scale_minmax
from svm_model_tirth import svm_model_training

X_train, X_test, y_train, y_test = split_data()

# Data Filling
filled_x_train = fill_data(data_frame=X_train)
filled_x_test = fill_data(data_frame=X_test)

# Data Scaling
scaled_train_data = scale_minmax(filled_x_train)
scaled_test_data = scale_minmax(filled_x_test)

# Features
X_train = extract_feature(data_frame=scaled_train_data, y_train=y_train)
X_test = extract_feature(data_frame=scaled_test_data, y_train=y_test)

#model_accuracy and precision
model_accuracy = svm_model_training(X_train, X_test, y_train, y_test)
model_precision = svm_model_training(X_train, X_test, y_train, y_test)

print(model_accuracy)
print(model_precision)