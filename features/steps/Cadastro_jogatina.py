
from behave import given, then, when
from selenium.webdriver.common.by import By


def before_feature(context, feature):
    context.execute_steps()

@given(u'que acesso o site Jogatina')
def step_impl(context):
    context.driver.get('https://www.jogatina.com/')
    print('Passo 1 - Acessou o site Jogatina')

@when(u'clico no botão cadastre-se')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, " a.header__logo-jogatina").text == 'Jogatina.com'
    context.driver.execute_script("window.scrollTo(0,300)")
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Buraco'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Dominó'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Bingo'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Tranca'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Truco'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Paciência'
    assert context.driver.find_element(By.CSS_SELECTOR, 'h3.titulo-jogo').text == 'Poker'
    print()

@when(u'preencho o campo "email" e "senha"')
def step_impl(context):
    print()


@when(u'clico no botão criar conta')
def step_impl(context):
    print()

@then(u'sou direcionado para a página de seleção dos jogos')
def step_impl(context):
    print()


@when(u'clico o incone do perfil e seleciono Ver meu perfil')
def step_impl(context):
    print()


@then(u'sou direcionado para página do meu perfil')
def step_impl(context):
    print()


@when(u'clico em editar informações')
def step_impl(context):
    print()


@then(u'sou direcionado para a página de gerenciamento do meu perfil')
def step_impl(context):
    print()


@when(u'clico em botão editar do campo perfil')
def step_impl(context):
    print()


@when(u'preencho os campos cidade , estado , País , sexo e data de nascimento')
def step_impl(context):
    print()


@when(u'clico no botão alterar perfil')
def step_impl(context):
    print()


@then(u'retorno para a página de gerenciamento de perfil')
def step_impl(context):
    print()
