#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# Import external libraries
import argparse

# Import student libraries
from data_processing import read_dataset, exploration, preprocessing, split_dataset
from algorithms import Logistic_Regression, Naive_Bayes, Support_Vector_Machine, K_Nearest_Neighbor, \
    Random_Forest_Classifier
from evaluation import confusion_matrix, compute_scores

#-----------------------------------------------------#
#                      Argparser                      #
#-----------------------------------------------------#
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Autism Spectrum Disorder (ASD) classification")
# Add arguments to the Argument Parser
parser.add_argument("-i", "--input", action="store", dest="input",
                    type=str, required=True,
                    help="Path to the Autism_Screening.Data.csv file.")
parser.add_argument("-a", "--algorithm", action="store", dest="algorithm",
                    type=str, default="lr",
                    help="Option which classification algorithm is used.\
                    Possible algorithm: [explore, lr, nb, knn, svm, rf, compare]")
# Parse arguments
args = parser.parse_args()
data_set = read_dataset(args.input)
#-----------------------------------------------------#
#                 Data Set Exploration                #
#-----------------------------------------------------#
if args.algorithm == "explore":
    # Run Data Set Exploration
    exploration(data_set)

#-----------------------------------------------------#
#               Classification Pipeline               #
#-----------------------------------------------------#
elif args.algorithm in ["lr", "nb", "knn", "svm", "rf"]:

    # Preprocess data set
    cat_var_list = ['Age_Range','Ethnicity','Residence','Entry_Person'] # TASK: fill in all categorical variables
    bol_var_list = ['ASD','Gender','Test_Jundice','Test_Family_PDD','Used_App_Before'] # TASK: fill in all boolean variables
    num_var_list = ['Age','Screening_A6','Screening_A7','Screening_A8','Screening_A9','Screening_A10'] # TASK: fill in all numerical variables
    data_set_preprocessed = preprocessing(data_set,
                                          categorical_variables=cat_var_list,
                                          binary_variables=bol_var_list,
                                          numeric_variables=num_var_list)

    # Split data set into train and test data sets
    train_x, test_x, train_y, test_y = split_dataset(data_set_preprocessed,
                                                     y_var="ASD",
                                                     test_size=0.2)

    # Initialize algorithm
    model = None
    if args.algorithm == "lr":
        model = Logistic_Regression()
    # TASK: Extend later with other algorithm
    elif args.algorithm == "nb":
        model = Naive_Bayes()
    elif args.algorithm == "knn":
        model = K_Nearest_Neighbor()
    elif args.algorithm == "svm":
        model = Support_Vector_Machine()
    else: #args.algorithm == "rf"
        model = Random_Forest_Classifier()
    # Train model
    model.train(train_x, train_y)

    # Predict the testing data with the
    pred = model.predict(test_x)

    # Evaluate results
    confusion_mat = confusion_matrix(pred, test_y)
    scores = compute_scores(confusion_mat)
    accuracy, f1, precision, sensitivity, specificity = scores

    # Output results
    print("Algorithm: " + args.algorithm)
    print("Accuracy: " + str(accuracy))
    print("F1: " + str(f1))
    print("Precision: " + str(precision))
    print("Sensitivity: " + str(sensitivity))
    print("Specificity: " + str(specificity))

#-----------------------------------------------------#
#                 Comparison Pipeline                 #
#-----------------------------------------------------#
elif args.algorithm == "compare":
    cat_var_list = ['Age_Range', 'Ethnicity', 'Residence', 'Entry_Person']  # TASK: fill in all categorical variables
    bol_var_list = ['ASD', 'Gender', 'Test_Jundice', 'Test_Family_PDD',
                    'Used_App_Before']  # TASK: fill in all boolean variables
    num_var_list = ['Age', 'Screening_A6', 'Screening_A7', 'Screening_A8', 'Screening_A9',
                    'Screening_A10']  # TASK: fill in all numerical variables
    data_set_preprocessed = preprocessing(data_set,
                                          categorical_variables=cat_var_list,
                                          binary_variables=bol_var_list,
                                          numeric_variables=num_var_list)

    # Split data set into train and test data sets
    train_x, test_x, train_y, test_y = split_dataset(data_set_preprocessed,
                                                     y_var="ASD",
                                                     test_size=0.2)

    models = [Logistic_Regression(),Naive_Bayes(),K_Nearest_Neighbor(),Support_Vector_Machine(),Random_Forest_Classifier()]
    names = ['lr: ','nb: ','knn: ','svm: ','rf: ']
    for model in models:
        model.train(train_x, train_y)
        pred = model.predict(test_x)
        confusion_mat = confusion_matrix(pred, test_y)
        scores = compute_scores(confusion_mat)
        accuracy, f1, precision, sensitivity, specificity = scores
        print(names[models.index(model)] + str(accuracy))
