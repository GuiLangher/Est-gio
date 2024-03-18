"""4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta: Há três interruptores, interruptor0, interruptor1, interruptor2, e tres salas, sala0, sala1 e sala2
ligo o interrupor0 espero um pouco, desligo o interruptor0 e ligo o interruptor1
vou a sala0, se a lampada estiver acessa, interruputor1 liga sala0
             se a lampada estiver quente e apagada, interruptor0 liga sala0
             se a lampada estiver apagada e fria, interruptor2 liga sala0
Após saber qual interrupotor liga a sala0, vou até a sala1 e testo os outros dois interruptores
Por exemplo: interrupor1 liga sala0. Ligo o interrupor0 e vou a sala1, 
                                     se a lampada estiver acessa, interruptor0 liga sala1 e o interruptor2 liga sala2
                                     se a lampada esriver apagada, interruptor2 liga sala1 e o interruptor0 liga sala2

"""
