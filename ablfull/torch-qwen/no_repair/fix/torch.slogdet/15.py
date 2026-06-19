
import torch
input_data = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float)
result = torch.slogdet(input_data)
print(result)
