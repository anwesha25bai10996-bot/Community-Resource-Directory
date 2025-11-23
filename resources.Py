resources = {
    'food': ['Food Bank A', 'Community Kitchen B', 'Meals on Wheels'],
    'shelter': ['Homeless Shelter X', 'Transitional Housing Y'],
    'health': ['Free Clinic 1', 'Mental Health Center 2'],
    'employment': ['Job Training Program A', 'Career Center B']
}

print("Available resource categories:")
for category in resources:
    print(f"- {category}")

need = input("\nWhat type of resource do you need? ").lower()
if need in resources:
    print(f"\nResources for {need}:")
    for resource in resources[need]:
        print(f"  - {resource}")
else:
    print("Category not found")