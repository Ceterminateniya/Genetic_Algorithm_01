def input_FitV():
    fit=input("Please enter the score (from 0 to 10):")
    while(type(fit)!=float):
        try:
            fit = float(fit)
            if (fit<0) or (fit>10):
                fit = input("Invalid range. Please enter the score again (from 0 to 10):")
        except:
            fit = input("Invalid type. Please enter the score again (from 0 to 10):")
    return fit

input_FitV()