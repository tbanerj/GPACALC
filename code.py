import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Function to calculate GPA
def calculate_gpa(grades):
    total_points = sum(grades.values())
    num_courses = len(grades)
    gpa = total_points / num_courses
    return round(gpa, 2)

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GPA Calculator")

    grades = {}  # Dictionary to store course grades

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    course_name = input("Enter course name: ")
                    grade = int(event.unicode)
                    grades[course_name] = grade

        # Clear the screen
        screen.fill(WHITE)

        # Display current grades
        y = 50
        for course, grade in grades.items():
            text = FONT.render(f"{course}: {grade}", True, BLACK)
            screen.blit(text, (50, y))
            y += 30

        # Display GPA
        gpa = calculate_gpa(grades)
        gpa_text = FONT.render(f"GPA: {gpa}", True, BLACK)
        screen.blit(gpa_text, (50, y + 30))

        pygame.display.flip()

if __name__ == "__main__":
    main()
