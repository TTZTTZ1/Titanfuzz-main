import torch
input_data = torch.zeros(3, 4)
input_data.random_(0, 10)
result = input_data.random_(0, 10)
print(result)