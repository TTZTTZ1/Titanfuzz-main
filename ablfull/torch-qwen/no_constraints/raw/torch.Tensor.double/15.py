import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
result_tensor = input_tensor.double()

print(result_tensor)