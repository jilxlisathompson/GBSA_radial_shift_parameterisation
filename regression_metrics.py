def get_MAE(predicted, observed):
    mae = (predicted - observed).abs().mean()
    return mae

def get_RMSE(predicted, observed):
    rmse = ((predicted - observed)**2).mean() ** 0.5
    return rmse
def get_std():
    pass

def get_metrics():
    pass
