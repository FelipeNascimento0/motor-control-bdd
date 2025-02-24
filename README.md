
## Features e Cenários

### 1 Controle de Direção do Motor
**Descrição:**  
Como um operador do motor, eu quero controlar a direção do motor com base nos sensores Hall, para que o motor gire no sentido correto.

**Cenários:**
- **Girar o motor no sentido horário (Hall A ativo):**
  - Dado que o motor está desligado.
  - Quando o sensor Hall A está ativo e os sensores B e C estão inativos.
  - Então o motor deve girar no sentido horário.

- **Girar o motor no sentido horário (Hall A e C ativos):**
  - Dado que o motor está desligado.
  - Quando o sensor Hall A está ativo, o sensor Hall C está ativo e o sensor B está inativo.
  - Então o motor deve girar no sentido horário.

### 2 Controle de Velocidade do Motor
**Descrição:**  
Como um operador do motor, eu quero ajustar a velocidade do motor usando um potenciômetro, para que eu possa controlar a rotação do motor conforme necessário.

**Cenários:**
- **Ajustar a velocidade do motor com o potenciômetro:**
  - Dado que o motor está desligado.
  - Quando o potenciômetro é ajustado para um valor diferente de zero.
  - Então o motor deve girar na velocidade correspondente ao valor do potenciômetro.

- **Parar o motor quando o potenciômetro está em zero:**
  - Dado que o motor está girando.
  - Quando o potenciômetro é ajustado para zero.
  - Então o motor deve parar.

### 3 Freio do Motor
**Descrição:**  
Como um operador do motor, eu quero ativar o freio do motor, para que o motor pare imediatamente em caso de emergência.

**Cenários:**
- **Ativar o freio do motor:**
  - Dado que o motor está girando.
  - Quando o pino de freio é ativado.
  - Então o motor deve parar imediatamente.

- **Desativar o freio do motor:**
  - Dado que o freio do motor está ativado.
  - Quando o pino de freio é desativado.
  - Então o motor deve permanecer parado até que o potenciômetro seja ajustado.

### 4 Parada do Motor
**Descrição:**  
Como um operador do motor, eu quero parar o motor manualmente, para que o motor não continue girando quando não for necessário.

**Cenários:**
- **Parar o motor manualmente:**
  - Dado que o motor está girando.
  - Quando o potenciômetro é ajustado para zero.
  - Então o motor deve parar.

