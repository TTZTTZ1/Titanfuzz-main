import torch

# Prepare input data
input_tensor = torch.tensor([1.0, -1.0], dtype=torch.float32)
other_tensor = torch.tensor([-1.0, 1.0], dtype=torch.float32)

# Call the API
result = torch.atan2(input_tensor, other_tensor)
print(result)