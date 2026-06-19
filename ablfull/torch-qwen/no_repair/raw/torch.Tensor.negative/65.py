import torch

# Generate input data
input_tensor = torch.tensor([1.0, -2.0, 3.0])

# Call the API
negative_tensor = input_tensor.negative()
print(negative_tensor)