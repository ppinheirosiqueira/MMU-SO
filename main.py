import pygame
import sys
import arquivo

def iniciarTela():
    pygame.init()

    # Configurações da tela
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("MMU")

    # Cores
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Fonte e texto do botão
    font = pygame.font.Font(None, 30)
    button_text = font.render("Selecionar Arquivo", True, black)
    button_rect = button_text.get_rect(center=(100, 15))
    button_textClose = font.render("FECHAR JOGO", True, black)
    button_close = button_text.get_rect(center=(100,15))
    button_close.topleft = (1200, 0)

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    arquivo.abrir_arquivo()
                if button_close.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Preencher a tela com a cor branca
        screen.fill(white)

        # Desenhar o botão
        pygame.draw.rect(screen, black, button_rect, 2)
        pygame.draw.rect(screen, black, button_close, 3)
        screen.blit(button_text, button_rect.topleft)
        screen.blit(button_textClose, button_close.topleft)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização da tela
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    iniciarTela()
