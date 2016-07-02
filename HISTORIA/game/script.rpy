# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
# define e = Character('Eileen', color="#c8ffc8")
define d = Character('Detective', color="#ff9933")
define t = Character('testigo', color="#cc0033")
define a = Character('Art', color="#c8ffc8")
define b = Character('Burt', color="#c8ffc8")
define c = Character('Carl', color="#c8ffc8")

image bg inte = "sala_interrogatorio.jpg"
image bg inicio = "city.png"
image bg muerte = "3.png"

image dete = "Peensando_opt.png"
image dete1 = "Hablandoo.png"
image dete2 = "Enojaado.png"
image tes = "2009.png"
image bart = "hablando3.png"
image art = "Taka.png"
image carl = "parada.png"

# The game starts here.
# - El juego comienza aquí.
label start:
    scene bg inicio
    show dete at left  
    d "Debemos resolver este misterioso crimen de una joven asesinada comencemos a interrogar a los sospechosos y testigos de inmediato"
    d "de este crimen"
    d "A quien interogaremos?"
    hide dete

    menu:
        "Testigo y sospechosos":
        
            scene bg inte
            show dete1 at right
            show tes at left
            d "Que me puede decir hacerca del asesinato ocurrido"
            hide inte

            with pixellate
            scene bg muerte
            show tes at left
            t "mis recueros son confusos lo que recuerdo es que  "
            t "Art era amigo de la victima "
            t "Burt era enemigo de la victima "
            t "carl conocia a la victima "
            with pixellate

            hide muerte
            hide dete1

            scene bg inte
            show dete at right
            hide tes
            d "Este va a ser un caso muy complicado sequire obteniendo mas informacion"
            hide dete
            show dete1 at right
            d "Lo siguiente es interrogar a los sospechosos de este asesinato"
            d "que pase el sospechoso"
            show bart at left
            b "En que lo puedo ayudar detective"
            d "digame su testimonio hacerca del acesinato"
            
    python:
           nuevo = []
    menu:
        "No estaba en el pueblo":
            python:
                 nuevo.append("no estaba en el pueblo")
            
            b "Eso es todo lo que tengo que decir"
            b "me retiro detective que pase un buen día detective" 
            d "que pase el siquiente sospechoso el SR. Art"
            scene bg inte
            show dete at right
            show art at left 
            a "En que lo puedo ayudar detective"      
            d "Digame todo lo que sabe hacerca de este asesinato "
            d "que vinculo tenia con la victima" 
        

        "No conocia a la victimas":
            python:
                 nuevo.append("no conocia a la victima")
            b "Eso es todo lo que tengo que decir"
            b "me retiro detective que pase un buen día"            
            d "se puede retirar SR. burt" 
                 
            d "que pase el siquiente sospechoso el SR. Art" 

            scene bg inte
            show dete at right
            show art at left 
            a "En que lo puedo ayudar detective"      
            d "Digame todo lo que sabe hacerca de este asesinato "
            d "que vinculo" 
    #python:
           #nuevo1 = []
    menu:
        "No estaba en el pueblo":
            python:
                 nuevo.append("no estaba en el pueblo")
            
            a "Eso es todo lo que tengo que decir"
            a "me retiro detective que pase un buen día detective" 

        "no conicia a la victima":
            python:
                 nuevo.append("no conocia a la victima")
            
            a "Eso es todo lo que tengo que decir"
            a "me retiro detective que pase un buen día detective"
            a "Eso es todo lo que tengo que decir"

    scene bg inte
    show dete at right
    show carl at left 
    c "En que lo puedo ayudar detective"      
    d "Digame todo lo que sabe hacerca de este asesinato "
    d "que vinculo con la victima " 
    
          
    menu:
        "No estaba en el pueblo":
            python:
                 nuevo.append("no estaba en el pueblo")
            
            c "Eso es todo lo que tengo que decir"
            c "me retiro detective que pase un buen día detective" 

        "no conicia a la victima":
            python:
                 nuevo.append("no conocia a la victima")
            
            c "Eso es todo lo que tengo que decir"
            c "me retiro detective que pase un buen día detective"
            c "Eso es todo lo que tengo que decir"

    scene bg inte
    show dete:
     ypos 50 xpos 60
    d "hay ciertas discrepacias en las declaraciones"
    d "analisando toda la informacion e llegado a una conclucio"
    hide dete

    show dete2:
     ypos 0 xpos 80
    d "Es:.......42"
    d  "________´$$$$`_________ "

    python:
            lista1 =list(nuevo)
            asesino1= open('/home/juan/Escritorio/Programacion/HISTORIA/game/asesino.pl','w')
            for x in lista1:
                asesino1.write(x)
                       
            
   # return               
