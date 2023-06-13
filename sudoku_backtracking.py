
import pygame

WIDTH = 540
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro de Sudoku")

puzzle = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

def draw_board():
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, (50, 50, 450, 450), 2)

    for x in range(9):
        if x % 3 == 0:
            line_thickness = 4
        else:
            line_thickness = 2
        pygame.draw.line(window, BLACK, (50 + x * 50, 50), (50 + x * 50, 500), line_thickness)
        pygame.draw.line(window, BLACK, (50, 50 + x * 50), (500, 50 + x * 50), line_thickness)

    font = pygame.font.Font(None, 36)

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                number_text = font.render(str(puzzle[i][j]), True, BLACK)
                window.blit(number_text, (75 + j * 50, 60 + i * 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    pygame.display.update()

pygame.quit()

def violare_constraintes(num,col,line,blc,constraints):
    if col != []:
        res = same_col(num,col)
        if res: 
            return True
    elif line != []:
        res = same_line(num,line)
        if res: 
            return True
    elif blc != []:
        res = same_block(num,blc)
        if res: 
            return True
    return False

def create_block(blc, lin, col):


def backtracking(sol=[],mtx,constraints):

    for lin in sol:
        for col in lin:
            if sol[lin,col] == 0:
                for num in range(1,10):
                        blc =  create_block(blc=[], lin, col)
                        new_v = violare_constraintes(num, lin, col, blc, constraints)
                

            
   


if __name__ == '__main__':
    constraints = [same_col,same_line,same_block]
    mtx = puzzle
    print(mtx) 
    res = backtracking(puzzle, constraints)
