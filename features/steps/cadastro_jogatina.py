import time

from behave import given, then, when
from selenium.webdriver.common.by import By



def before_feature(context, feature):
    context.execute_steps(
        context.driver.implicitly_wait(30)
    )

@given(u'que acesso o site Jogatina')
def step_impl(context):
    #abrindo o site
    context.driver.get('https://www.jogatina.com/')
    print('Passo 1 - Acessou o site Jogatina')
    #time.sleep(5)


@when(u'clico no botão cadastre-se')
def step_impl(context):
    # rolagem e validação dos 7 tipos de jogas na página inicial
    assert context.driver.find_element(By.CSS_SELECTOR, " a.header__logo-jogatina").text == 'Jogatina.com'
    context.driver.execute_script("window.scrollTo(0,450)")
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'li.box-jogo.buraco-aberto.box-esquerda:nth-child(1) a:nth-child(1) > h3.titulo-jogo').text == 'Buraco'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'li.box-jogo.domino:nth-child(2) a:nth-child(1) > h3.titulo-jogo').text == 'Dominó'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       ' li.box-jogo.bingo:nth-child(3) a:nth-child(1) > h3.titulo-jogo').text == 'Bingo'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'li.box-jogo.tranca:nth-child(4) a:nth-child(1) > h3.titulo-jogo').text == 'Tranca'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       ' li.box-jogo.truco-paulista.box-esquerda:nth-child(5) a:nth-child(1) > h3.titulo-jogo').text == 'Truco'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'li.box-jogo.paciencia:nth-child(6) > h3.titulo-jogo:nth-child(2)').text == 'Paciência'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'li.box-jogo.poker:nth-child(7) a:nth-child(1) > h3.titulo-jogo').text == 'Poker'
    context.driver.execute_script("window.scrollTo(0,-450)")
    #time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-laranja.js-btn-cadastro').click()
    #time.sleep(3)


@when(u'preencho o campo "{email}" e "{senha}"')
def step_impl(context, email, senha):
    #cadastro de cliente inserindo email e senha  que podem ser trocados na feature de cadastro
    context.driver.find_element(By.ID, 'emailIn').send_keys(email)
    context.driver.find_element(By.ID, 'password-field').send_keys(senha)
    #time.sleep(3)


@when(u'clico no botão criar conta')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-laranja.js-event-track').click()


@then(u'sou direcionado para a página de seleção dos jogos confirmando "{usuario}"')
def step_impl(context, usuario):
    #Faz a validação de uma imagem esta visével e valida o usuário
    context.driver.execute_script("window.scrollTo(0,40)")
    context.driver.find_element(By.CSS_SELECTOR,
                                'div.footer__logo-reclame-aqui.fright > img:nth-child(1)').is_displayed()
    context.driver.execute_script("window.scrollTo(0,-40)")
    #time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, 'a.header__nav-profile-wrapper > i.caret').click()
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.header__subnav-info-email').text == usuario
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Sair')]").click()
    #time.sleep(7)


