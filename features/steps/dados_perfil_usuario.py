import time

from behave import given, then, when
from selenium.webdriver.common.by import By

@when(u'clico no botão entrar e preencho com "{email}" e "{senha}"')
def step_impl(context, email, senha):
    #Clica no botão de entrar no login e efetua o login que foi cadastrado na feature anterior
    #time.sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-verde.header__btn-login.js-login-btn').click()
    #time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, '#email-login').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, '#senha-login').send_keys(senha)
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-verde.btn-entrar.fright:nth-child(5)').click()




@when(u'clico no icone e seleciono ver meu perfil de "{usuario}"')
def step_impl(context, usuario):
    #Valido usuario e clico para ver o perfil
    #time.sleep(3)
    context.driver.find_element(By.XPATH, '//body/div[1]/div[1]/ul[1]/li[6]/a[1]/i[1]').click()
    #time.sleep(3)
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.header__subnav-info-email').text == usuario
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Ver meu Perfil')]").click()



@when(u'sou direcionado para a página do meu perfil e seleciono a opção de editar informacoes')
def step_impl(context):
    #Valida se esta dentro da aba de  perfil e clico em editar informações
    assert context.driver.find_element(By.CSS_SELECTOR, 'li.nav-secondary__item.active:nth-child(1)').text == 'Perfil'
    context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/p[1]/a[1]').click()


@when(u'sou direcionado para a página de gerenciamento do meu perfil')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'h1.titulo.titulo--pagina:nth-child(1)').text == 'Gerenciar Conta'


@when(u'clico em editar no perfil preencho os campos cidade, estado, pais, genero  e nascimento')
def step_impl(context):

    #Mudança o foco para outro frame para correta seleção dos elementos e suas respectivas interações
    context.driver.find_element(By.CSS_SELECTOR, '#perfil .btn').click()
    context.driver.switch_to.frame(context.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > iframe.cboxIframe"))
    #time.sleep(5)
    city = context.driver.find_element(By.ID, 'campo-new-city')
    city.clear()
    city.send_keys('Cariacica')
    #time.sleep(2)
    state = context.driver.find_element(By.ID, 'campo-new-state')
    state.clear()
    state.send_keys('Espirito Santo')
    #time.sleep(2)
    dropdown = context.driver.find_element(By.ID, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'Brasil']").click()
    context.driver.find_element(By.ID, 'mascGender').click()
    dropdown = context.driver.find_element(By.ID, "birthday")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    dropdown = context.driver.find_element(By.ID, "birthmonth")
    dropdown.find_element(By.XPATH, "//option[. = 'Abril']").click()
    dropdown = context.driver.find_element(By.ID, "birthyear")
    dropdown.find_element(By.XPATH, "//option[. = '1988']").click()
    #time.sleep(3)



@when(u'clico no botão alterar perfil e fecho a janela')
def step_impl(context):
    #checagem  se o perfil foi alterado e retorno a página principal
    context.driver.find_element(By.CSS_SELECTOR, 'input.md-btn.md-btn--primary').click()
    #time.sleep(2)
    assert context.driver.find_element(By.TAG_NAME, 'span').text == 'Perfil alterado com sucesso'
    context.driver.switch_to.default_content()
    context.driver.find_element(By.CSS_SELECTOR, "#cboxClose").click()
    #time.sleep(5)



@then(u'retorno para a página de gerenciamento de perfil e saio da conta')
def step_impl(context):
    #Validação das informações que foram alteradas
    #Obs: Não foi checar o estado cadastrado pois ele não está aparecendo corretamente, está aparecendo assim "--"
   # time.sleep(4)
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(2)').text == 'Cariacica'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(6)').text == 'Brasil'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(9)').text == 'Masculino'
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       'div.opcoes--cadastro__descricao > label:nth-child(11)').text == '02/04/1988'
    context.driver.find_element(By.CSS_SELECTOR, 'a.header__nav-profile-wrapper > i.caret').click()
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Sair')]").click()
    #time.sleep(7)


