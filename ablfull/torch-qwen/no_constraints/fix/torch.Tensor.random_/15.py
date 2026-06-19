import torch
input_data = (5,)
result = torch.Tensor().random_(*input_data)
print(result)