# Import pytorch 

import torch 
import torch.nn as nn

from basic.device_setup import Processing_Unit

tensors = torch.tensor([1, 2, 3, 4, 5, 6, 7])

print("Tensor: ",tensors.device)

print("Tensor: ",tensors.to(Processing_Unit()))