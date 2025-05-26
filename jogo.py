import time
import random
import sys

inimigos = ["João", "Abacaxi Feroz", "Cuscuz Salgado"]
sobreinimigos = {"João" : {"olhar de reprovação" : 10,
                           "nota baixa" : 15,
                           "reprovado por falta" : 20},
                 "Abacaxi Feroz" : {"espinhos venenosos" : 10,
                           "coroa do arrependimento" : 15,
                           "ataque do rei" : 20},
                  "Cuscuz Salgado" : {"Tá fervendo" : 10,
                           "Faltou manteiga" : 15,
                           "Desmancho" : 20}}
inimigos2 = {"Pato": {"bicada" : 30,
             "patada": 25,
             "bicada e patada" : 50},
         "Leão": {"mordida": 30, 
                      "investida": 35,
                      "rugido": 55},
                      "shrek": {"urro": 30, 
                      "voadora do pantano": 35,
                      """BURRO!
                      Nesse ataque shrek invoca o burro e a dragoa para te atacarem
                                   ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\ -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
                      """"""""""": 55}}
fases = [ {"nome" : "Pato", "hp" :  200, "ataques": inimigos2["Pato"], "foto":  """
    __
_  ( o)>
\ <_. )
 `---'   
"""},
         {"nome" : "Leão", "hp" :  300, "ataques": inimigos2["Leão"], "foto" : """ .~ ~ ~.
 (  o,,,o  )
(   ). .(   )
 \  { v }  /
   ~ `v' ~"""},
         {"nome" : "Shrek", "hp" :  350, "ataques": inimigos2["shrek"], "foto": """⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉"""}]
