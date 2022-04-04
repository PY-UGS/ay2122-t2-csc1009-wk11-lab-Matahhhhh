class Calculator:
    #initialize value to 0
    def __init__(self):
        self.value = 0

    # add two values and return the result
    def adder(self, input1, input2):
        self.value = input1 + input2
        return self.value

    # subtract two values and return the result
    def subtractor(self, input1, input2):
        self.value = input1 - input2
        return self.value

    # mutliply two values and return the result
    def multiplier(self, input1, input2):
        self.value = input1 * input2
        return self.value

    # divide two values and return the result
    def divider(self, input1, input2):
        self.value = input1 / input2
        return self.value

    # reset calculator value to 0
    def clear(self):
        self.value = 0

# create a result object
result = Calculator()

# take in the 2 values from user
input1 = float(input("Enter float input 1:"))
input2 = float(input("Enter float input 2 :"))

# perform all the operations and print their values
print("Addition of input1 and input2: ", result.adder(input1, input2))
print("Subtraction of input1 and input2: ",result.subtractor(input1, input2))
print("Multiplication of input1 and input2: ", result.multiplier(input1, input2))
print ("Division of input1 and input2: ",result.divider(input1, input2))

result.clear()