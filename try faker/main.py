"""
Faker Library Full Example
--------------------------
This script demonstrates most of the key features of the Faker library.
It includes:
  - Generating fake personal data (name, address, etc.)
  - Using locales (for different languages)
  - Seeding (for reproducible fake data)
  - Generating multiple fake records
  - Using built-in providers (like job, company, text, etc.)
  - Custom fake profiles and data structures
"""

import json
from decimal import Decimal
from datetime import date
from faker import Faker

# 1️⃣ Create a Faker instance
fake = Faker()

# 2️⃣ Generate basic fake personal information
print("=" * 50)
print("🔹 Basic Fake Data")
print("=" * 50)
print("Name:", fake.name())
print("Address:\n", fake.address())
print("Email:", fake.email())
print("Phone:", fake.phone_number())
print("Date of Birth:", fake.date_of_birth(minimum_age=18, maximum_age=80))
print("Job:", fake.job())
print("Company:", fake.company())
print("Text (paragraph):", fake.paragraph())

# 3️⃣ Generate internet-related fake data
print("\n" + "=" * 50)
print("🔹 Internet and Web Data")
print("=" * 50)
print("Username:", fake.user_name())
print("URL:", fake.url())
print("IPv4:", fake.ipv4())
print("IPv6:", fake.ipv6())
print("Domain Name:", fake.domain_name())
print("Email Domain:", fake.free_email_domain())

# 4️⃣ Geographic & address details
print("\n" + "=" * 50)
print("🔹 Location and Address Data")
print("=" * 50)
print("City:", fake.city())
print("State:", fake.state())
print("Country:", fake.country())
print("Postcode:", fake.postcode())
print("Latitude:", fake.latitude())
print("Longitude:", fake.longitude())

# 5️⃣ Financial & Business info
print("\n" + "=" * 50)
print("🔹 Financial / Business Data")
print("=" * 50)
print("Credit Card Number:", fake.credit_card_number())
print("Credit Card Provider:", fake.credit_card_provider())
print("Credit Card Expire:", fake.credit_card_expire())
print("Currency Name:", fake.currency_name())
print("Currency Code:", fake.currency_code())

# 6️⃣ Locale examples (French and Japanese)
print("\n" + "=" * 50)
print("🔹 Locale Examples")
print("=" * 50)
fake_fr = Faker('fr_FR')
fake_jp = Faker('ja_JP')
print("French Name:", fake_fr.name())
print("Japanese Name:", fake_jp.name())
print("French Address:\n", fake_fr.address())
print("Japanese Address:\n", fake_jp.address())

# 7️⃣ Seeding (reproducible fake data)
print("\n" + "=" * 50)
print("🔹 Seeding Example (Reproducibility)")
print("=" * 50)
Faker.seed(1234)
fake.seed_instance(1234)
print("Seeded Name 1:", fake.name())
print("Seeded Name 2:", fake.name())  # Will be the same every run with same seed

# 8️⃣ Generating multiple fake user records
print("\n" + "=" * 50)
print("🔹 Generate Multiple Fake Users")
print("=" * 50)

users = []
for _ in range(5):
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "dob": str(fake.date_of_birth(minimum_age=18, maximum_age=80)),
        "job": fake.job(),
        "company": fake.company(),
        "phone": fake.phone_number()
    }
    users.append(user)

# Print in readable format
for i, user in enumerate(users, 1):
    print(f"\nUser {i}:")
    for key, value in user.items():
        print(f"  {key.capitalize()}: {value}")

# 9️⃣ Exporting fake data to JSON (for databases, APIs, etc.)
print("\n" + "=" * 50)
print("🔹 Exporting Data to JSON")
print("=" * 50)

with open("fake_users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=4, ensure_ascii=False)
print("✅ Saved 5 fake users to 'fake_users.json'")

# 🔟 Bonus: Using built-in profile generator
print("\n" + "=" * 50)
print("🔹 Faker Built-in Profiles")
print("=" * 50)
profile = fake.profile()

# Function to convert non-serializable types (Decimal and date) to serializable formats
def convert_special_types(obj):
    """Convert Decimal objects to float and date objects to string for JSON serialization."""
    if isinstance(obj, Decimal):
        return float(obj)  # Convert Decimal to float
    elif isinstance(obj, date):  # Handle date objects
        return obj.isoformat()  # Converts the date to a string in YYYY-MM-DD format
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")

print(json.dumps(profile, default=convert_special_types, indent=4, ensure_ascii=False))
