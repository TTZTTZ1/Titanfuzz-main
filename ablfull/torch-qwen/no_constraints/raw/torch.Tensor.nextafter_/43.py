import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
eps = torch.tensor(1e-7, dtype=torch.float32)

# Call the API
result = input_tensor.nextafter(eps)

print(result)