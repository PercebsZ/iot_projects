# Utilizando a plataforma Arduino Nano para Tocar Notas em Frequências Especificadas


Este projeto tem o propósito de ajudar o iniciante a dar os primeiros passos no uso de funções principais das bibliotecas IRremote, Tone e LiquidCrystal_I2C. 
Em síntese, o projeto foi desenvolvido na plataforma embacada Arduino Nano dado ao fato de que possui compatibilidade com o protocolo I2C para facilitar a 
comunicação com o LCD Display 16x2. 
Componentes utilizados para desenvolver esse projeto:
1. Arduino Nano;
2. Sensor Receptor de IR;
3. Buzzer;
4. LCD Display 16x2;
5. Módulo adptador para LCD Display 16x2;
6. Protoboard;
7. Jumpers;
8. Controle Remoto IR Universal;

## O Funcionamento do projeto tem o objetivo de atender seguinte problema: 

Utilize a plataforma Arduino para gerar os tons de frequência descritos a seguir em uma buzina.
A duração de cada tom deve ser de 300ms. Um teclado matricial ou teclas individuais devem ser
utilizadas para seleção do tom a ser gerado na buzina. Os tons podem ser baseados em onda quadrada
Dó - 264 Hz; Re - 297 Hz; Mi - 330 Hz; Fá - 352 Hz; Sol - 396 Hz; Lá - 440 Hz; Si - 495 Hz; dó -
528

## Considerações Finais:

As bibliotecas IRremote e Tone utilizam o mesmo timer para os Serviços de Interrupção de Rotina. Por isso, é necessário ir na Biblioteca IRremote e procurar
pelo arquivo IRremoteBoardDefs.h e procurar a seguinte sessão:

/*********************
 * ARDUINO Boards
 *********************/
// Arduino Duemilanove, Diecimila, LilyPad, Mini, Fio, Nano, etc
// ATmega48, ATmega88, ATmega168, ATmega328
#elif defined(__AVR_ATmega328P__) || defined(__AVR_ATmega168__) // old default clause
//#  if !defined(IR_USE_TIMER1) && !defined(IR_USE_TIMER2)
//#define IR_USE_TIMER1   // tx = pin 9
//#define IR_USE_TIMER2     // tx = pin 3
//#  endif

Conforme está especificado acima, é necessário alterar o IR_USE_TIME de IR_USE_TIME2 para IR_USE_TIME1 
