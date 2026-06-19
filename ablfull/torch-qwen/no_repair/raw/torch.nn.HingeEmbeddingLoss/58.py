import torch

# Define parameters
margin = 1.0
size_average = True
reduce = True
reduction = 'mean'

# Create sample input data
input1 = torch.randn(3)
input2 = torch.randn(3)

# Initialize loss function
criterion = torch.nn.HingeEmbeddingLoss(margin=margin, size_average=size_average, reduce=reduce, reduction=reduction)

# Call the API
loss = criterion(input1, input2)