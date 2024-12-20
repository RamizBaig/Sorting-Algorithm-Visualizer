import pygame
import time
from sortingAlgorithms import insertionSort, selectionSort, bubbleSort, quickSort
pygame.init()

options = [["Insertion", "Selection"], ["Bubble", "Quick"]]
sortingGenerators = [[None, None],[None, None]]
arrays = [[None, None],[None, None]]
sorted = [[None, None],[None, None]]
passes = [[0, 0],[0, 0]]
completed = False
started = False
size = 70 # best with a factor of 350
timeDelay = 0.005

def visualizationInput(event):
    global completed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            if completed: 
                return passes
                    
def renderVisualization(screen, sortingOptions):
    screen.fill((30,30,30))
    font = pygame.font.Font(None, 26)
    if not started:
        createSortingGenerators(sortingOptions)
    if not completed:
        tickSortingAlgorithms()
                
    for i in range(len(options)):
        for j in range(len(options[i])):
            color = (20, 200, 20) if sorted[i][j] else (200, 20, 20)
            if sortingOptions[options[i][j]]:
                name = font.render(options[i][j], True, (255,255,255))
                screen.blit(name, (200+400*j - name.get_width()//2, 20+300*i))
                if arrays[i][j]:
                    for index in range(len(arrays[i][j])):
                        height = arrays[i][j][index]
                        pygame.draw.rect(screen, (0,0,0), pygame.Rect(24 + j*400 + index*350//size, 250 - height + 300 * i-1, 350//size+2, height+2))
                        pygame.draw.rect(screen, color, pygame.Rect(25 + j*400 + index*350//size, 250 - height + 300 * i, 350//size, height))
                
    time.sleep(timeDelay)
    
def createSortingGenerators(sortingOptions):
    global started
    started = True
    import random
    array = [random.randint(1,200) for _ in range(size)]
    if sortingOptions[options[0][0]]:
        sortingGenerators[0][0] = insertionSort(array.copy())
    if sortingOptions[options[0][1]]:
        sortingGenerators[0][1] = selectionSort(array.copy())
    if sortingOptions[options[1][0]]:
        sortingGenerators[1][0] = bubbleSort(array.copy())
    if sortingOptions[options[1][1]]:
        sortingGenerators[1][1] = quickSort(array.copy())
   
def tickSortingAlgorithms():
    global arrays, completed
    for i in range(len(options)):
        for j in range(len(options[i])):
            try:
                if not sorted[i][j]:
                    arrays[i][j] = next(sortingGenerators[i][j])
                    passes[i][j] += 1
            except:
                sorted[i][j] = True
    completed = all(sorted[i][j] for i, j in ((0, 0), (0, 1), (1, 0), (1, 1)))

def resetVisualizationValues():
    global sortingGenerators, arrays,sorted,passes,completed,started
    sortingGenerators = [[None, None],[None, None]]
    arrays = [[None, None],[None, None]]
    sorted = [[None, None],[None, None]]
    passes = [[0, 0],[0, 0]]
    completed = False
    started = False