🏠 House Price Prediction (Ames Dataset)

📌 Overview

This project focuses on predicting house prices using the Ames Housing dataset. It demonstrates a complete machine learning workflow, from data cleaning to model evaluation.

---

🚀 What I Did

- Cleaned dataset and handled missing values
- Performed Exploratory Data Analysis (EDA)
- Identified important features using correlation
- Handled skewed data using log transformation
- Created new features (Total SF, House Age)
- Encoded categorical variables
- Removed outliers and redundant features
- Built and compared models:
  - Linear Regression (baseline)
  - Random Forest
- Evaluated performance using MAE and RMSE

---

📊 Key Insights

- Overall Quality and Living Area are the strongest predictors of house price
- Garage and Basement features significantly impact price
- Log transformation improved prediction accuracy
- Linear Regression performed slightly better due to strong linear relationships in data

---

🧠 Models Performance

Model| RMSE
Linear Regression| ~0.125
Random Forest| ~0.129

---

🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

📁 Project Structure

- "data/" → dataset files
- "notebooks/" → Jupyter notebooks
- "README.md" → project documentation

---

📈 How to Run

pip install -r requirements.txt
jupyter notebook

---

🎯 Conclusion

This project demonstrates a strong understanding of data preprocessing, feature engineering, and model evaluation. Linear Regression performed well due to clear linear relationships in the dataset, while Random Forest did not significantly improve performance.

---
