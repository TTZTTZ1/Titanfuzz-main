import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and hidden state
input_tensor = torch.randn(3, input_size)  # Batch size of 3, sequence length of 1, feature dimension of 10
hidden_state = torch.randn(3, hidden_size)  # Batch size of 3, hidden dimension of 20

# Update the hidden state
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)