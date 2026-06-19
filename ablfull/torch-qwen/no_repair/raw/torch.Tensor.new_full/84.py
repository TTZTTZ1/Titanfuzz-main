import torch

# Prepare valid input data
size = (3, 4)
fill_value = 5.0
dtype = torch.float32

# Call the API
tensor = torch.Tensor.new_full(size, fill_value, dtype=dtype)

print(tensor)