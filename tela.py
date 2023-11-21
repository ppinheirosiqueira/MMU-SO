import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Botão Clicável")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Fonte e texto do botão
font = pygame.font.Font(None, 36)
button_text = font.render("Clica aqui PEPE!", True, black)
button_rect = button_text.get_rect(center=(100, 15))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Botão clicado!")

    # Preencher a tela com a cor branca
    screen.fill(white)

    # Desenhar o botão
    pygame.draw.rect(screen, black, button_rect, 2)
    screen.blit(button_text, button_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização da tela
    pygame.time.Clock().tick(60)
