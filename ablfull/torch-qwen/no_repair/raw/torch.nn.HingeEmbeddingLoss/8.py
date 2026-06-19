import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0], requires_grad=True)
input2 = torch.tensor([-1.0, 1.0], requires_grad=True)
target = torch.tensor([1, -1])

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Call the API
output = criterion(input1, input2, target)

print(output)