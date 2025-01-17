# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f2s4IvgsbmA5DAS3oyemS7bE4y4biB96
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from tensorflow.keras.datasets import mnist
from sklearn.metrics import confusion_matrix  # Importa la función confusion_matrix para calcular la matriz de confusión
import seaborn as sns  # Importa seaborn para generar gráficos de la matriz de confusión

# Cargar el conjunto de datos MNIST (imágenes de dígitos de 0-9)
# El conjunto de datos se divide en dos partes: entrenamiento y prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento de los datos
# Aplanamos las imágenes 28x28 píxeles a un vector de 784 valores (28*28)
x_train_flat = x_train.reshape(x_train.shape[0], -1)  # Aplana los datos de entrenamiento
x_test_flat = x_test.reshape(x_test.shape[0], -1)     # Aplana los datos de prueba

# Dividir el conjunto de datos de entrenamiento en entrenamiento y validación
x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(
    x_train_flat, y_train, test_size=0.3, random_state=42
)

# Crear y entrenar un árbol de decisión con una profundidad máxima ajustada a 5
# 'max_depth' controla la profundidad máxima del árbol, es decir, cuántas divisiones puede hacer el árbol antes de detenerse.
#Un valor más alto puede conducir a sobreajuste, mientras que un valor demasiado bajo puede conducir a un modelo subajustado.
clf = DecisionTreeClassifier(max_depth=5)
clf = clf.fit(x_train_split, y_train_split)  # Entrenar el modelo con los datos de entrenamiento

# Predecir las etiquetas del conjunto de datos de prueba
y_pred = clf.predict(x_test_flat)

# Evaluar el rendimiento del modelo comparando las predicciones con las etiquetas verdaderas
# 'accuracy_score' mide la proporción de predicciones correctas.
accuracy = accuracy_score(y_test, y_pred)
print("Precisión en el conjunto de prueba:", accuracy)

# Visualizar el árbol de decisión
# Esta visualización muestra cómo el árbol toma decisiones dividiendo los datos en función de características.
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, fontsize=10)
plt.show()

# Visualizar una imagen del conjunto de datos de prueba junto con su etiqueta real y la predicción del modelo
# 'imshow' muestra la imagen del dígito, y se utiliza para comparar la predicción y la etiqueta real.
plt.imshow(x_test[0], cmap='gray')  # Muestra la primera imagen en el conjunto de prueba
plt.title(f"Etiqueta real: {y_test[0]}, Predicción: {y_pred[0]}")  # Comparación visual
plt.show()

# Identificar los errores cometidos por el modelo
# 'np.where' devuelve los índices donde las predicciones no coinciden con las etiquetas verdaderas.
errors = np.where(y_pred != y_test)[0]

# Visualizar algunos de los errores
# Este bloque crea una cuadrícula de 3x3 donde se muestran las primeras 9 imágenes que el modelo predijo incorrectamente.
#Esto ayuda a entender qué tipos de dígitos son más difíciles para el modelo.
plt.figure(figsize=(10, 10))
for i, error in enumerate(errors[:9]):  # Iterar sobre los primeros 9 errores
    plt.subplot(3, 3, i+1)  # Crear una cuadrícula de 3x3
    plt.imshow(x_test[error], cmap='gray')  # Mostrar la imagen del dígito erróneo
    plt.title(f"Pred: {y_pred[error]}, True: {y_test[error]}")  # Mostrar predicción y valor real
plt.show()

# Imprimir el informe de clasificación que incluye métricas como precisión, recall y f1-score
# Estas métricas proporcionan más información sobre el rendimiento del modelo para cada clase (dígito).
print(classification_report(y_test, y_pred))

# Imprimir la precisión final del modelo en poercentaje
print(f'Exactitud del modelo: {accuracy*100:.2f}%')

# Predecir los valores para el conjunto de prueba
y_pred = clf.predict(x_test_flat)  # Genera las predicciones usando el modelo entrenado con los datos de prueba

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)  # Compara las etiquetas reales con las predichas y calcula la matriz de confusión

# Visualizar la matriz de confusión usando seaborn
plt.figure(figsize=(10, 7))  # Configura el tamaño de la figura para el gráfico de la matriz de confusión
sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')  # Genera un mapa de calor de la matriz de confusión, con anotaciones de los valores
plt.title('Matriz de Confusión')  # Añade un título al gráfico
plt.xlabel('Etiqueta Predicha')  # Etiqueta para el eje X que indica las clases predichas por el modelo
plt.ylabel('Etiqueta Verdadera')  # Etiqueta para el eje Y que indica las clases reales o verdaderas
plt.show()  # Muestra el gráfico en la pantalla