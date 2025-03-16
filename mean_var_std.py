import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
        
    array = np.array(list).reshape(3, 3)
    mean_0 = array.mean(axis = 0).tolist()
    mean_1 = array.mean(axis = 1).tolist()
    flat_mean = array.mean().tolist()
    
    var_0 = array.var(axis = 0).tolist()
    var_1 = array.var(axis = 1).tolist()
    flat_var = array.var().tolist()
    
    std_0 = array.std(axis = 0).tolist()
    std_1 = array.std(axis = 1).tolist()
    flat_std = array.std().tolist()
    
    max_0 = array.max(axis = 0).tolist()
    max_1 = array.max(axis = 1).tolist()
    flat_max = array.max().tolist()
    
    min_0 = array.min(axis = 0).tolist()
    min_1 = array.min(axis = 1).tolist()
    flat_min = array.min().tolist()
    
    sum_0 = array.sum(axis = 0).tolist()
    sum_1 = array.sum(axis = 1).tolist()
    flat_sum = array.sum().tolist()
    
    calculations = {
        'mean': [mean_0, mean_1, flat_mean],
        'variance': [var_0, var_1, flat_var],
        'standard deviation': [std_0, std_1, flat_std],
        'max': [max_0, max_1, flat_max],
        'min': [min_0, min_1, flat_min],
        'sum': [sum_0, sum_1, flat_sum]        
    }
    
    return calculations
    
