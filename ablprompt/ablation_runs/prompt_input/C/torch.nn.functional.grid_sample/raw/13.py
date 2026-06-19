import torch
from torchvision import transforms

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define an affine transformation matrix
theta = torch.tensor([[1.0, 0.0, 32], [0.0, 1.0, 32]], dtype=torch.float32).unsqueeze(0)
grid = transforms.ToPILImage()(transforms.functional.affine(input_tensor.squeeze().permute(1, 2, 0), theta=theta, scale=None, shear=None, translate=[32, 32], fillcolor=None)).convert('RGB')

# Convert the PIL image back to a tensor
grid = transforms.ToTensor()(grid).unsqueeze(0).permute(0, 3, 1, 2)

# Perform grid sampling
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)  # Should be (1, 3, 64, 64)