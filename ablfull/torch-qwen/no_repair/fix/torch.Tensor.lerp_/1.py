
import torch
start_tensor = torch.tensor([1.0, 2.0, 3.0])
end_tensor = torch.tensor([4.0, 5.0, 6.0])
weight = 0.5
result_tensor = start_tensor.clone()
result_tensor.lerp_(end_tensor, weight)
print(result_tensor)
