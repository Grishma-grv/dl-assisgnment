1. AlexNet – Image Classification
The original AlexNet implementation only defined the architecture and assumed the ImageNet dataset, which is very large and impractical for academic execution.
The CIFAR-10 dataset was used instead, as it is a standard academic dataset containing RGB images across 10 classes.
This dataset change preserves the image classification objective while reducing computational and memory requirements.
The AlexNet architecture was simplified to match the smaller image size of CIFAR-10.
Batch Normalization was added to stabilize and speed up training.
Fully connected layers were reduced, and Dropout was added to reduce overfitting.
The optimized model trains efficiently and is suitable for student-level systems.

2. Cat vs Dog – Convolutional Neural Network
The original code used hard-coded file paths and older data loading techniques.
A folder-based Cats vs Dogs dataset was used, which is simple to organize and widely accepted for academic use.
Automatic image resizing, batching, and normalization were introduced.
The CNN architecture was simplified to reduce overfitting and training time.
Dropout was added to improve generalization.
The optimized version is portable, cleaner, and easier to execute while maintaining the same binary classification output.

3. Deep Reinforcement Learning – Q Learning
The original program used a fixed graph environment with repeated logic and global variables.
A simplified Q-learning implementation was created using a class-based structure.
Redundant functions were removed to improve readability.
The learning objective and reward mechanism remain unchanged.
The optimized version is easier to understand and can be extended for advanced reinforcement learning models.

4. LSTM – Time Series Prediction
The original airline passenger dataset was replaced with a daily temperature dataset.
The prediction objective remains the same, i.e., forecasting future values from historical data.
Data preprocessing was simplified for better readability.
Batch size was increased to improve training speed.
The optimized LSTM model trains faster and is more suitable for academic demonstrations of time-series forecasting.

5. RNN – Text Generation
The original implementation used a very small text sample with one-hot encoding.
A longer text dataset was used to improve sequence learning.
One-hot encoding was replaced with an embedding layer to reduce memory usage.
Model efficiency and generalization were improved.
The core objective of character-level text generation remains unchanged.

6. Tic Tac Toe – Reinforcement Learning
The original Tic Tac Toe program used a complex and lengthy reinforcement learning logic.
The exploration and action-selection strategy was simplified.
Code structure was optimized to improve clarity and readability.
The reinforcement learning objective remains the same.
The optimized version is easier to understand and suitable for academic reinforcement learning demonstrations.

Conclusion
In all programs, datasets were modified where necessary to make execution practical in an academic environment.
Code optimizations were applied to improve efficiency, readability, and training performance.
The core learning objectives of each program were preserved.
These modifications demonstrate practical understanding of deep learning and reinforcement learning concepts and are suitable for academic submission.
