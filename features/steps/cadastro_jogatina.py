import time

from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions


def before_feature(context, feature):
    context.execute_steps(
        context.driver.implicitly_wait(30)
    )

@given(u'que acesso o site Jogatina')
def step_impl(context):
    context.driver.get('https://www.jogatina.com/')
    print('Passo 1 - Acessou o site Jogatina')
    time.sleep(5)
@when(u'clico no botão cadastre-se')
def step_impl(context):
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
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-laranja.js-btn-cadastro').click()
    time.sleep(3)
    print()

@when(u'preencho o campo "email" e "senha"')
def step_impl(context):
    context.driver.find_element(By.ID, 'emailIn').send_keys('viniciustester01@tester.com')
    context.driver.find_element(By.ID, 'password-field').send_keys('123456')
    time.sleep(3)
    print()

@when(u'clico no botão criar conta')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-laranja.js-event-track').click()
    print()

@then(u'sou direcionado para a página de seleção dos jogos')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                'div.footer__logo-reclame-aqui.fright > img:nth-child(1)').is_displayed()
    print()

@when(u'clico o incone do perfil e seleciono Ver meu perfil')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a.header__nav-profile-wrapper > i.caret').click()
    context.driver.find_element(By.CSS_SELECTOR,
                                'ul.header__subnav.header__subnav--profile li.header__subnav-item:nth-child(4) > a.header__subnav-link').click()
    print()

@then(u'sou direcionado para página do meu perfil')
def step_impl(context):
    time.sleep(3)
    assert context.driver.find_element(By.CSS_SELECTOR, 'li.nav-secondary__item.active:nth-child(1)').text == 'Perfil'
    print()


@when(u'clico em editar informações')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/p[1]/a[1]').click()
    print()

@then(u'sou direcionado para a página de gerenciamento do meu perfil')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'h1.titulo.titulo--pagina:nth-child(1)').text == 'Gerenciar Conta'
    print()

@when(u'clico em botão editar do campo perfil')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '#perfil .btn').click()
    time.sleep(5)
    print()

@when(u'preencho os campos "cidade" , "estado" , País , sexo e data de nascimento')
def step_impl(context):

    #Mudança o foco para outro frame para correta seleção dos elementos e suas respectivas interações
    context.driver.switch_to.frame(context.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > iframe.cboxIframe"))
    time.sleep(5)
    cidade = context.driver.find_element(By.ID, 'campo-new-city')
    cidade.clear()
    cidade.send_keys('Cariacica')
    time.sleep(2)
    estado = context.driver.find_element(By.ID, 'campo-new-state')
    estado.clear()
    estado.send_keys('Espírito Santo')
    time.sleep(2)
    dropdown = context.driver.find_element(By.ID, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'Brasil']").click()
    context.driver.find_element(By.ID, 'mascGender').click()
    dropdown = context.driver.find_element(By.ID, "birthday")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    dropdown = context.driver.find_element(By.ID, "birthmonth")
    dropdown.find_element(By.XPATH, "//option[. = 'Abril']").click()
    dropdown = context.driver.find_element(By.ID, "birthyear")
    dropdown.find_element(By.XPATH, "//option[. = '1988']").click()
    time.sleep(3)
    print()


@when(u'clico no botão alterar perfil')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.md-btn.md-btn--primary').click()
    time.sleep(2)
    assert context.driver.find_element(By.TAG_NAME, 'span').text == 'Perfil alterado com sucesso'
    context.driver.switch_to.default_content()
    context.driver.find_element(By.CSS_SELECTOR, "#cboxClose").click()
    time.sleep(5)
    print()


@then(u'retorno para a página de gerenciamento de perfil')
def step_impl(context):
    time.sleep(4)
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(2)').text == 'Cariacica'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(6)').text == 'Brasil'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(9)').text == 'Masculino'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(11)').text == '02/04/1988'

    print()
