import torch

# Example usage of torch.exp
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)
output_tensor = torch.exp(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)