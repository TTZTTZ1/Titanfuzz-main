import torch
start_tensor = torch.tensor([0.0, 1.0], dtype=torch.float32)
end_tensor = torch.tensor([2.0, 3.0], dtype=torch.float32)
weight = 0.5
result_tensor = start_tensor.clone()
result_tensor.lerp_(end_tensor, weight)
print(result_tensor)