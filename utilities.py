import numpy as np

def netting(out_, in_):
    if not np.isnan(out_) and np.isnan(in_):
        return out_-0
    if np.isnan(out_) and not np.isnan(in_):
        return 0-in_
    if np.isnan(out_) and np.isnan(in_):
        return 0
    return 0