import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create a GRUCell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_tensor = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5
hidden_state = torch.randn(5, hidden_size)  # Batch size of 5

# Process the input through the GRUCell
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print(updated_hidden_state)