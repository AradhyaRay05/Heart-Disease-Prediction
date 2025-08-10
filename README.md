# HeartGuardAI - AI Powered Heart Disease Predictor

---

## 📌 Project Goal  
HeartGuardAI is designed to assist in the early detection of heart disease by leveraging machine learning models.  
The goal is to provide a simple, accurate, and accessible tool for predicting the likelihood of heart disease based on patient data.  
The project aims to support preventive healthcare and reduce diagnostic delays.

---

## 📖 Overview  
HeartGuardAI uses a trained deep learning model to predict whether a patient is likely to have heart disease.  
It processes key health parameters such as age, cholesterol levels, and blood pressure, then delivers predictions through an easy-to-use **Streamlit web interface**.  
This project demonstrates the complete ML pipeline from **data preprocessing** to **deployment**.

---

## 🔄 Project Workflow  

### 1️⃣ Data Preprocessing  
- Loaded heart disease dataset from **UCI Machine Learning Repository**.  
- Checked for missing/null values and handled inconsistencies.  
- Encoded categorical variables into numerical format.  
- Normalized and scaled features using **StandardScaler** from `scikit-learn`.  
- Split dataset into **80% training** and **20% testing** sets for model evaluation.  

### 2️⃣ Model Building  
Tested multiple classification models:  
- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine (SVM)  
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Gradient Boosting Classifier
- **Deep Neural Network (✅ Best Performer)**  

**Final Model:**  
- Architecture: 3 Dense layers with ReLU activation and Dropout layers to prevent overfitting  
- Output Layer: Sigmoid activation for binary classification  
- Optimizer: Adam  
- Loss: Binary Crossentropy  
- Saved using `.keras` format for deployment and `joblib` for the scaler.  

### 3️⃣ Evaluation Metrics  
- **Accuracy:** 0.86 on the test set  
- **Precision:** 0.84  
- **Recall:** 0.87  
- **F1-Score:** 0.85  
- Confusion matrix visualized for better understanding of model performance.  

### 4️⃣ Deployment  
- Built an interactive **Streamlit** web app for local deployment.  
- User inputs health data through sliders and dropdowns.  
- Data is scaled using the saved `StandardScaler` before prediction.  
- Model predicts and displays results instantly with a clear **"Heart Disease Detected"** or **"No Heart Disease Detected"** message.  
- Ready to be deployed on platforms like **Streamlit Cloud** or **Heroku** for global access.  

---

## ✨ Features  
- Predicts likelihood of heart disease using health parameters  
- Simple and interactive web interface  
- Fast, lightweight, and easy to deploy locally  

---

## 🚀 Future Enhancements  
- Deploy on **cloud platforms** like Heroku or Streamlit Cloud  
- Add visualization of prediction probabilities  
- Expand dataset for improved generalization  
- Implement explainable AI techniques for better interpretability
  
---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
