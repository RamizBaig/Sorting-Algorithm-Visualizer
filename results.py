import pygame
pygame.init()

orderedOptions = []
sorted = False

def resultsInput(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return True
        
def renderResults(screen, passes):
    if not sorted:
        order(passes)
        
    screen.fill((30,30,30))
    font = pygame.font.Font(None, 50)
    for i in range(len(orderedOptions)):
        name = font.render(orderedOptions[i], True, (255,255,255))
        screen.blit(name, (100, 50+150*i))
         
def order(passes):
    global sorted
    orderedOptions.clear()
    if passes[1][1]:
        orderedOptions.append("Quick Sort comparisons: " + (str)(passes[1][1]))
    if passes[0][0]:
        orderedOptions.append("Insertion Sort comparisons: " + (str)(passes[0][0]))
    if passes[1][0]:
        orderedOptions.append("Bubble Sort comparisons: " + (str)(passes[1][0]))
    if passes[0][1]: 
        orderedOptions.append("Selection Sort comparisons: " + (str)(passes[0][1]))
    sorted = True
                
def resetResultValues():
    global orderedOptions, sorted
    orderedOptions = []
    sorted = False