import torch
input_data = torch.tensor([(- 0.5), 0.0, 0.5], dtype=torch.float32)
result = input_data.asin_()
print(result)