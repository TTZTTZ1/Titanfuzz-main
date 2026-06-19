import torch
from torchvision import transforms
from PIL import Image

# Load an image and convert it to a tensor
image = Image.open('path_to_image.jpg')
transform = transforms.ToTensor()
input_tensor = transform(image).unsqueeze(0)

# Create a grid for sampling
grid = torch.rand((1, 256, 256, 2)) * 2 - 1  # Random grid within [-1, 1]

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)