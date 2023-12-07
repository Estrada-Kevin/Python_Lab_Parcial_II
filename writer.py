import pygame
import re
class Writer:
    #init the writer with the screen,font,size, and text color
    def __init__(self,screen,font,size,text_color):
        self.screen = screen
        self.font = pygame.font.SysFont(font,size)
        self.text_color = text_color

    #write a text on the screen
    #param: text to write, coordinates, and if optional param is in False it will automatically writes in a certain coordinate
    def write_text(self, text, x, y,manual=False):
        text_img = self.font.render(text,True,self.text_color)
        if manual == False:
            self.screen.blit(text_img,((x - text_img.get_width()) / 2,(y - text_img.get_height())/2 ))
        else:
            self.screen.blit(text_img,((x,y)))
    
    #write a text list on the screen
    #param: text to write, coordinates
    def write_text_list(self, text, x, y):
        for item in self.filter_list(text):
            item = item.replace("\n", "").replace("\r", "")
            item_img = self.font.render(item, True, self.text_color)
            width, height = item_img.get_size()
            self.screen.blit(item_img, (x - (width / 2), y))
            y += height
      
    #filter the list to show in the screen later
    #param: list to filter
    def filter_list(self,score_list):
        try:
        # Extract scores from the original list
            scores_as_strings = [re.search(r"Score: (\d+)", item).group(1) for item in score_list]
            scores_as_integers = [int(score) for score in scores_as_strings]

            # Sort scores in descending order
            sorted_scores = sorted(scores_as_integers, reverse=True)

            # Select the top 5 scores
            top_5_scores = sorted_scores[:5]

            # Filter the original list based on the top 5 scores
            selected_elements = [item for item, score in zip(score_list, scores_as_integers) if score in top_5_scores]

            return selected_elements
        except IndexError:
            print("Error. The list is empty.")
        except ValueError:
            print("Error. Conversion failed")



