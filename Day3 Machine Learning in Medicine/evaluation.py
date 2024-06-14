#-----------------------------------------------------#
#                  Evaluation methods                 #
#-----------------------------------------------------#
def confusion_matrix(pred, truth):
    truth = truth.values.tolist()
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(0,len(pred)):
        if pred[i] == 0 and truth[i] == 0:
            tn += 1
        elif pred[i] == 1 and truth[i] == 0:
            fp += 1
        elif pred[i] == 0 and truth[i] == 1:
            fn += 1
        else: #pred[i] == 1 and truth[i] == 1
            tp += 1
    return [tp,tn,fp,fn]
def compute_scores(m):
    accuracy = (m[0] + m[1])/(m[0] + m[1] + m[2] + m[3])
    precision = m[0]/(m[0] + m[2])
    sensitivity = m[0]/(m[0] + m[3])
    specificity = m[1]/(m[1] + m[2])
    f1 = (2 * precision * sensitivity)/(precision + sensitivity)
    return accuracy, f1, precision, sensitivity, specificity
