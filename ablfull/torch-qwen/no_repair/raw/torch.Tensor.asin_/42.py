import torch

# Generate input data
input_tensor = torch.tensor([0.5, -0.5], dtype=torch.float32)

# Call the API
result = input_tensor.asin_()
print(result)