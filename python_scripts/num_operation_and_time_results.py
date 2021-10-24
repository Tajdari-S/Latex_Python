class Results:
    def __init__(self,number_of_flows,arrival_rate,number_of_operations,update_time):
        self.number_of_flows= number_of_flows
        self.arrval_rate = arrival_rate
        self.number_of_operation = number_of_operations
        self.update_time = update_time

    def __str__(self):
        return str(self.number_of_flows).__add__("\t")\
            .__add__(str(self.arrval_rate)).__add__("\t")\
            .__add__(str(self.update_time))\
            .__add__("\t").__add__(str(self.number_of_operation))

