import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0], requires_grad=True)
input2 = torch.tensor([-1.0, 1.0], requires_grad=True)
margin = 1.0
reduction = 'mean'

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(margin=margin, reduction=reduction)

# Call the API
output = criterion(input1, input2)
print(output)