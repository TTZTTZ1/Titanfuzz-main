import torch

# Prepare input data
input_tensor = torch.tensor([[1.0, 2.0, 3.0]])
indices_tensor = torch.tensor([[0, 1, 2]])

# Call the API
output = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size=2)

print(output)