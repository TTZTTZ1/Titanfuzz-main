import torch

# Example usage of torch.sign
tensor = torch.tensor([-1.0, 0.0, 1.0])
signed_tensor = torch.sign(tensor)
print(signed_tensor)  # Output: tensor([-1.,  0.,  1.])