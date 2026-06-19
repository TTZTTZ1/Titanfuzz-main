import torch
input_data = torch.tensor([[4.0, 0.0], [0.0, 3.0]], dtype=torch.float32)
result = torch.slogdet(input_data)
print(result)