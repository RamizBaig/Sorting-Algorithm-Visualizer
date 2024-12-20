import pygame
pygame.init()

options = [["Insertion", "Selection"], ["Bubble", "Quick"]]
pos = (0, 0)

def renderMenu(screen, sortingOptions):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Select Sorting Algorithms", True, (255, 255, 255))
    hint1 = font2.render("Hint: use the arrow keys and spacebar to navigate", True, (255,255,255))
    hint2 = font2.render("Hint: click enter to continue", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 540))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 560))
    
    pygame.draw.rect(screen, (200,200, 30), pygame.Rect(90+400*pos[1], 140+200*pos[0], 220, 120))
    for i in range(len(options)):
        for j in range(len(options[i])):
            color = (50, 220, 100) if sortingOptions[options[i][j]] else (200, 40, 40)
            pygame.draw.rect(screen, color, pygame.Rect(100+400*j, 150+200*i, 200, 100))
            name = font2.render(options[i][j], True, (0,0,0))
            screen.blit(name, (200+400*j - name.get_width()//2, 200+200*i-name.get_height()//2))

def menuInput(event, sortingOptions):
    global pos
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_SPACE:
                sortingOptions[options[pos[0]][pos[1]]] = not sortingOptions[options[pos[0]][pos[1]]]
            case pygame.K_DOWN | pygame.K_s:
                pos = (1, pos[1])
            case pygame.K_UP | pygame.K_w:
                pos = (0, pos[1])
            case pygame.K_LEFT | pygame.K_a:
                pos = (pos[0], 0)
            case pygame.K_RIGHT | pygame.K_d:
                pos = (pos[0], 1)
            case pygame.K_RETURN:
                if any(sortingOptions[i] for i in ("Insertion", "Selection", "Bubble", "Quick")):
                    return True
    
def resetMenuValues():
    global pos
    pos = (0, 0)