import torch
input_data = torch.tensor([1.0, (- 1.0), float('inf'), float('-inf'), float('nan')], dtype=torch.float32)
result = torch.isfinite(input_data)
print(result)