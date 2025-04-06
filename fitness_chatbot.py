import random

class FitnessBot:
    def __init__(self):
        self.responses = {
            'workout': [
                "Here's a quick workout: 20 pushups, 30 squats, and 40 jumping jacks!",
                "Try this: 15 minutes of jogging followed by stretching exercises.",
                "How about: 3 sets of 10 burpees, 15 lunges, and 20 mountain climbers?"
            ],
            'diet': [
                "Remember to eat plenty of protein and vegetables!",
                "Try to maintain a balanced diet with lean proteins, whole grains, and fresh vegetables.",
                "Don't forget to stay hydrated! Aim for 8 glasses of water daily."
            ],
            'motivation': [
                "You've got this! Every step counts towards your fitness goals!",
                "Remember: Your only competition is yourself!",
                "Small progress is still progress. Keep going!"
            ]
        }
        
        self.workout_plans = {
            'beginner': {
                'cardio': {
                    'minimal': ['10 minutes jogging in place', '20 jumping jacks', '10 high knees'],
                    'standard': ['20 minutes light jogging', '10 minutes cycling', '15 minutes swimming']
                },
                'strength': {
                    'minimal': ['10 pushups', '15 squats', '10 lunges per leg'],
                    'standard': ['3x10 dumbbell rows', '3x10 bench press', '3x12 squats']
                }
            },
            'intermediate': {
                'cardio': {
                    'minimal': ['20 minutes HIIT', '100 jumping jacks', '50 burpees'],
                    'standard': ['30 minutes running', '20 minutes cycling intervals', '30 minutes swimming']
                },
                'strength': {
                    'minimal': ['20 pushups', '30 squats', '20 lunges per leg'],
                    'standard': ['4x12 dumbbell rows', '4x10 bench press', '4x15 squats']
                }
            },
            'advanced': {
                'cardio': {
                    'minimal': ['30 minutes HIIT', '150 jumping jacks', '75 burpees'],
                    'standard': ['45 minutes running', '30 minutes cycling intervals', '45 minutes swimming']
                },
                'strength': {
                    'minimal': ['30 pushups', '50 squats', '30 lunges per leg'],
                    'standard': ['5x12 dumbbell rows', '5x10 bench press', '5x15 squats']
                }
            }
        }
        self.user_preferences = None

    def get_user_preferences(self):
        print("\nLet me create a custom workout plan for you.")
        
        while True:
            level = input("What's your fitness level? (beginner/intermediate/advanced): ").lower()
            if level in ['beginner', 'intermediate', 'advanced']:
                break
            print("Please choose beginner, intermediate, or advanced.")

        while True:
            workout_type = input("Do you prefer cardio or strength training?: ").lower()
            if workout_type in ['cardio', 'strength']:
                break
            print("Please choose cardio or strength.")

        while True:
            equipment = input("Do you have access to gym equipment? (yes/no): ").lower()
            equipment_level = 'standard' if equipment == 'yes' else 'minimal'
            if equipment in ['yes', 'no']:
                break
            print("Please answer yes or no.")

        self.user_preferences = {
            'level': level,
            'type': workout_type,
            'equipment': equipment_level
        }
        return self.create_custom_workout()

    def create_custom_workout(self):
        if not self.user_preferences:
            return "Please set your preferences first!"
        
        plan = self.workout_plans[self.user_preferences['level']]
        type_plan = plan[self.user_preferences['type']]
        workout = type_plan[self.user_preferences['equipment']]
        
        return f"Here's your custom workout plan:\n" + "\n".join(f"- {exercise}" for exercise in workout)

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if any(word in user_input for word in ['custom', 'plan', 'personal']):
            return self.get_user_preferences()
            
        if any(word in user_input for word in ['workout', 'exercise', 'training', 'routine']):
            return random.choice(self.responses['workout'])
            
        if any(word in user_input for word in ['eat', 'food', 'diet', 'nutrition']):
            return random.choice(self.responses['diet'])
            
        if any(word in user_input for word in ['motivate', 'tired', 'give', 'up']):
            return random.choice(self.responses['motivation'])
            
        return "I'm your fitness assistant! You can ask me about workouts, diet, or motivation!"

def main():
    print("🏋️‍♂️ Fitness Chatbot: Hello! I'm your personal fitness assistant!")
    print("You can ask me about workouts, diet tips, or get some motivation.")
    print("Type 'custom plan' to get a personalized workout plan.")
    print("Type 'quit' to exit.")

    bot = FitnessBot()
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() == 'quit':
                print("Fitness Chatbot: Goodbye! Stay healthy! 💪")
                break
            
            response = bot.get_response(user_input)
            print(f"Fitness Chatbot: {response}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
