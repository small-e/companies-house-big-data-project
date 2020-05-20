class BinaryClassifierMetrics:
    '''
    '''

    def __init__(self):
        self.__init__

    @staticmethod
    def binary_confusion_matrix(pred: int, files: str):
        '''
        Calculates the number of true positives, true negatives, false positives and
        false negatives from the output of the classifier, where the true values are
        extracted from the corresponding file names

        Arguments:
            pred:  output from classifier
            files: list of file names

        Raises:
            None

        Returns:
            tuple 
        '''

        exp = [1 if i.rfind('positive') else 0 for i in files]
        tp = sum(1 for i, j in zip(pred, exp) if i + j is 2)
        tn = sum(1 for i, j in zip(pred, exp) if i + j is 0)
        fp = sum(1 for i, j in zip(pred, exp) if i is 1 and j is 0)
        fn = sum(1 for i, j in zip(pred, exp) if i is 0 and j is 1)

        return tp, tn, fp, fn

    @staticmethod
    def accuracy(tp: int, tn: int, fp: int, fn: int):
        '''
        Calculate the accuracy as a ratio of the number of correct predictions 
        to the total number of predictions.
        
        Arguments:
            tp: number of true positives
            tn: number of true negatives
            fp: number of false positives
            fn: number of false negatives
        
        Raises:
            Exception if a None value is specified as an argument.
            Exception if the type of a value specified as an argument is not an int.
        
        Returns:
            float

        accuracy = ( tp + tn ) / (tp + tn + fp + fn)
        '''

        if tp is None or tn is None or fp is None or fn is None:
            raise ValueError("Specify integer values")
        if type(tp) not in [int] or type(tn) not in [int] or type(fp) not in [int] or type(fn) not in [int]:
            raise TypeError("Specify integer types")
        if (tp + tn + fp + fn) is not 0:
            return (tp + tn) / (tp + tn + fp + fn)

    @staticmethod
    def precision(tp: int, fp: int):
        '''
        Calculate the precision as a ratio of the number of true positives 
        to the total number of reported positives.
        
        Arguments:
            tp: number of true positives
            fp: number of false positives  
        
        Raises:
            Exception if a None value is specified as an argument.
            Exception if the type of a value specified as an argument is not an int.
        
        Returns:
            float
        
        precision = tp / (tp + fp)
        '''

        if tp is None or fp is None:
            raise ValueError("Specify integer values")
        if type(tp) not in [int] or type(fp) not in [int]:
            raise TypeError("Specify integer types")
        if (tp + fp) is not 0:
            return tp / (tp + fp)

    @staticmethod
    def recall(tp: int, fn: int):
        '''
        Calculate the recall as a ratio of the number of true positives 
        to the total number of real positives. 
        
        Arguments:
            tp: number of true positives
            fn: number of false negatives  
        
        Raises:
            None
        
        Returns:
            float
        
        recall = tp / (tp + fn)
        '''
        if (tp + fn) is not 0:
            return tp / (tp + fn)

    @staticmethod
    def specificity(tn: int, fn: int):
        '''
        Calculate the specificity as a ratio of the number of true negatives 
        to the total number of reported negatives.
        
        Arguments:
            tn: number of true negatives
            fn: number of false negatives  
        
        Raises:
            Exception if a None value is specified as an argument.
            Exception if the type of a value specified as an argument is not an int.
        
        Returns:
            float
        
        specificity = tn / (tn + fn)
        '''


        if tn is None or fn is None:
            raise ValueError("Specify integer values")
        if type(tn) not in [int] or type(fn) not in [int]:
            raise TypeError("Specify integer types")
        if (tn + fn) is not 0:
            return tn / (tn + fn)

    @staticmethod
    def metrics_reports(accuracy: float, precision: float, recall: float, specificity: float):
        '''
        Outputs the performance metrics values of a binary classifier to the terminal. 
        The performance metrics are accuracy, precision, recall and specificity. 
        Values for each metric are between 0.0 and 1.0.
        
        Arguments:
            accuracy:       instance of the accuracy object.
            precision:      instance of the precision object.
            recall:         instance of the recall object.
            specificity:    instance of the specificity object.
        
        Raises:
            None
        
        Returns:
            String
        '''
        output = "\nThe performance metrics of the binary classifier presented with image ??? "\
                 "are as follows:\naccuracy = {}\nprecision = {}\nrecall = {}\nspecificity = {}"\
                 .format(accuracy, precision, recall, specificity)
        print(output)