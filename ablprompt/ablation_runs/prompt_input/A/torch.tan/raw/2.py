import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the torch.tan function
tan_output = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Tangent Output:", tan_output)