class IntermediateCodeGenerator:
    def __init__(self):
        self.intermediate_code = []

    def generate_code(self, operation, arg1=None, arg2=None, result=None):
        code = {'operation': operation, 'arg1': arg1, 'arg2': arg2, 'result': result}
        self.intermediate_code.append(code)

    def display_code(self):
        for code in self.intermediate_code:
            print(code)

# Example usage:
if __name__ == "__main__":
    generator = IntermediateCodeGenerator()
    generator.generate_code('ADD', 'A', 'B', 'T1')
    generator.generate_code('MULT', 'T1', 'C', 'T2')
    generator.display_code()
