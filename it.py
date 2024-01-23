# Define the tax slabs and rates as per the old regime
tax_slabs = [(250000, 0.05), (500000, 0.1), (1000000, 0.2), (float('inf'), 0.3)]
# Input total income
total_income = float(input("Enter your total income: "))

# Input deductions
deduction_80C = float(input("Enter deductions under Section 80C (up to 1.5 lakhs): "))
deduction_10_13A = float(input("Enter deductions under Section 10(13A) – HRA: "))
deduction_10_14 = float(input("Enter deductions under Section 10(14)(i): "))
deduction_16 = float(input("Enter deductions under Section 16 – Standard Deduction etc.: "))
deduction_VIA = float(input("Enter deductions under Chapter VI A (total, consider permissible limits): "))

# Calculate taxable income
taxable_income = total_income - (deduction_80C + deduction_10_13A + deduction_10_14 + deduction_16 + deduction_VIA)

# Calculate tax based on slabs
tax = 0
remaining_income = taxable_income

for slab in tax_slabs:
    slab_limit, slab_rate = slab
    if remaining_income > slab_limit:
        tax += (slab_limit) * slab_rate
        remaining_income -= slab_limit
    else:
        tax += remaining_income * slab_rate
        break

# Print the final tax
print(f"Your income tax for the year under the old regime is: ₹{tax:.2f}")
