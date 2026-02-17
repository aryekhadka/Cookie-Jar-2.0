import pygame
from cookie import Jar


pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Cookie Jar 2.0")

# Fonts
font = pygame.font.Font("Font/ChocoCrumb.ttf", 38)
font_large = pygame.font.Font("Font/ChocoCrumb.ttf", 50)
font_larger = pygame.font.Font("Font/ChocoCrumb.ttf", 72)
clock = pygame.time.Clock()


# Images
default_surface = pygame.image.load("Graphics/default.png").convert_alpha()
jar_surface = pygame.image.load("Graphics/jar.png").convert_alpha()
action_surface = pygame.image.load("Graphics/actions.png").convert_alpha()
eat_surface = pygame.image.load("Graphics/Eat_cookie.png").convert_alpha()
back_arrow_surface = pygame.image.load("Graphics/back_arrow.png").convert_alpha()
back_arrow_surface_resized = pygame.transform.scale_by(back_arrow_surface, 0.2)
deposit_surface = pygame.image.load("Graphics/deposit.png").convert_alpha()
cookie_surface = pygame.image.load("Graphics/cookie.png").convert_alpha()
cookie_resized_surface = pygame.transform.scale(cookie_surface, (65, 65))


# Texts
start_text = font.render("Press any key to start!", True, (133, 98, 50))
jar_size_text = font.render("Enter jar size: ", True, (140, 96, 40))
error_text = font.render(" ", True, (255, 0, 0))
question_text = font_large.render("What would you like to do?", True, (140, 96, 40))
eat_text = font_large.render("Eat", True, (140, 96, 40))
deposit_text = font_large.render("Deposit", True, (140, 96, 40))
display_text = font_large.render("Display", True, (140, 96, 40))
exit_text = font_large.render("Exit", True, (140, 96, 40))
eat_text_rect = pygame.Rect(190, 105, eat_text.get_width()+30, eat_text.get_height()+10)
deposit_text_rect = pygame.Rect(190, 225, deposit_text.get_width()+30, deposit_text.get_height()+10)
display_text_rect = pygame.Rect(190, 345, display_text.get_width()+30, display_text.get_height()+10)
exit_text_rect = pygame.Rect(190, 465, exit_text.get_width()+30, exit_text.get_height()+10)
back_arrow_rect = back_arrow_surface_resized.get_rect(center = (950, 50))

# input boxes
jar_size_ip = ''
eat_ip = ''
deposit_ip = ''


# input rectangles
jar_size_text_box = pygame.Rect(435, 270, 140, 50)
eat_text_box = pygame.Rect(65, 385, 478, 162)
deposit_text_box = pygame.Rect(105, 300, 478, 162)
eat_text_hover = False
deposit_text_hover = False
display_text_hover = False
exit_text_hover = False
jar_text_active = False
eat_text_active = False
deposit_text_active = False
display_cookies = False
global counter
counter = 0

key = pygame.key.get_pressed()
screen_state = "home"


def display_home_screen() -> None:
    global counter
    screen.blit(default_surface, (0, -50))
    screen.blit(start_text, (320, 510))
    pygame.display.update()
    if counter == 0:
        print("Successfully launched Cookie Jar 2.0!")
        counter += 1


def jar_size_screen() -> None:
    global counter
    screen.blit(jar_surface)
    screen.blit(jar_size_text, (385, 200))
    if jar_text_active:
        color = (133, 98, 50)
    else:
        color = (85, 41, 12)
    pygame.draw.rect(screen, color, jar_size_text_box, 2)
    ip_surface = font.render(jar_size_ip, True, (140, 96, 40))
    screen.blit(ip_surface, (jar_size_text_box.x + 50, jar_size_text_box.y))
    jar_size_text_box.w = max(140, ip_surface.get_width() + 10)
    if counter == 1:
        print("Successfully displayed jar size screen!")
        counter += 1


