from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard
label_map = {label:num for num, label in enumerate(actions)}

print(label_map)
seqs, labls = [], []

for action in actions:
    print("ACTION-->>",action,"sequence->")
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
          try:
            res = np.load(os.path.join(Dataset_Path, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
            seqs.append(window)
            labls.append(label_map[action])
          except Exception as e:
             print("ERROR=-->>>>",e)  

X = np.array(seqs)
y = to_categorical(labls).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(15,63)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
res = [.7, 0.2, 0.1]

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=200, callbacks=[tb_callback])
model.summary()

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save('model.h5')