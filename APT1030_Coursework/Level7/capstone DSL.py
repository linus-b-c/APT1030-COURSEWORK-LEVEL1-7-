# Level 7: Mobile Money DSL Interpreter

class MobileMoneyDSL:
    def __init__(self, sender_balance):
        self.balance = sender_balance

    def process_command(self, command):
        print(f"\nProcessing Command: '{command}'")
        
        # 1. THE PARSER: Breaking the string into tokens
        # Example: "TRANSFER 5000 FROM Alice TO Bob IF BALANCE > 1000"
        tokens = command.split()

        try:
            # 2. EXTRACTION: Mapping tokens to variables
            # We assume a fixed syntax structure:
            # [0]TRANSFER [1]Amount [2]FROM [3]Sender [4]TO [5]Receiver [6]IF [7]BALANCE [8]> [9]Threshold
            amount = float(tokens[1])
            sender = tokens[3]
            receiver = tokens[5]
            threshold = float(tokens[9])

            print(f"--- Parsing Successful ---")
            print(f"Amount: {amount} | Sender: {sender} | Receiver: {receiver}")

            # 3. INTERPRETER LOGIC: Validating the rule
            if self.balance < amount:
                return "TRANSACTION FAILED: Insufficient Funds."
            
            if self.balance <= threshold:
                return f"TRANSACTION FAILED: Balance must be above {threshold} to transfer."

            # 4. EXECUTION
            self.balance -= amount
            return f"TRANSACTION SUCCESS: {amount} sent from {sender} to {receiver}. New Balance: {self.balance}"

        except (IndexError, ValueError):
            return "SYNTAX ERROR: Command does not match DSL rules."

# --- Testing the DSL ---
# Setup: Alice has 10,000 KES
m_pesa_engine = MobileMoneyDSL(10000)

# Test Case 1: Valid Transaction
cmd1 = "TRANSFER 5000 FROM Alice TO Bob IF BALANCE > 1000"
print(m_pesa_engine.process_command(cmd1))

# Test Case 2: Violation of the 'IF' rule
cmd2 = "TRANSFER 2000 FROM Alice TO Charlie IF BALANCE > 8000"
print(m_pesa_engine.process_command(cmd2))