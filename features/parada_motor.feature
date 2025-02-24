Feature: Parada do Motor
  Como um operador do motor
  Eu quero parar o motor manualmente
  Para que o motor não continue girando quando não for necessário

  @alta_prioridade
  Scenario: Parar o motor manualmente
    Given O motor está girando
    When O potenciômetro é ajustado para zero
    Then O motor deve parar