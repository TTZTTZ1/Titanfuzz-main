import torch

# Prepare input data
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
other_tensor = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float32)

# Call the API
result_tensor = input_tensor.add_(other_tensor)

print(result_tensor)