def Text_animado(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(delay)  
    print()
def menu():
    Text_animado("""Boas vindas ao \n╔══════════════════════════╗\n
║    SALVE-SE QUEM PUDER   ║ \n
╚══════════════════════════╝""", delay=0.07)
    time.sleep(1)
    print("Você deseja jogar?")
    print("1-Sim")
    print("2-Não")
    while True:
        opcao= int(input("Escolha sua opção: "))
        if opcao == 1:
            menu2()
            break
        elif opcao == 2:
            print("fechando jogo...")
            break
        else:
            print("Opção inválida.")
            break
def menu2():
     print("Obrigada por querer jogar! \n Qual modo de jogo você prefere?")
     print("1 - História")
     print("2 - Combate por fases")
     print("3 - Combate unico")
     while True:
        opcao2 = int(input("Escolha sua opção: "))
        if opcao2 == 1:
            história()
            break
        elif opcao2 == 3:
            combate()
            break
        elif opcao2 == 2:
             combate2()
             break
        else:
            print("Opção inválida.")
            break
def história():
    print("No início da criação do mundo, temos apenas uma salvação para todos.")
    print("A pessoa mais valente de todo o Reino deverá aniquilar os terríveis vilões que assombram todas as planícies e montanhas.")
    print("Os povos dependem da coragem dessa grandiosa pessoa para sobreviver!!!")
    print("E você é essa pessoa!!! Que comece a luta!!!")
    combate2()
def combate():
    oponente = random.choice(inimigos)
    hp_player = 100
    inimigohp = 100
    print("Ótima escolha!")
    time.sleep(1)
    print("Iniciando combate...")
    time.sleep(1)
    print("Escolhendo oponente...")
    time.sleep(2)
    print(f"Oponente escolhido: {oponente}")
    Text_animado("""============================
||   COMBATE INICIADO!   ||
============================""", delay=0.07)
    monstro1()
    time.sleep(2)
    while hp_player > 0 and inimigohp > 0:
     hp_player, inimigohp = atq(hp_player, inimigohp, oponente)
     if inimigohp <= 0:
        print(f"{oponente} foi derrotado!")
        mensagem_vitoria()
        break
     ataqueslist = sobreinimigos[oponente]
     ataque = random.choice(list(ataqueslist.keys()))
     dano = ataqueslist[ataque]
     print(f"\n Turno de {oponente}")
     time.sleep(2)
     print(f"{oponente} usou {ataque} e causou {dano} de dano")
     hp_player -= dano
     print(f"Agora você tem {hp_player} de vida")
     time.sleep(1)
     if hp_player <= 0:
        mensagem_derrota()
        break
        
     
     

def atq(hp_player, inimigohp, oponente):
   print("Seu turno")
   time.sleep(0.7)
   print("1 - Poção de cura (cura 15 de vida)")
   time.sleep(0.7)
   print("2 - Café de ontem (15 de dano)")
   time.sleep(0.7)
   print("3 - Miojo queimado (20 de dano)")
   opc = int(input("Escolha seu ataque: "))
   if opc == 1:
    hp_player += 15
    print(f"Você usou poção de cura e agora tem {hp_player} de vida")
   elif opc == 2:
    dano = 15
    inimigohp -= dano
    print(f"Você usou Cafe de ontem e causou {dano} de dano")
   elif opc == 3:
    dano = 20
    inimigohp -= dano
    print(f"Você usou miojo queimado e causou {dano} de dano \n {oponente} agora tem {inimigohp} de vida")
   else:
    print("Opção inválida. \n Você perdeu seu turno.") 
   return hp_player, inimigohp

def atq2(hp_player, inimigohp, oponente):
   print("Seu turno")
   time.sleep(0.7)
   print("1 - Poção de cura (cura 50 de vida)")
   time.sleep(0.7)
   print("2 - Café de ontem (40 de dano)")
   time.sleep(0.7)
   print("3 - Miojo queimado (50 de dano)")
   opc = int(input("Escolha seu ataque: "))
   if opc == 1:
    hp_player += 50
    print(f"Você usou poção de cura e agora tem {hp_player} de vida")
   elif opc == 2:
    dano = 40
    inimigohp -= dano
    print(f"Você usou Cafe de ontem e causou {dano} de dano")
   elif opc == 3:
    dano = 50
    inimigohp -= dano
    print(f"Você usou miojo queimado e causou {dano} de dano \n {oponente} agora tem {inimigohp} de vida")
   else:
    print("Opção inválida. \n Você perdeu seu turno.") 
   return hp_player, inimigohp

def combate2():
   print("Prepare-se! Você enfrentará uma sequência de inimigos agora. Será que você é capaz de derrotar todos eles?")
   time.sleep(2)
   for fase in fases:
     Text_animado("""============================
||   COMBATE INICIADO!   ||
============================""", delay=0.07)
     hp_player = 100
     hp_player += 250
     nome = fase["nome"]
     hp = fase["hp"]
     atqs = fase["ataques"]
     foto = fase["foto"]
     print(f"Seu oponente: {nome} com {hp} de vida")
     print(foto)
     while hp_player > 0 and hp > 0:
       hp_player, hp = atq2(hp_player,hp, nome)
       if hp <= 0:
        print(f"{nome} foi derrotado!")
        mensagem_vitoria()
        break
       ataque = random.choice(list(atqs.keys()))
       dano = atqs[ataque]
       print(f"\n Turno de {nome}")
       time.sleep(2)
       print(f"{nome} usou {ataque} e causou {dano} de dano")
       hp_player -= dano
       print(f"Agora você tem {hp_player} de vida")
       time.sleep(1)
       if hp_player <= 0:
        mensagem_derrota()
        break
     
fotos = {  "foto":  """
    __
_( o)>
\ <_. )
 `---'   
""", "foto" : """ .~ ~ ~.
 (  o,,,o  )
(   ). .(   )
 \  { v }  /
   ~ `v' ~"""}    

      
def mensagem_vitoria():
    Text_animado("""╔════════════════════════════════╗
║    ★ PARABÉNS, VOCÊ VENCEU! ★  ║
╚════════════════════════════════╝""", delay=0.07)

def mensagem_derrota():
    Text_animado("""
    ╔════════════════════════════════╗
║    (ಥ﹏ಥ)  VOCÊ FOI DERROTADO... ║
╚════════════════════════════════╝
    """, delay=0.7)
def monstro1():
   print("""
   （ •_•)    ~
    (  :  ) ▄︻̷̿┻̿═━一  monstro sombrio se arrasta!
    (_  _)""")
menu()
