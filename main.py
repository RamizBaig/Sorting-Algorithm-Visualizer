import pygame
pygame.init()

from mainMenu import renderMenu, menuInput, resetMenuValues
from visualization import renderVisualization, visualizationInput, resetVisualizationValues
from results import renderResults, resultsInput, resetResultValues

gameStates = {"mainMenu": True, "visualization": False, "results": False}
sortingOptions = {"Bubble": False, "Insertion": False, "Quick": False, "Selection": False}
passes = None

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

running = True
while running:
    pygame.display.update()
    if gameStates["mainMenu"]:
        renderMenu(screen, sortingOptions)
    if gameStates["visualization"]:
        renderVisualization(screen, sortingOptions)
    if gameStates["results"]:
        renderResults(screen, passes)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
        if gameStates["mainMenu"]:
            if menuInput(event, sortingOptions):
                resetMenuValues()
                gameStates["mainMenu"], gameStates["visualization"] = False, True
                
        elif gameStates["visualization"]:
            passes = visualizationInput(event)
            if passes:
                resetVisualizationValues()
                gameStates["visualization"], gameStates["results"] = False, True
                
        elif gameStates["results"]:
            if resultsInput(event):
                resetResultValues()
                gameStates["results"], gameStates["mainMenu"] = False, True
                sortingOptions = {"Bubble": False,"Insertion": False,"Quick": False,"Selection": False}
            
pygame.quit()