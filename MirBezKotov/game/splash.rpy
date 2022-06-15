image logo:
    "images/logo.png"
    subpixel True
    xcenter 0.5
    ycenter 0.4 # положение лого по оси хуигрик



label splashscreen:
    $ config.allow_skipping = False # чето не работает, хотя в доки доки именно благодаря этому низя было скипнуть, поэтомому если быстро клацать получится какое то говно, буду думать и разбираться че не так
    pause 2
    show logo with dissolve

    $ renpy.pause(2.1,hard=True) # время перед появлением текста

    show text"{size=40}ПРЕДСТАВЛЯЮТ" with moveinbottom: # там размер шрифта текст блять иди нахуй сам разберешься
        subpixel True
        yalign .8 # положение текста по оси хуигрик
        xalign .5

    $ renpy.pause(2,hard=True) # время когда все скипнется

    hide text with Dissolve(1)
    hide logo with Dissolve(1)

    $ renpy.pause(2,hard=True) # время после скипа говна

    # для того шобы одновременно все пропало надо шобы все было в одной картинке
    # низя одновременно убрать эту залупу
    # hard в pause прописывается шобы скипунть ваще низя было
