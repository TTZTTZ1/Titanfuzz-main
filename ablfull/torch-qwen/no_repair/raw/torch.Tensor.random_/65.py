import torch

input_data = -5
output = torch.Tensor().random_(from_=input_data, to=None)
print(output)