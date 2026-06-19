import torch
input_data = torch.tensor([(- float('inf'))], dtype=torch.float32)
result = torch.isneginf(input_data)
print(result)