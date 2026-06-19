import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Call the API
raveled_tensor = input_tensor.ravel()
print(raveled_tensor)