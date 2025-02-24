from behave import given, when, then

# Definindo as constantes LOW e HIGH
LOW = 0
HIGH = 1

# Variáveis globais para simular o estado do sistema
estado_mosfet = [LOW, LOW, LOW, LOW, LOW, LOW]  # Estado dos mosfets (A1, A2, B1, B2, C1, C2)
sensores_hall = [LOW, LOW, LOW]  # Estado dos sensores hall (A, B, C)
valor_potenciometro = 0  # Valor do potenciômetro
freio_ativado = False  # Estado do freio

# Função para simular a definição do estado dos MOSFETs
def definir_estado_mosfet(a1, a2, b1, b2, c1, c2):
    global estado_mosfet
    estado_mosfet = [a1, a2, b1, b2, c1, c2]

# Função para simular a leitura dos sensores Hall
def ler_sensores_hall():
    return sensores_hall

# Função para simular a leitura do potenciômetro
def ler_potenciometro():
    return valor_potenciometro

# Função para simular a ativação do freio
def ativar_freio():
    global freio_ativado
    freio_ativado = True
    definir_estado_mosfet(LOW, LOW, LOW, LOW, LOW, LOW)

# Função para simular a desativação do freio
def desativar_freio():
    global freio_ativado
    freio_ativado = False

# Função para simular a comutação do motor
def comutaMotor(hallA, hallB, hallC):
    if not freio_ativado:
        if hallA == HIGH and hallB == LOW and hallC == LOW:
            definir_estado_mosfet(HIGH, LOW, LOW, HIGH, LOW, LOW)  # A1, B2 ativos
        elif hallA == HIGH and hallB == LOW and hallC == HIGH:
            definir_estado_mosfet(HIGH, LOW, LOW, LOW, LOW, HIGH)  # A1, C2 ativos
        elif hallA == LOW and hallB == HIGH and hallC == HIGH:
            definir_estado_mosfet(LOW, LOW, HIGH, LOW, LOW, HIGH)  # B1, C2 ativos
        elif hallA == LOW and hallB == HIGH and hallC == LOW:
            definir_estado_mosfet(LOW, HIGH, HIGH, LOW, LOW, LOW)  # B1, A2 ativos
        elif hallA == LOW and hallB == LOW and hallC == HIGH:
            definir_estado_mosfet(LOW, HIGH, LOW, LOW, HIGH, LOW)  # C1, A2 ativos
        elif hallA == LOW and hallB == LOW and hallC == LOW:
            definir_estado_mosfet(LOW, LOW, LOW, HIGH, HIGH, LOW)  # C1, B2 ativos

# Função para simular a parada do motor
def pararMotor():
    definir_estado_mosfet(LOW, LOW, LOW, LOW, LOW, LOW)

# Função para mapear valores 
def map_value(value, from_min, from_max, to_min, to_max):
    return (value - from_min) * (to_max - to_min) // (from_max - from_min) + to_min

# Steps para a feature "Controle de Direção do Motor"
@given('O motor está desligado')
def step_motor_desligado(context):
    definir_estado_mosfet(LOW, LOW, LOW, LOW, LOW, LOW)

@when('O sensor Hall A está ativo e os sensores B e C estão inativos')
def step_hall_a_ativo(context):
    global sensores_hall
    sensores_hall = [HIGH, LOW, LOW]
    comutaMotor(*sensores_hall)

@when('O sensor Hall A está ativo, o sensor Hall C está ativo e o sensor B está inativo')
def step_hall_a_c_ativos(context):
    global sensores_hall
    sensores_hall = [HIGH, LOW, HIGH]
    comutaMotor(*sensores_hall)

@then('O motor deve girar no sentido horário')
def step_motor_gira_horario(context):
    if sensores_hall == [HIGH, LOW, LOW]:  # A ativo, B e C inativos
        assert estado_mosfet == [HIGH, LOW, LOW, HIGH, LOW, LOW], "Motor não está girando no sentido horário"
    elif sensores_hall == [HIGH, LOW, HIGH]:  # A e C ativos, B inativo
        assert estado_mosfet == [HIGH, LOW, LOW, LOW, LOW, HIGH], "Motor não está girando no sentido horário"

# Steps para a feature "Controle de Velocidade do Motor"
@when('O potenciômetro é ajustado para um valor diferente de zero')
def step_potenciometro_ajustado(context):
    global valor_potenciometro
    valor_potenciometro = 512  # Valor médio do potenciômetro

@then('O motor deve girar na velocidade correspondente ao valor do potenciômetro')
def step_motor_gira_velocidade_correspondente(context):
    tempo_comutacao = map_value(valor_potenciometro, 0, 1023, 5000, 500)
    assert 500 <= tempo_comutacao <= 5000, "Tempo de comutação fora do esperado"

# Steps para a feature "Freio do Motor"
@when('O pino de freio é ativado')
def step_freio_ativado(context):
    ativar_freio()

@then('O motor deve parar imediatamente')
def step_motor_para_imediatamente(context):
    assert estado_mosfet == [LOW, LOW, LOW, LOW, LOW, LOW], "Motor não parou imediatamente"

@given('O freio do motor está ativado')
def step_freio_ja_ativado(context):
    ativar_freio()

@when('O pino de freio é desativado')
def step_freio_desativado(context):
    desativar_freio()

@then('O motor deve permanecer parado até que o potenciômetro seja ajustado')
def step_motor_permance_parado(context):
    assert estado_mosfet == [LOW, LOW, LOW, LOW, LOW, LOW], "Motor não permaneceu parado"

# Steps para a feature "Parada do Motor"
@given('O motor está girando')
def step_motor_girando(context):
    global valor_potenciometro
    valor_potenciometro = 512  # Define um valor para o potenciômetro para simular o motor girando

@when('O potenciômetro é ajustado para zero')
def step_potenciometro_zero(context):
    global valor_potenciometro
    valor_potenciometro = 0
    pararMotor()

@then('O motor deve parar')
def step_motor_para(context):
    assert estado_mosfet == [LOW, LOW, LOW, LOW, LOW, LOW], "Motor não parou"