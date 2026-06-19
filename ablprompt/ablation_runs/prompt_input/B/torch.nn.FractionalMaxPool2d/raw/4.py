import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Define the FractionalMaxPool2d layer
fractional_max_pool = F.fractional_max_pool2d(
    input_tensor,
    kernel_size=3,
    output_size=(112, 112),
    return_indices=True
)

print(fractional_max_pool.shape)