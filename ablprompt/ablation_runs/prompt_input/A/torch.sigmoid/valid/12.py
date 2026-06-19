import torch

# Example usage of torch.sigmoid
input_tensor = torch.tensor([-1.0, 0.0, 1.0])
output_tensor = torch.sigmoid(input_tensor)
print(output_tensor)