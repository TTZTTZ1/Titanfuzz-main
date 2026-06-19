import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Call torch.topk
top_values, top_indices = torch.topk(tensor, k=2)

print("Top values:", top_values)
print("Top indices:", top_indices)