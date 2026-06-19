import torch

# Generate valid input data
input_tensor = torch.tensor([-0.5, 0.0, 0.5], dtype=torch.float32)

# Call the API
result = input_tensor.arcsin_()
print(result)