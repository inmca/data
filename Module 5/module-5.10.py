
##################################################################
# 10) Neural Network on MNIST with Keras
##################################################################

def task10_mnist_nn(epochs=5, batch_size=128):
    import tensorflow as tf
    from tensorflow.keras import layers, models
    import matplotlib.pyplot as plt
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train = x_train.astype('float32')/255.0
    x_test = x_test.astype('float32')/255.0
    x_train = x_train.reshape((-1,28,28,1))
    x_test = x_test.reshape((-1,28,28,1))
    num_classes = 10
    y_train_cat = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test_cat = tf.keras.utils.to_categorical(y_test, num_classes)

    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D((2,2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train, y_train_cat, epochs=epochs, batch_size=batch_size, validation_split=0.1)

    # Plot accuracy and loss
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.plot(history.history['accuracy'], label='train_acc')
    plt.plot(history.history['val_accuracy'], label='val_acc')
    plt.legend(); plt.title('Accuracy')
    plt.subplot(1,2,2)
    plt.plot(history.history['loss'], label='train_loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.legend(); plt.title('Loss')
    plt.show()

    test_loss, test_acc = model.evaluate(x_test, y_test_cat, verbose=0)
    print('Test accuracy:', test_acc)

    # Predict and show one image
    import numpy as np
    idx = 0
    pred = model.predict(x_test[idx:idx+1])
    pred_label = np.argmax(pred)
    print('True label:', y_test[idx], 'Predicted:', pred_label)
    plt.imshow(x_test[idx].reshape(28,28), cmap='gray')
    plt.title(f'True: {y_test[idx]} Pred: {pred_label}')
    plt.axis('off')
    plt.show()
    return model

##################################################################
# If run as script, show usage
##################################################################
if __name__ == '__main__':
    print('This file contains functions task1_corr_feature_selection, task2_forward_selection,\n'
          'task3_backward_elimination, task4_knn_iris, task5_naive_bayes, task6_decision_tree_iris,\n'
          'task7_linear_regression, task8_correlation_analysis, task9_multi_linear_regression,\n'
          'task10_mnist_nn. Call them individually with appropriate dataset paths.')
