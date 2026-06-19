import torch
input_data = torch.tensor([0.5, (- 0.5)], dtype=torch.float32)
output_data = input_data.asin_()
print(output_data)