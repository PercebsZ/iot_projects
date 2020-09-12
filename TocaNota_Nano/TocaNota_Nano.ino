#include <IRremote.h> //Biblioteca com funções para trabalhar com o receptor de sinal infravermelho.
#include <LiquidCrystal_I2C.h>


//Set the LCD number of columns and rows.
int LCDColumns = 16;
int LCDRows = 2;

//Set LCD Adress, number of columns and rows. In order
//to get the LCD Adress, you should look for a I2C Scanner sketch.
LiquidCrystal_I2C lcd(0x27, LCDColumns, LCDRows);


const int RECV_PIN = 8 ; //Pino para leitura do sinal infravermelho
IRrecv irrecv(RECV_PIN); //Instanciando o objeto RECV_PIN a partir da função irrecv da classe IRcev;
decode_results results;


void setup() 
{
  
  pinMode(4, OUTPUT);
  Serial.begin(115200); //Inicializa as ações com a porta serial;
  irrecv.enableIRIn();
  irrecv.blink13(true); //Faz com o que o LED BUILT IN do Hardware pisque quando houver acontecer uma interrupção de rotina;  

  lcd.begin(); //Inicializa o LCD Display
  lcd.backlight(); // Turn on backlight
  
}

void loop()
{
  if (irrecv.decode(&results))
  {
//    DutyCicle = 60;
//Fazer uma função pra não ficar tanta coisa no loop;
    Serial.println(results.value, HEX);
    switch (results.value)
    {
      case 0xFF30CF: //Caso Botão Número 1
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: Do");
        lcd.setCursor(0,1);
        lcd.print("Freq: 264 Hz");
        tone(4, 264,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF18E7: //Caso Botão Número 2
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: Re");
        lcd.setCursor(0,1);
        lcd.print("Freq: 297 Hz");
        tone(4, 297,300); //Escreve a frequência Re ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF7A85: //Caso Botão Número 3
      {
      lcd.setCursor(0,0);
        lcd.print("Nota: Mi");
        lcd.setCursor(0,1);
        lcd.print("Freq: 330 Hz");
        tone(4, 330,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF10EF: //Caso Botão Número 4
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: Fa");
        lcd.setCursor(0,1);
        lcd.print("Freq: 352 Hz");
        tone(4, 352,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF38C7: //Caso Botão Número 5
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: Sol");
        lcd.setCursor(0,1);
        lcd.print("Freq: 396 Hz");
        tone(4, 396,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF5AA5: //Caso Botão Número 6
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: La");
        lcd.setCursor(0,1);
        lcd.print("Freq: 440 Hz");
        tone(4, 440,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF42BD: //Caso Botão Número 7
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: Si");
        lcd.setCursor(0,1);
        lcd.print("Freq: 495 Hz");
        tone(4, 495,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      case 0xFF4AB5: //Caso Botão Número 8
      {
        lcd.setCursor(0,0);
        lcd.print("Nota: do");
        lcd.setCursor(0,1);
        lcd.print("Freq: 528 Hz");
        tone(4, 528,300); //Escreve a frequência Dó ao canal definido.
        delay(500);
        lcd.clear();
        break; // Saí do switch;
      }
      default:
      {
        lcd.setCursor(0,0);
        lcd.print("Fail");
        delay(500);
        lcd.clear();
      }
    }
    irrecv.resume(); // Método da classe irrecv para habilitar novamente o repector IR.
  }
}
