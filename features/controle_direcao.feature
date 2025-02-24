Feature: Controle de Direção do Motor
  Como um operador do motor
  Eu quero controlar a direção do motor com base nos sensores Hall
  Para que o motor gire no sentido correto

  @alta_prioridade
  Scenario: Girar o motor no sentido horário (Hall A ativo)
    Given O motor está desligado
    When O sensor Hall A está ativo e os sensores B e C estão inativos
    Then O motor deve girar no sentido horário

  @alta_prioridade
  Scenario: Girar o motor no sentido horário (Hall A e C ativos)
    Given O motor está desligado
    When O sensor Hall A está ativo, o sensor Hall C está ativo e o sensor B está inativo
    Then O motor deve girar no sentido horário