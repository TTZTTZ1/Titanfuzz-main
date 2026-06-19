import torch
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0], dtype=torch.float32)
std_mean_result = torch.std_mean(input_data)