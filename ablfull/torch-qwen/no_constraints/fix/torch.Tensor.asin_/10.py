import torch
input_data = torch.tensor([0.5, 0.7, (- 0.3)])
result = input_data.asin_()
print(result)