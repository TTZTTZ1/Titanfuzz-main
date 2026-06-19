import torch
from torchvision import transforms
from PIL import Image

# Load and preprocess an image
image = Image.open('path_to_image.jpg').convert('RGB')
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
input_tensor = transform(image).unsqueeze(0)

# Create an affine transformation grid
theta = torch.tensor([[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]])  # Identity transformation
grid = transforms.functional.affine_grid(theta, size=input_tensor.size(), align_corners=True)

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=True)

print(output_tensor.shape)