import streamlit as st
import random

def generate_recipe(ingredients, diet_preference):
    # Split and clean the ingredient list
    ingredient_list = [ing.strip().lower() for ing in ingredients.split(',') if ing.strip()]
    
    # Basic recipe structure
    recipe = {
        "title": f"{ingredient_list[0].capitalize()} {random.choice(['Curry', 'Sabzi', 'Tikka', 'Biryani', 'Dal'])}",
        "ingredients": ingredients,
        "instructions": []
    }
    
    # Cooking instructions based on ingredients
    if 'rice' in ingredient_list:
        recipe["instructions"].append("Cook the rice according to package instructions.")
    
    # Prepare vegetables
    veggies = [ing for ing in ingredient_list if ing in ['onion', 'garlic', 'tomatoes', 'bell peppers', 'potatoes', 'spinach', 'cauliflower', 'peas', 'carrots']]
    if veggies:
        recipe["instructions"].append(f"Chop {', '.join(veggies)}.")
        recipe["instructions"].append(f"Heat oil in a pan and add {', '.join(veggies)}. Sauté until softened.")
    
    # Proteins for vegetarian and non-vegetarian
    if diet_preference == 'non-vegetarian':
        proteins = [ing for ing in ingredient_list if ing in ['chicken', 'mutton', 'fish', 'shrimp']]
        if proteins:
            recipe["instructions"].append(f"Cook {proteins[0]} in a separate pan with spices until done.")
            recipe["instructions"].append(f"Add the cooked {proteins[0]} to the vegetable mix.")
    
    if 'paneer' in ingredient_list:
        recipe["instructions"].append("Cut the paneer into cubes and lightly fry until golden brown.")
    
    if 'tofu' in ingredient_list or 'chickpeas' in ingredient_list:
        protein = 'tofu' if 'tofu' in ingredient_list else 'chickpeas'
        recipe["instructions"].append(f"Add {protein} to the pan and cook for a few minutes.")
    
    # Spices and seasoning
    spices = [ing for ing in ingredient_list if ing in ['salt', 'pepper', 'cumin', 'coriander', 'turmeric', 'garam masala', 'mustard seeds', 'red chili powder', 'asafoetida', 'fenugreek']]
    if spices:
        recipe["instructions"].append(f"Add {', '.join(spices)} to the pan and cook for a few minutes.")
    
    # Cooking Dals
    if 'dal' in ingredient_list or 'lentils' in ingredient_list:
        recipe["instructions"].append("Boil the dal in water until soft, then mash lightly and add to the vegetable mix.")
    
    # Finishing touches
    if 'coconut milk' in ingredient_list:
        recipe["instructions"].append("Pour in coconut milk and simmer for 10-15 minutes.")
    
    recipe["instructions"].append("Adjust seasoning if needed.")
    recipe["instructions"].append("Serve hot with rice or roti and enjoy your meal!")

    return recipe["title"], recipe["ingredients"], "\n".join(f"{i+1}. {step}" for i, step in enumerate(recipe["instructions"]))

# Streamlit interface
st.title("AI-Powered Indian Recipe Generator")
st.write("Enter your ingredients to get a personalized Indian recipe:")

ingredients_input = st.text_area("Ingredients (comma-separated):")
diet_preference = st.radio("Diet Preference", ("vegetarian", "non-vegetarian"))

if st.button("Generate Recipe"):
    if ingredients_input:
        try:
            with st.spinner("Generating recipe..."):
                title, ingredients, instructions = generate_recipe(ingredients_input, diet_preference)
                st.write("### Generated Recipe:")
                st.write(f"**Recipe Title:** {title}")
                st.write(f"**Ingredients:** {ingredients}")
                st.write(f"**Instructions:**\n{instructions}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter some ingredients.")
