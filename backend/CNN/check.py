import numpy as np
import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os



data = np.genfromtxt('final_dataset.csv', delimiter=',', skip_header=1)


X = data[:, :-1]
y = data[:, -1]


scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(12, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')


def predict_weather_condition(temperature, wind_speed, pressure):
    input_data = np.array([[temperature, wind_speed, pressure]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)
    return predicted_class

temperature_to_predict = float(input("Enter the temperature: "))
wind_speed_to_predict = float(input("Enter the wind speed: "))
pressure_to_predict = float(input("Enter humidity: "))
predicted_class = predict_weather_condition(temperature_to_predict, wind_speed_to_predict, pressure_to_predict)
weather_classes = {
    0: "Fire hazard",
    1: "Hurricane",
    2: "Heat",
    4: "Snowstorm",
    5: "Normal conditions",
    6: "Downpour",
    7: "Tornado",
    8: "Frost",
    9: "Fog",
    10: "Icy Conditions",
    11: "Freezing rain"
}

print("Predicted Weather Condition:", weather_classes[predicted_class])



file_path = f'decription/{(weather_classes[predicted_class]).replace(" ","_")}.txt'
if os.path.isfile(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
else:
        if weather_classes[predicted_class].replace(" ","_") == 'Normal_conditions':
                print("Great weather")
        else:
                print("Description file not found for the predicted weather condition.")