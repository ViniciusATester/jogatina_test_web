from selenium import webdriver


# Inicio
def before_all(context):
    context.driver = webdriver.Chrome(
        "C:/Users/vinic/PycharmProjects/jogatina_test_web/drivers/chrome/98/chromedriver.exe")

    context.driver.maximize_window()

    context.driver.implicitly_wait(30)

    print('Passo A - Antes de Tudo')


# Final
def after_all(context):
    context.drive.quit()

    print('Passo Z - Depois de tudo')
