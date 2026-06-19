import torch
input_data = torch.tensor([(- torch.pi), ((- 0.5) * torch.pi), 0.0, (0.5 * torch.pi), torch.pi], dtype=torch.float32)
result = torch.sin(input_data)
print(result)