import torch
from torchvision import transforms
from PIL import Image

# Load and preprocess an image
image = Image.open('path_to_image.jpg')
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])
input_tensor = transform(image).unsqueeze(0)

# Create a grid for transformation
grid = torch.rand(input_tensor.size()[0], 128, 128, 2) * 2 - 1

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)