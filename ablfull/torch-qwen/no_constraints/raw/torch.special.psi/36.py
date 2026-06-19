import torch

# Generate input data: a tensor of shape (2,) with values between -5 and 5
x = torch.tensor([-4.0, 0.0], dtype=torch.float32)

# Call the API torch.special.psi
result = torch.special.psi(x)
print(result)