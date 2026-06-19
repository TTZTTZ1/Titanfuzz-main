import torch

# Define input size and hidden size
input_size = 10
hidden_size = 20

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and hidden state
input_tensor = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5
hidden_state = torch.randn(5, hidden_size)

# Update the hidden state
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)