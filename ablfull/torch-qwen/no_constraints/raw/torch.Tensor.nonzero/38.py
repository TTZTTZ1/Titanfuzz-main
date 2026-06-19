import torch

# Generate input data
input_tensor = torch.tensor([[0, 1, 2], [3, 0, 5]], dtype=torch.float32)

# Call the API
result = input_tensor.nonzero()

print(result)