import torch
from torchvision import transforms
from PIL import Image

# Load an image and transform it to a tensor
image = Image.open('path_to_image.jpg')
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((256, 256))
])
input_tensor = transform(image).unsqueeze(0)

# Create a grid for sampling
grid = torch.rand(input_tensor.size(0), 256, 256, 2) * 2 - 1

# Apply grid sampling
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)