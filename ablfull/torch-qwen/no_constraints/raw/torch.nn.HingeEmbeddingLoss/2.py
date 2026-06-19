import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0, 0.5])
input2 = torch.tensor([-1.0, 1.0, -0.5])
target = torch.tensor([1, -1, 1])

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Call the API
loss = criterion(input1, input2, target)

print(loss)