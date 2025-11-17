user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birthday: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

def generate_profile(age):
    if age < 0:
        return "Error"
    if age <= 12:
        return "Child"
    if age <= 19:
        return "Teenager"
    else:
        return "Adult"

life_stage = generate_profile(current_age)
hobbies = []

while True:
    hobby = input("Enter your favorite hobby or type 'stop' to finish: ")
    if hobby == "stop":
        break
    hobbies.append(hobby)

user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

check_hobbies = len(hobbies)
hobbies_text = ""

if check_hobbies > 0:
    for i in range(check_hobbies):
        if i == 0:
            hobbies_text = f"- {hobbies[i]}"
        else:
            hobbies_text += f"\n- {hobbies[i]}"
else:
    hobbies_text = "You didn't enter any hobbies."

print(f"""---
Profile summary:
Name: {user_profile['name']}
Age: {user_profile['age']}
Life stage: {user_profile['stage']}
Favorite hobbies ({check_hobbies}):
{hobbies_text}
---""")