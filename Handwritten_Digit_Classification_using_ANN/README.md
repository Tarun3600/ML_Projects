### MNIST Neural Network Classifier

#### **Overview**
This project uses a neural network to classify handwritten digits (0–9) from the MNIST dataset. The model is built with TensorFlow/Keras and trained to predict the digit in grayscale images.

---

#### **What It Does**
1. **Data Prep**: MNIST images are normalized (scaled to 0–1).
2. **Model**: 
   - **Flatten Layer**: Converts 28x28 images to a flat array.
   - **Dense Layers**: Uses ReLU and softmax activations for learning and classification.
3. **Training**:
   - First trained for 10 epochs.
   - Extended to 25 epochs to study overfitting.
4. **Evaluation**:
   - Accuracy is checked on test data.
   - Visualizes predictions and training progress.

---

#### **Key Insights**
- Adding more epochs improved training accuracy but led to **overfitting** on validation data.
- Final test accuracy is evaluated with Scikit-learn’s `accuracy_score`.

---

#### **How to Run**
1. Install dependencies:
   ```bash
   pip install tensorflow matplotlib scikit-learn
   ```
2. Run the code to train the model and visualize results.

---

#### **Next Steps**
- Add dropout to reduce overfitting.
- Test deeper networks or different optimizers.

---
