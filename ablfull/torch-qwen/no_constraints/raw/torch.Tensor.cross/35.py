import torch

# Generate two 3D vectors as input data
vector1 = torch.tensor([1.0, 2.0, 3.0])
vector2 = torch.tensor([4.0, 5.0, 6.0])

# Call the API
result = vector1.cross(vector2)

print(result)