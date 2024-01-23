import os

def calculate_tax_from_file(filepath):
    # Initialize variables
    total_income = 0
    deduction_80C = 0
    deduction_10_13A = 0
    deduction_10_14 = 0
    deduction_16 = 0
    deduction_VIA = 0

    # Read the values from the file
    with open(filepath, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            if key == 'total income':
                total_income = float(value)
            elif key == '80C':
                deduction_80C = float(value)
            elif key == '10(13A)':
                deduction_10_13A = float(value)
            elif key == '10(14)(i)':
                deduction_10_14 = float(value)
            elif key == '16':
                deduction_16 = float(value)
            elif key == 'VIA':
                deduction_VIA = float(value)

    # Calculate taxable income
    taxable_income = total_income - (deduction_80C + deduction_10_13A + deduction_10_14 + deduction_16 + deduction_VIA)
    return calculate_tax(taxable_income)

def calculate_tax(taxable_income):
    # Define the tax slabs and rates as per the old regime
    tax_slabs = [(250000, 0.05), (500000, 0.1), (1000000, 0.2), (float('inf'), 0.3)]
    tax = 0
    remaining_income = taxable_income

    for slab in tax_slabs:
        if remaining_income > slab[0]:
            tax += slab[0] * slab[1]
            remaining_income -= slab[0]
        else:
            tax += remaining_income * slab[1]
            break

    return tax

# Main program
def main():
    filepath = 'income.prop'
    
    if os.path.exists(filepath):
        tax = calculate_tax_from_file(filepath)
    else:
        # If the file does not exist, prompt the user for input
        total_income = float(input("Enter your total income: "))
        deduction_80C = float(input("Enter deductions under Section 80C (up to 1.5 lakhs): "))
        deduction_10_13A = float(input("Enter deductions under Section 10(13A) – HRA: "))
        deduction_10_14 = float(input("Enter deductions under Section 10(14)(i): "))
        deduction_16 = float(input("Enter deductions under Section 16 – Standard Deduction etc.: "))
        deduction_VIA = float(input("Enter deductions under Chapter VI A (total, consider permissible limits): "))
        
        # Calculate taxable income
        taxable_income = total_income - (deduction_80C + deduction_10_13A + deduction_10_14 + deduction_16 + deduction_VIA)
        tax = calculate_tax(taxable_income)

    # Print the final tax
    print(f"Your income tax for the year under the old regime is: ₹{tax:.2f}")

if __name__ == '__main__':
    main()

