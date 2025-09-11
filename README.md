# Org Go - Data & Preprocessing

This repository contains the raw agricultural datasets and Jupyter notebooks for data cleaning, feature engineering, preprocessing, and train-test split generation for the Org Go AI project focused on sustainable organic agriculture.

## 📂 Repository Structure

- `data/raw/` - Raw agricultural datasets (CSV files and images)
- `data/processed/` - Cleaned and processed datasets ready for ML
- `notebooks/01_data_preprocessing.ipynb` - Data preprocessing pipeline
- `requirements.txt` - Python dependencies required
- `.gitignore` - Excludes large data files and sensitive info

## 🚀 Getting Started

1. Place downloaded raw dataset files in `data/raw/` as per project structure.
2. Install required packages:
3. Start Jupyter Notebook and run preprocessing:

## 🧹 Preprocessing Steps

- Remove duplicates and handle missing values intelligently
- Feature engineering: soil nutrient ratios, climate indices, rainfall and soil type categories
- Label encoding for categorical features
- Scaling features with StandardScaler
- Train-test split creation for model training

## 📦 Outputs

- Cleaned datasets saved under `data/processed/`
- Scaled train and test datasets
- Feature encoding artifacts for reproducibility

## 🔗 Next Steps

Use the processed datasets from this repo to train models in the [Org Go Models repository](https://github.com/yourusername/Org-GO-Models).

## 📄 License

This project is licensed under the MIT License.
