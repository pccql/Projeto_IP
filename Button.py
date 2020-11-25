def button(size_text, message, center_message, colour_message, colour_button, surface,
           new_colour_msg=None, new_colour_button=None, font=None):
    import pygame

    if new_colour_msg == None:
        new_colour_msg = colour_message
    if new_colour_button == None:
        new_colour_button = colour_button

    font = pygame.font.Font(font, size_text)
    text = font.render(message, True, colour_message)
    xButaoInicio = center_message[0] - (text.get_width() // 2) - 20
    yButaoInicio = center_message[1] - (text.get_height() // 2) - 20
    xButaoFinal = text.get_width() + 40
    yButaoFinal = text.get_height() + 40
    pygame.draw.rect(surface, colour_button, (xButaoInicio, yButaoInicio, xButaoFinal, yButaoFinal))
    surface.blit(text, text.get_rect(center=center_message))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if xButaoInicio < mouse[0] < xButaoInicio + xButaoFinal and yButaoInicio < mouse[1] < yButaoFinal + yButaoInicio:
        pygame.draw.rect(surface, new_colour_button, (xButaoInicio, yButaoInicio, xButaoFinal, yButaoFinal))
        text = font.render(message, True, new_colour_msg)
        surface.blit(text, text.get_rect(center=center_message))
        if click[0] == 1:
            return True