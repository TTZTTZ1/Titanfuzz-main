import torch
input_data = torch.zeros(3, 4)
input_data.random_(0, 10)
output_tensor = input_data.random_(0, 10)