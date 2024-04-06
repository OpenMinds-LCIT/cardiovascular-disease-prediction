import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance

class FeatureImportanceAnalysis:

    def __init__(self, model_files, X_test, y_test):
        self.model_files = model_files
        self.X_test = X_test
        self.y_test = y_test

    def load_models(self):
        models = {}
        for model_name, filename in self.model_files.items():
            filepath = self.get_dump_file(filename)
            model = joblib.load(filepath)

            # Check the type of loaded model
            if isinstance(model, dict):
                models[model_name] = model
            else:
                models[model_name] = {
                    "predict": model,
                    "feature_importance": model.feature_importances_ if hasattr(model, 'feature_importances_') else
                    model.coef_[0],
                    "feature_names": self.X_test.columns.tolist()
                }
        return models

    def get_dump_file(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
        path = os.path.join(project_dir, f'src/dump_model/{filename}')
        return path

    def plot_feature_importance(self):
        models = self.load_models()
        for model_name, model in models.items():
            feature_importance = model["feature_importance"]
            feature_names = model["feature_names"]

            # Plot feature importance
            plt.figure(figsize=(8, 6))
            plt.barh(feature_names, feature_importance)
            plt.xlabel('Feature Importance')
            plt.title(f'Feature Importance - {model_name}')
            plt.tight_layout()
            plt.savefig(f'{model_name}_feature_importance.png')
            plt.show()
            plt.close()

    def permutation_importance_analysis(self):
        models = self.load_models()
        for model_name, model in models.items():
            # permutation importance analysis
            result = permutation_importance(model["predict"], self.X_test, self.y_test, n_repeats=10, random_state=42)
            sorted_idx = result.importances_mean.argsort()

            # Plot permutation importance
            fig, ax = plt.subplots()
            ax.boxplot(result.importances[sorted_idx].T, vert=False,
                       labels=np.array(model["feature_names"])[sorted_idx])
            ax.set_title(f"Permutation Importances ({model_name} - test set)")
            plt.tight_layout()
            plt.savefig(f'{model_name}_permutation_importance.png')
            plt.show()
            plt.close()
