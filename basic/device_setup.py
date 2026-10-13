import torch
import torch.nn as nn

def Processing_Unit():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    return device


device = Processing_Unit()

print("Device:", device)

print(torch.__version__)

print(torch.cuda.device_count())
    