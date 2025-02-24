Feature: Freio do Motor
  Como um operador do motor
  Eu quero ativar o freio do motor
  Para que o motor pare imediatamente em caso de emergência

  @alta_prioridade
  Scenario: Ativar o freio do motor
    Given O motor está girando
    When O pino de freio é ativado
    Then O motor deve parar imediatamente

  @media_prioridade
  Scenario: Desativar o freio do motor
    Given O freio do motor está ativado
    When O pino de freio é desativado
    Then O motor deve permanecer parado até que o potenciômetro seja ajustado