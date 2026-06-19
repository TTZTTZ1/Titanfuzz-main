import torch
from torchvision import transforms
from PIL import Image

# Load an image
image = Image.open('path_to_image.jpg')

# Convert image to tensor
tensor_image = transforms.ToTensor()(image)

# Define the desired output size
output_size = (256, 256)

# Interpolate the tensor image
interpolated_tensor = torch.nn.functional.interpolate(tensor_image.unsqueeze(0), size=output_size, mode='bilinear', align_corners=False)

# Convert back to PIL image
interpolated_image = transforms.ToPILImage()(interpolated_tensor.squeeze(0))

# Save the interpolated image
interpolated_image.save('interpolated_image.jpg')