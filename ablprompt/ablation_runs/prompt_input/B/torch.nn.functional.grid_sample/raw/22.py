import torch
from torchvision import transforms
from PIL import Image

# Load an image and convert it to a tensor
image = Image.open('path_to_image.jpg')
transform = transforms.ToTensor()
input_tensor = transform(image).unsqueeze(0)

# Create a grid for sampling
grid = torch.rand(input_tensor.size(0), input_tensor.size(2), input_tensor.size(3), 2) * 2 - 1

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)