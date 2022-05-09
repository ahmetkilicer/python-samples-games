print('''
*******************************************************************************
       __,-----,,,,  ,,,--------,__ 
                _-/|\\/|\\/|\\\|\//\\\//|/|//|\\_ 
               /|\/\//\\\\\\\\\\//////////////\\\\ 
             //|//           \\\///            |\\|\ 
            ///|\/             \/               \|\|\ 
           |/|//                                 |\\|\  
          |/|/                                    \|\|\
          ///;    ,,=====,,,  ~~-~~  ,,,=====,,    ;|\|\
         |/|/   '"          `'     '"          "'   ;|\|
         ||/`;   _--~~~~--__         __--~~~~--_   ;/|\|
         /|||;  :  /       \~~-___-~~/       \  :  ;|\| 
         /\|;    -_\  (o)  / ,'; ;', \  (o)  /_-    ;|| 
         |\|;      ~-____--~'  ; ;  '~--____-~      ;\| 
          ||;            ,`   ;   ;   ',            ;||
        __|\ ;        ,'`    (  _  )    `',        ;/|__ 
    _,-~   \|/;    ,'`        ~~ ~~        `',    ;|\   ~-,_ 
  ,'         ||;  '                           '  ;\|/       `, 
 , _          ; ,         _--~~-~~--_           ;            _',
,-' `;-,        ;        ,; |_| | |_| ;,       ;;        ,-;' `-,
      ; `,      ;       ;_| : `~'~' : |_;       ;      ,' ;
       ;  `,     ;     :  `\/       \/   :     ;     ,'  ;
        ;   `,    ;     :               ;     ;    ,'   ;
         ;    `,_  ;     ;./\_     _/\.;     ;   _,    ;
spb   _-'        ;  ;     ~~--|~|~|--~~     ;   ;       '-_
  _,-'            ;  ;        ~~~~~        ;   ;           `-,_
,~                 ;  \`~--__         __--~/  ;                ~,
                    ;   \   ~~-----~~    /   ;                   
                     ~-_  \  /  |  \   /  _-~                    
                        ~~-\/   |   \/ -~~                       
                       (=)=;==========;=(=)
*******************************************************************************
''')
print("Welcome to Vampire Hunt.")
print("Your mission is to find the Vampire and save the village.")
day = input(
    "Everything is ready, do you wanna go hunt on daylight or night? \nChoose Day or Night\n"
)
if day == "Night" or day == "night" or day == "NIGHT":
    fight = input(
        "Vampires attacked to u, do u wanna fight or run?\nChoose Fight or Run\n"
    )
    if fight == "Fight" or fight == "fight" or fight == "FIGHT":
        print("They were so many, they kill u. Game Over!!!")
    else:
        print(
            "U find some of ur warrior friend, and togetger u kill the vampires and save the village.\nCONGRULATIONS, YOU WIN!!!"
        )
else:
    trap = input(
        "U find a cave, vampires probably hiding here, Do u wanna enter or set a trap?\nChoose Enter or Trap\n"
    )
    if trap == "Enter" or trap == "enter" or trap == "ENTER":
        print("Vampires hunt u down, Game Over!!!")
    else:
        print(
            "Vampires stuck at ur trap and Sunlight kill them, You Win\n CONGRULATIONS!!!"
        )

