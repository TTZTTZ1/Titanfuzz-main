import torch
input_tensor = torch.tensor([1.0, (- 2.0), 3.0], dtype=torch.float32)
negative_tensor = torch.Tensor.negative(input_tensor)
print(negative_tensor)