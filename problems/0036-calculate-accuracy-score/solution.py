import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	dogru_sayisi = np.sum(y_true==y_pred)
	toplam_sayisi = len(y_true)
	return float(dogru_sayisi/toplam_sayisi)
	pass