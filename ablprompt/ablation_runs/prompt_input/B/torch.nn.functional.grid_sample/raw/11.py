import torch
from torchvision import transforms
from PIL import Image

# Load and preprocess an image
image = Image.open('path_to_image.jpg').convert('RGB')
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])
input_tensor = transform(image).unsqueeze(0)

# Create a grid for transformation
grid = torch.rand(1, 64, 64, 2) * 2 - 1  # Random grid in [-1, 1]

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)