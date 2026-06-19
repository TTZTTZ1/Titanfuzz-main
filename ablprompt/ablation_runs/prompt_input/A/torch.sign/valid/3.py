import torch

# Create a tensor with some values
tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the torch.sign function
signed_tensor = torch.sign(tensor)

# Print the result
print(signed_tensor)