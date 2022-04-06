@cadastro_usuario
Feature: Cadastrar novo usuário para jogar
  Scenario Outline: Novo cadastro do usuário e preenchimento e checagem do endereço com sucesso
    Given que acesso o site Jogatina
    When clico no botão cadastre-se
    When preencho o campo "<email>" e "<senha>"
    And clico no botão criar conta
    Then sou direcionado para a página de seleção dos jogos confirmando "<usuario>"

    Examples:
      | email                       | senha  | usuario                     |
      | viniciustestes02@tester.com | 123456 | viniciustestes02@tester.com |
      | viniciustestes03@tester.com | 654321 | viniciustestes03@tester.com |



