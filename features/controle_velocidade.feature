Feature: Controle de Velocidade do Motor
  Como um operador do motor
  Eu quero ajustar a velocidade do motor usando um potenciômetro
  Para que eu possa controlar a rotação do motor conforme necessário

  @alta_prioridade
  Scenario: Ajustar a velocidade do motor com o potenciômetro
    Given O motor está desligado
    When O potenciômetro é ajustado para um valor diferente de zero
    Then O motor deve girar na velocidade correspondente ao valor do potenciômetro

  @media_prioridade
  Scenario: Parar o motor quando o potenciômetro está em zero
    Given O motor está girando
    When O potenciômetro é ajustado para zero
    Then O motor deve parar