def display_action_screen(jar) -> None:
    right_offset = 0
    left_offset = 43
    global display_cookies
    cookie_width = 450
    screen.blit(jar_surface, (0, -70))
    screen.blit(action_surface, (0, -10))
    screen.blit(question_text, (200, 0))
    if eat_text_hover:
        pygame.draw.rect(screen, (189, 127, 60), eat_text_rect, border_radius = 30)
        screen.blit(eat_text, (eat_text_rect.x + 15, eat_text_rect.y + 2))
    else:     
        pygame.draw.rect(screen, (87, 46, 17), eat_text_rect, border_radius = 30)
        screen.blit(eat_text, (eat_text_rect.x + 15, eat_text_rect.y + 2))

    if deposit_text_hover:
        pygame.draw.rect(screen, (189, 127, 60), deposit_text_rect, border_radius = 30)
        screen.blit(deposit_text, (deposit_text_rect.x + 15, deposit_text_rect.y + 2))
    else:
        pygame.draw.rect(screen, (87, 46, 17), deposit_text_rect, border_radius = 30)
        screen.blit(deposit_text, (deposit_text_rect.x + 15, deposit_text_rect.y + 2))

    if display_text_hover:
        pygame.draw.rect(screen, (189, 127, 60), display_text_rect, border_radius = 30)
        screen.blit(display_text, (display_text_rect.x + 15, display_text_rect.y + 2))
    else:
        pygame.draw.rect(screen, (87, 46, 17), display_text_rect, border_radius = 30)
        screen.blit(display_text, (display_text_rect.x + 15, display_text_rect.y + 2))
    
    if exit_text_hover:
        pygame.draw.rect(screen, (189, 127, 60), exit_text_rect, border_radius = 30)
        screen.blit(exit_text, (exit_text_rect.x + 15, exit_text_rect.y + 2))
    else:    
        pygame.draw.rect(screen, (87, 46, 17), exit_text_rect, border_radius = 30)
        screen.blit(exit_text, (exit_text_rect.x + 15, exit_text_rect.y + 2))
    if display_cookies and jar is not None:
        if jar.size == 0:
            empty_cookies_text = font.render("No cookies in the jar!", True, (255, 0, 0))
            screen.blit(empty_cookies_text, (320, 540))
            pygame.display.update()
            pygame.time.delay(1500)
            display_cookies = False
        else:
            for i in range(jar.size):
                if i % 2 == 0:
                    screen.blit(cookie_resized_surface, (cookie_width + right_offset, 543))
                    right_offset += 43
                else:
                    screen.blit(cookie_resized_surface, (cookie_width - left_offset, 543))
                    left_offset += 43
    else:
        pygame.display.update()
    
    


def display_eat_surface() -> None:
    screen.blit(eat_surface, (0, -30))
    screen.blit(back_arrow_surface_resized, back_arrow_rect)
    if eat_text_active:
        color = (133, 98, 50)
    else:
        color = (90, 44, 4)
    pygame.draw.rect(screen, color, eat_text_box, 6, border_radius = 8)
    eat_ip_surface = font_larger.render(eat_ip, True, (82, 43, 5))
    screen.blit(eat_ip_surface, (eat_text_box.x + 200, eat_text_box.y + 22))



def display_deposit_screen() -> None:
    screen.blit(deposit_surface, (0, 0))
    screen.blit(back_arrow_surface_resized, back_arrow_rect)
    if deposit_text_active:
        color = (133, 98, 50)
    else:
        color = (90, 44, 4)
    pygame.draw.rect(screen, color, deposit_text_box, 6, border_radius = 8)
    deposit_ip_surface = font_larger.render(deposit_ip, True, (82, 43, 5))
    screen.blit(deposit_ip_surface, (deposit_text_box.x + 200 , eat_text_box.y - 70))
    

