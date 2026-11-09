import numpy as np
def precision(y_true, y_pred):
	# Your code here
	#
	tp = np.sum((y_pred==1)&(y_true==1))
	tp_plus = np.sum(y_pred==1)
	if tp_plus == 0:
		return 0.0
	return tp / tp_plus
	pass
