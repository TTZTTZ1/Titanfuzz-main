import torch

# Generate input data satisfying all constraints
input_data = torch.Tensor.random_((3,), dtype=torch.float, from_=0, to=1)
print(input_data)