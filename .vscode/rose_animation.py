import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beautiful Growing Rose")

# Colors
BACKGROUND = (10, 10, 40)
STEM_GREEN = (30, 120, 30)
LEAF_GREEN = (50, 180, 70)
ROSE_RED = (220, 30, 60)
ROSE_PINK = (255, 150, 180)
ROSE_DARK = (180, 20, 50)
YELLOW = (255, 225, 50)
PURPLE = (180, 70, 220)

# Animation parameters
growth_factor = 0
max_growth = 100
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20, bold=True)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-2, -0.5)
        self.size = random.uniform(1, 3)
        self.color = random.choice([ROSE_PINK, ROSE_RED, PURPLE, (255, 255, 200)])
        self.lifetime = random.randint(30, 100)
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.05  # Gravity
        self.lifetime -= 1
        
    def draw(self, surface):
        alpha = min(255, self.lifetime * 3)
        color_with_alpha = (self.color[0], self.color[1], self.color[2], alpha)
        pygame.draw.circle(surface, color_with_alpha, (int(self.x), int(self.y)), int(self.size))

# Create a transparent surface for particles
particle_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
particles = []

# Main loop
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                growth_factor = 0  # Reset animation
                particles = []
    
    # Clear screen
    screen.fill(BACKGROUND)
    
    # Draw stars in background
    for i in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)
    
    # Increase growth factor
    if growth_factor < max_growth:
        growth_factor += 0.5
    
    # Calculate current sizes based on growth factor
    stem_height = 200 * (growth_factor / max_growth)
    rose_size = 80 * (growth_factor / max_growth)
    leaf_size = 30 * (growth_factor / max_growth)
    
    # Draw stem
    pygame.draw.line(screen, STEM_GREEN, (WIDTH//2, HEIGHT), (WIDTH//2, HEIGHT - stem_height), 5)
    
    # Draw leaves
    if growth_factor > 20:
        leaf_y = HEIGHT - stem_height * 0.7
        # Left leaf
        pygame.draw.ellipse(screen, LEAF_GREEN, (WIDTH//2 - 40, leaf_y, leaf_size, leaf_size*0.7))
        # Right leaf
        pygame.draw.ellipse(screen, LEAF_GREEN, (WIDTH//2 + 40 - leaf_size, leaf_y, leaf_size, leaf_size*0.7))
    
    # Draw rose
    if growth_factor > 30:
        center_x, center_y = WIDTH//2, HEIGHT - stem_height
        
        # Draw outer petals
        for i in range(8):
            angle = i * (2 * math.pi / 8) + growth_factor * 0.01
            petal_size = rose_size * (0.8 + 0.2 * math.sin(growth_factor * 0.1))
            x = center_x + math.cos(angle) * petal_size * 0.8
            y = center_y + math.sin(angle) * petal_size * 0.8
            
            # Draw petal
            points = []
            for j in range(10):
                a = j * (2 * math.pi / 10)
                r = petal_size * (0.5 + 0.5 * math.sin(a * 2))
                px = x + math.cos(a + angle) * r
                py = y + math.sin(a + angle) * r
                points.append((px, py))
            
            pygame.draw.polygon(screen, ROSE_PINK, points)
            pygame.draw.polygon(screen, ROSE_RED, points, 2)
        
        # Draw inner petals
        for i in range(6):
            angle = i * (2 * math.pi / 6) + growth_factor * 0.02
            petal_size = rose_size * (0.5 + 0.2 * math.cos(growth_factor * 0.1))
            x = center_x + math.cos(angle) * petal_size * 0.5
            y = center_y + math.sin(angle) * petal_size * 0.5
            
            # Draw petal
            points = []
            for j in range(10):
                a = j * (2 * math.pi / 10)
                r = petal_size * (0.5 + 0.5 * math.sin(a * 2))
                px = x + math.cos(a + angle) * r
                py = y + math.sin(a + angle) * r
                points.append((px, py))
            
            pygame.draw.polygon(screen, ROSE_RED, points)
            pygame.draw.polygon(screen, ROSE_DARK, points, 1)
        
        # Draw center of the rose
        pygame.draw.circle(screen, YELLOW, (center_x, center_y), rose_size * 0.2)
        
        # Draw center details
        for i in range(10):
            angle = i * (2 * math.pi / 10) + growth_factor * 0.05
            x = center_x + math.cos(angle) * rose_size * 0.15
            y = center_y + math.sin(angle) * rose_size * 0.15
            pygame.draw.circle(screen, (240, 150, 30), (int(x), int(y)), int(rose_size * 0.05))
        
        # Add particles when rose is fully grown
        if growth_factor > 90:
            for _ in range(3):
                particles.append(Particle(center_x + random.uniform(-10, 10), 
                                         center_y + random.uniform(-10, 10)))
    
    # Update and draw particles
    particle_surface.fill((0, 0, 0, 0))  # Clear with transparent color
    for particle in particles[:]:
        particle.update()
        if particle.lifetime <= 0:
            particles.remove(particle)
        else:
            particle.draw(particle_surface)
    
    screen.blit(particle_surface, (0, 0))
    
    # Draw message
    if growth_factor > 90:
        message = "For someone special..."
        text = font.render(message, True, (255, 255, 255))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//4))
    
    # Display instructions
    instructions = [
        "Press 'r' to reset animation",
        "Press ESC to quit",
        "Watch the beautiful rose grow"
    ]
    
    for i, instruction in enumerate(instructions):
        text = font.render(instruction, True, (200, 200, 200))
        screen.blit(text, (10, 10 + i * 25))
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()