import torch

# Example usage of torch.sign
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)
signed_tensor = torch.sign(input_tensor)

print("Input Tensor:", input_tensor)
print("Signed Tensor:", signed_tensor)