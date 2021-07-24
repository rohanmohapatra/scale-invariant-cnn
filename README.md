# Scale invariant CNN

"Size doesn't matter for me" - That's what our neural network said

## Keras - Baseline CNN
### Requirements
Install them first on your laptop
```
scikit-images
tqdm
```
### Baseline CNN
Took Mnist Data,  resized it to 16x16, 24x24 and 28x28. Then I padded all of them to make it look like 32x32

![plot_28_padded32](https://user-images.githubusercontent.com/31756343/126871877-b6f19159-c232-46c1-8b41-1c94d856aca3.png)
![plot_24_padded32](https://user-images.githubusercontent.com/31756343/126871882-81370da5-83f5-453b-a7f6-82d690df735b.png)
![plot_16_padded_32](https://user-images.githubusercontent.com/31756343/126871885-dafe5f6d-13db-43a0-b4b7-334ee44d837d.png)


Training Loss and Accuracy:
```
loss: 0.0620 - acc: 98.23
```

Validation Accuracy:
```
acc:98.44444444444445
```

To Run it just do:
```
python3 BaselineCNN.py
```

Testing:
```
X_tester = np.pad(resize(X_test[1174],(6,6)),[13,13],mode='constant')

np.argmax(model.predict(X_tester.reshape(1,32,32,1)))

plt.subplot(121)
plt.imshow(X_tester, cmap='gray')
```
