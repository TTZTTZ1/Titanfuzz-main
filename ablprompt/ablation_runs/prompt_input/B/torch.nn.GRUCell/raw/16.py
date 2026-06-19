import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_sequence = torch.randn(5, 3, 10)  # Sequence length x Batch size x Input size
initial_hidden_state = torch.randn(3, 20)  # Batch size x Hidden size

# Process each time step
hidden_states = []
for input_step in input_sequence:
    hidden_state = gru_cell(input_step, initial_hidden_state)
    hidden_states.append(hidden_state)
    initial_hidden_state = hidden_state

# Convert list to tensor for further processing if needed
hidden_states_tensor = torch.stack(hidden_states)
print(hidden_states_tensor.shape)  # Should be (5, 3, 20)