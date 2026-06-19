import torch

# Generate input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.float32)

# Call the API
result_tensor = input_tensor.double()

print(result_tensor)