def main():
# Game Loop
    global screen_state
    global eat_text_hover
    global deposit_text_hover
    global display_text_hover
    global exit_text_hover
    global jar_text_active
    global eat_text_active
    global deposit_text_active
    global display_cookies
    global jar
    global jar_size_ip
    global eat_ip
    global deposit_ip
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and screen_state == "home":
                screen_state = "jar_size"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jar_size_text_box.collidepoint(event.pos):
                    jar_text_active = True
                elif eat_text_box.collidepoint(event.pos):
                    eat_text_active = True
                elif deposit_text_box.collidepoint(event.pos):
                    deposit_text_active = True
                elif back_arrow_rect.collidepoint(event.pos):
                    screen_state = "action"
                else:
                    eat_text_active = False
                    jar_text_active = False
                    deposit_text_active = False
            if event.type == pygame.KEYDOWN:
                if jar_text_active and screen_state == "jar_size":
                    if event.key == pygame.K_BACKSPACE:
                        jar_size_ip = jar_size_ip[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            capacity = int(jar_size_ip)
                            global jar
                            jar = Jar(capacity)
                        except ValueError:
                            error_text = font.render("Please enter an integer!", True, (255, 0, 0))
                            screen.blit(error_text, (310, 25))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            jar_size_ip = ''
                            continue
                        screen_state = "action"
                        pygame.display.update()
                        jar_text_active = False
                    else:
                        jar_size_ip += event.unicode
                elif eat_text_active and screen_state == "eat":
                    if event.key == pygame.K_BACKSPACE:
                        eat_ip = eat_ip[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            cookies = eat_ip
                            jar.withdraw(cookies)
                        except ValueError as e:
                            error_text = font.render(str(e), True , (255, 0, 0))
                            screen.blit(error_text, (80, 540))
                            pygame.display.update()
                            pygame.time.delay(1500)
                            eat_ip = ''
                            continue
                        successful_text = font.render(f'You ate {cookies} cookies!', True, (0, 238, 0))
                        screen.blit(successful_text, (140, 540))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        screen_state = "action"
                        eat_ip = ''
                    else:
                        eat_ip += event.unicode
                elif deposit_text_active and screen_state == "deposit":
                    if event.key == pygame.K_BACKSPACE:
                        deposit_ip = deposit_ip[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            cookies = deposit_ip
                            jar.deposit(cookies)
                        except ValueError as e:
                            error_text = font.render(str(e), True , (255, 0, 0))
                            screen.blit(error_text, (34, 480))
                            pygame.display.update()
                            pygame.time.delay(1500)
                            deposit_ip = ''
                            continue
                        successful_text = font.render(f'You deposited {cookies} cookies!', True, (0, 238, 0))
                        screen.blit(successful_text, (140, 472))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        screen_state = "action"
                        deposit_ip = ''
                    else:
                        deposit_ip += event.unicode
            if event.type == pygame.MOUSEMOTION and screen_state == "action":
                if eat_text_rect.collidepoint(event.pos):
                    eat_text_hover = True
                elif deposit_text_rect.collidepoint(event.pos):
                    deposit_text_hover = True
                elif display_text_rect.collidepoint(event.pos):
                    display_text_hover = True
                elif exit_text_rect.collidepoint(event.pos):
                    exit_text_hover = True
                else:
                    eat_text_hover = False
                    deposit_text_hover = False
                    display_text_hover = False
                    exit_text_hover = False
            if event.type == pygame.MOUSEBUTTONDOWN and screen_state == "action":
                if eat_text_rect.collidepoint(event.pos):
                    screen_state = "eat"
                    display_cookies = False
                elif deposit_text_rect.collidepoint(event.pos):
                    screen_state = "deposit"
                    display_cookies = False
                elif display_text_rect.collidepoint(event.pos):
                    if not display_cookies:
                        display_cookies = True
                    else:
                        display_cookies = False
                elif exit_text_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        if screen_state == "home":
            display_home_screen()
        elif screen_state == "jar_size":
            jar_size_screen()
        elif screen_state == "action":
            display_action_screen(jar)
        elif screen_state == "eat":
            display_eat_surface()
        elif screen_state == "deposit":
            display_deposit_screen()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
